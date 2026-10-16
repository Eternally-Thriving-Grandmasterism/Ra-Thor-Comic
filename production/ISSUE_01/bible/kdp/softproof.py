# ISSUE01-KDP-WRAP-1: CMYK soft proof of the KDP wrap (checking only; KDP accepts RGB PDFs and converts them itself).
# usage: python3 softproof.py WRAP.jpg [--profile icc/GRACoL2013_CRPC6.icc] [--intent relative|perceptual] [--out DIR]
# Council ruling (Wild, 2026-10-15 11:01 PM ET): RGB masters are the source of truth; soft-proof against GRACoL 2013 (CRPC6), not FOGRA39.
# Little CMS (Pillow ImageCms): sRGB -> CMYK (profile, intent, black-point compensation) -> sRGB proof (relative colorimetric + BPC).
# Both the original and the proof are converted to CIELAB (D65, computed here in numpy) and compared pixel by pixel:
# dE76 > 10 = clearly outside the press gamut (flagged magenta); dE76 5..10 = visibly shifted (amber).
# icc/GRACoL2013_CRPC6.icc: ICC Profile Registry, https://www.color.org/registry/GRACoL2013_CRPC6.xalter (Idealliance; X-Rite copyright;
# 'may be used, embedded, exchanged and shared without restriction', unaltered). TAC 320%, Medium+ GCR, CGATS.21-2 CRPC6.
import argparse, os, json, cv2, numpy as np
from PIL import Image, ImageCms
HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(); ap.add_argument('wrap'); ap.add_argument('--profile', default=os.path.join(HERE, 'icc/GRACoL2013_CRPC6.icc'))
ap.add_argument('--intent', default='relative', choices=['relative', 'perceptual']); ap.add_argument('--out', default=os.path.join(HERE, 'out'))
a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
INT = ImageCms.Intent.RELATIVE_COLORIMETRIC if a.intent == 'relative' else ImageCms.Intent.PERCEPTUAL
F = ImageCms.Flags.BLACKPOINTCOMPENSATION
src = Image.open(a.wrap).convert('RGB'); sRGB = ImageCms.createProfile('sRGB'); LAB = ImageCms.createProfile('LAB', 5000); CMYK = ImageCms.getOpenProfile(a.profile)
pname = ImageCms.getProfileDescription(CMYK).strip(); tag = os.path.splitext(os.path.basename(a.profile))[0] + '_' + a.intent
cmyk = ImageCms.applyTransform(src, ImageCms.buildTransform(sRGB, CMYK, 'RGB', 'CMYK', INT, flags=F))
proof = ImageCms.applyTransform(cmyk, ImageCms.buildTransform(CMYK, sRGB, 'CMYK', 'RGB', ImageCms.Intent.RELATIVE_COLORIMETRIC, flags=F))   # display-matched (BPC)
inkp = ImageCms.applyTransform(cmyk, ImageCms.buildTransform(CMYK, sRGB, 'CMYK', 'RGB', ImageCms.Intent.RELATIVE_COLORIMETRIC))          # 'simulate black ink': no BPC on the way back
def lab(im):
    c = np.asarray(im, np.float32) / 255; c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    M = np.array([[0.4124564, 0.3575761, 0.1804375], [0.2126729, 0.7151522, 0.0721750], [0.0193339, 0.1191920, 0.9503041]], np.float32)
    xyz = c @ M.T / np.array([0.95047, 1.0, 1.08883], np.float32)
    f = np.where(xyz > 216 / 24389, np.cbrt(xyz), (24389 / 27 * xyz + 16) / 116)
    return np.dstack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])])
LO, LP, LI = lab(src), lab(proof), lab(inkp)
dE = np.sqrt(((LO - LP) ** 2).sum(2))                 # gamut clipping as seen on a display-matched proof
dAB = np.sqrt(((LO[..., 1:] - LI[..., 1:]) ** 2).sum(2))   # chroma/hue shift with black ink simulated
dLI = LI[..., 0] - LO[..., 0]                          # lightness lift with black ink simulated (obsidian check)
C = np.asarray(cmyk, np.float32) * 100 / 255; tac = C.sum(2)
rgb = np.asarray(src); hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV); H, S, V = hsv[..., 0], hsv[..., 1], hsv[..., 2]   # H 0..179
cls = {'rose-gold / copper (hue 10-24 deg)': (H >= 5) & (H < 12) & (S > 90) & (V > 110),
       'gold / amber (hue 24-56 deg)': (H >= 12) & (H < 28) & (S > 90) & (V > 110),
       'blue / white-blue lightning (hue 190-260 deg)': (H >= 95) & (H <= 130) & (S > 35) & (V > 110),
       'obsidian / near-black (V < 60)': V < 60,
       'whole cover': np.ones(H.shape, bool)}
stats = {'profile': pname, 'intent': a.intent + ' + black-point compensation', 'flag_rule': 'dE76 > 10 out of gamut; 5..10 shifted',
         'tac_max_pct': round(float(tac.max()), 1), 'tac_p99_pct': round(float(np.percentile(tac, 99)), 1), 'classes': {}}
for k, m in cls.items():
    n = int(m.sum()); d = dE[m] if n else np.zeros(1)
    stats['classes'][k] = dict(pixels=n, ink_sim_mean_dL=round(float(dLI[m].mean()) if n else 0, 2), ink_sim_p95_dAB=round(float(np.percentile(dAB[m], 95)) if n else 0, 2),
                               ink_sim_max_dAB=round(float(dAB[m].max()) if n else 0, 2), pct_of_cover=round(100 * n / m.size, 2), mean_dE=round(float(d.mean()), 2), p95_dE=round(float(np.percentile(d, 95)), 2),
                               pct_shifted_5_10=round(100 * float(((d > 5) & (d <= 10)).mean()), 2), pct_out_gt10=round(100 * float((d > 10).mean()), 2))
# flag map: greyscale proof + amber where 5..10, magenta where >10
g = cv2.cvtColor(np.asarray(proof), cv2.COLOR_RGB2GRAY); FL = np.dstack([g, g, g]).astype(np.float32) * 0.55
FL[(dE > 5) & (dE <= 10)] = (255, 170, 0); FL[dE > 10] = (255, 0, 255)
def lbl(img, t):
    img = img.copy(); cv2.rectangle(img, (0, 0), (img.shape[1], 46), (0, 0, 0), -1); cv2.putText(img, t, (12, 32), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2, cv2.LINE_AA); return img
P = np.asarray(proof); O = rgb; FLu = FL.astype(np.uint8); h = 900; w = O.shape[1] * h // O.shape[0]
rs = lambda im: cv2.resize(im, (w, h), interpolation=cv2.INTER_AREA)
PI = np.asarray(inkp)
side = np.vstack([lbl(rs(O), 'sRGB original (what KDP receives)'), lbl(rs(P), 'CMYK soft proof: %s, %s + BPC (display-matched)' % (pname, a.intent)),
                  lbl(rs(PI), 'CMYK soft proof, black ink simulated (no BPC on return): obsidian lift'),
                  lbl(rs(FLu), 'gamut flags: amber dE 5-10 shifted, magenta dE>10 out of gamut')])
Image.fromarray(side).save(os.path.join(a.out, 'softproof_%s_side_by_side.jpg' % tag), quality=90)
# 100% crops: front title band (rose-gold bolt + gold), sun-eye sigil (gold), blue lightning
W0 = O.shape[1] - 2025
crops = {'title_rosegold': (W0 + 1150, 60, W0 + 2000, 420), 'sigil_gold': (W0 + 750, 300, W0 + 1300, 850), 'blue_lightning': (W0 + 1450, 500, W0 + 2025, 1500)}
rows = []
for k, (x0, y0, x1, y1) in crops.items():
    tiles = [O[y0:y1, x0:x1], P[y0:y1, x0:x1], PI[y0:y1, x0:x1], FLu[y0:y1, x0:x1]]; hh = 520; tiles = [cv2.resize(t, (t.shape[1] * hh // t.shape[0], hh), interpolation=cv2.INTER_AREA) for t in tiles]
    rows.append(lbl(np.hstack(tiles), '%s: original | proof (BPC) | proof (black ink sim) | flags' % k))
mw = max(r.shape[1] for r in rows); rows = [np.pad(r, ((0, 0), (0, mw - r.shape[1]), (0, 0))) for r in rows]
Image.fromarray(np.vstack(rows)).save(os.path.join(a.out, 'softproof_%s_crops.jpg' % tag), quality=90)
json.dump(stats, open(os.path.join(a.out, 'softproof_%s.json' % tag), 'w'), indent=1); print(json.dumps(stats, indent=1))
