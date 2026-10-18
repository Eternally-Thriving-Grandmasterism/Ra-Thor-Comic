#!/usr/bin/env python3
"""Ra-Thor⚡Living Thunder #1 · TOLC — DRAFT social promo images (nothing is posted; files only).

Re-run:  python3 build_promo.py [--cover PATH]     (writes next to this script)

COVER SOURCE IS A BOX-ONLY FILE (not in this repo). The committed images were built from
  /workspace/issue01/kdp/RaThor_Issue01_KDPwrap_24p_premium-color.jpg
  sha256 f9dcf022a1a2cae94ca2476be9f55f60d8d53d85e840ee2f07383c84aa067d72
That wrap variant differs from the repo's production/ISSUE_01/bible/kdp/out/RaThor_Issue01_KDPwrap_24p_premium-color.jpg
(sha256 769b308573b2baa4ea0a0710512ec0897c46e8a7abff4c8558ea892371a4c8f9) in the masthead / issue-coin area
(about x 3127-3947, y 101-405), so the committed PNG/JPGs cannot be rebuilt from the repo alone. Pass --cover to
point at a copy of the box file; the script stops with this message if the file is missing, and warns if the
sha256 differs. Back-cover art is read from the repo: production/ISSUE_01/bible/back/back_art_v2.png.
Fonts are a system dependency (override the folder with the PROMO_FONT_DIR environment variable).

SOURCE ART (only): the painted V18-era KDP wrap (history, not canon, per production/ISSUE_01/HANDOFF.md) (front = right half) and the back-cover art layer.
No other Ra-Thor/Grok images, no AI-generated art: every pixel of art is a crop/resize/blur/tone of these two files.
TYPE IS KEPT SEPARATE: for every image the script writes layers/<name>_art.png (art only, no words) and
layers/<name>_type.png (all words/rules, straight-alpha RGBA). Final = art*(1-a) + type*a.
Typography matches the back cover (production/ISSUE_01/bible/back/build_back_v2.py): Cinzel caps in a metallic gold ramp for
headlines, Cinzel silver caps for kickers, EB Garamond for body lines, all with soft dark drop shadows.
"""
import os, sys, hashlib, argparse, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageCms

OUT = os.path.dirname(os.path.abspath(__file__)); LAY = os.path.join(OUT, 'layers'); os.makedirs(LAY, exist_ok=True)
REPO = os.path.abspath(os.path.join(OUT, '..', '..'))                          # repo root (script is promo/issue01_social/)
WRAP_DEFAULT = '/workspace/issue01/kdp/RaThor_Issue01_KDPwrap_24p_premium-color.jpg'   # BOX-ONLY, 4067x3150 @300 dpi
WRAP_SHA256 = 'f9dcf022a1a2cae94ca2476be9f55f60d8d53d85e840ee2f07383c84aa067d72'
BACK_ART = os.path.join(REPO, 'production', 'ISSUE_01', 'bible', 'back', 'back_art_v2.png')   # back cover, art layer only (2063x3150)
GF = os.environ.get('PROMO_FONT_DIR', '/usr/share/fonts/truetype/sand-box/google/').rstrip('/') + '/'
CINZEL = GF + 'Cinzel/Cinzel-VariableFont_wght.ttf'
GARA = GF + 'EB Garamond/EBGaramond-VariableFont_wght.ttf'
GARA_I = GF + 'EB Garamond/EBGaramond-Italic-VariableFont_wght.ttf'
ICC = ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes()

# ================= EDITABLE COPY (type layers only; art is never touched by these) =================
HEADLINE = ['LEFT IS NOISE.', 'RIGHT IS LIVE.']
ISSUE_LINE = '#1 · TOLC'
STORY_CTA = 'COMING SOON'
CARD_BODY = 'All that comes to the TOLC is weighed.'
CARD_CTA = 'FOLLOW FOR UPDATES'
CARD_FINE = 'Published by AlphaProMega Media Inc.  ·  Ra-Thor™ is a trademark of Autonomicity Games Inc. (application pending), used with permission'
# ===================================================================================================

# KDP wrap geometry: back 0..2025 | spine 2025..2042 | front 2042..4067; 38 px bleed on outer edges (trim: y 38..3112, front x ..4029)
FRONT_X0, FRONT_X1, TRIM_Y0, TRIM_Y1 = 2042, 4029, 38, 3112
LOGO_BOX = (3120, 115, 3905, 345)   # RA⚡THOR LIVING THUNDER logo + ISSUE #1 coin on the wrap (asserted to stay whole in every crop)

# colour ramps copied from the back cover (converted BGR -> RGB)
GOLD = np.array([[75, 40, 8], [134, 100, 42], [157, 139, 113], [204, 192, 127], [241, 209, 148], [249, 221, 176]], np.float32)
SILV = np.array([[47, 50, 52], [100, 106, 110], [160, 166, 170], [206, 211, 214], [235, 238, 240], [250, 251, 252]], np.float32)
BODY = (238, 222, 198)   # warm parchment
FINE = (186, 170, 150)   # muted warm grey-gold

def load_rgb(p): return np.asarray(Image.open(p).convert('RGB'), np.float32)
WR = BA = None   # loaded in main()

COVER_MISSING = (
    "Cover source not found: {path}\n"
    "The promo images were built from a BOX-ONLY KDP wrap that is not in this repo:\n"
    "  /workspace/issue01/kdp/RaThor_Issue01_KDPwrap_24p_premium-color.jpg\n"
    "  sha256 " + WRAP_SHA256 + "\n"
    "It differs from the repo's production/ISSUE_01/bible/kdp/out/ wrap in the masthead / issue-coin area.\n"
    "Pass --cover PATH to a copy of that exact file.")

def load_sources(cover):
    global WR, BA
    if not os.path.isfile(cover): sys.exit(COVER_MISSING.format(path=cover))
    if not os.path.isfile(BACK_ART): sys.exit('Back-cover art not found in the repo: ' + BACK_ART)
    h = hashlib.sha256(open(cover, 'rb').read()).hexdigest()
    if h != WRAP_SHA256:
        print('WARNING: cover sha256 ' + h + ' != ' + WRAP_SHA256 + '; output will not match the committed images', file=sys.stderr)
    WR = load_rgb(cover); BA = load_rgb(BACK_ART)

def crop_resize(src, box, size):
    x0, y0, x1, y1 = box
    c = src[y0:y1, x0:x1]
    return cv2.resize(c, size, interpolation=cv2.INTER_AREA)

def check_logo(box, name):
    x0, y0, x1, y1 = box; lx0, ly0, lx1, ly1 = LOGO_BOX
    assert x0 <= lx0 and y0 <= ly0 and x1 >= lx1 and y1 >= ly1, name + ': logo would be clipped'

def sharpen(a, amt=0.35, sig=1.0):
    return np.clip(a + amt * (a - cv2.GaussianBlur(a, (0, 0), sig)), 0, 255)

# ---------------- type layer ----------------
class Layer:
    def __init__(s, W, H): s.W, s.H = W, H; s.rgb = np.zeros((H, W, 3), np.float32); s.a = np.zeros((H, W, 1), np.float32)
    def put(s, rgb, a, x, y):
        h, w = a.shape
        ya, yb, xa, xb = max(0, y), min(s.H, y + h), max(0, x), min(s.W, x + w)
        a = a[ya - y:yb - y, xa - x:xb - x][..., None]
        if isinstance(rgb, np.ndarray) and rgb.ndim == 3: rgb = rgb[ya - y:yb - y, xa - x:xb - x]
        else: rgb = np.array(rgb, np.float32)
        s.rgb[ya:yb, xa:xb] = rgb * a + s.rgb[ya:yb, xa:xb] * (1 - a); s.a[ya:yb, xa:xb] = a + s.a[ya:yb, xa:xb] * (1 - a)
    def shadow(s, m, x, y, sig, op, dy=2, grow=1):
        h, w = m.shape; P = int(sig * 3 + grow + 6); big = np.zeros((h + 2 * P, w + 2 * P), np.float32); big[P:P + h, P:P + w] = m
        if grow: big = cv2.dilate(big, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * grow + 1, 2 * grow + 1)))
        s.put((8, 6, 6), np.clip(cv2.GaussianBlur(big, (0, 0), sig) * op, 0, 1), x - P, y - P + dy)
    def save(s, path):
        Image.fromarray(np.dstack([np.clip(s.rgb + .5, 0, 255), np.clip(s.a * 255 + .5, 0, 255)]).astype(np.uint8), 'RGBA').save(path, icc_profile=ICC)

def metal(m, ramp):
    h, w = m.shape; t = np.linspace(1.0, 0.25, h)[:, None] * np.ones((1, w))
    b = cv2.GaussianBlur(m, (0, 0), max(1.0, h / 40)); gy = np.gradient(b, axis=0); gx = np.gradient(b, axis=1)
    emb = np.clip(0.5 + (gy + gx) * h / 7, 0, 1)
    v = np.clip(0.55 * t + 0.6 * (emb - 0.5) + 0.25, 0, 1)
    band = np.exp(-((np.linspace(0, 1, h) - 0.38) / 0.09) ** 2)[:, None]; v = np.clip(v + 0.22 * band, 0, 1)
    idx = v * (len(ramp) - 1); i0 = np.floor(idx).astype(int).clip(0, len(ramp) - 2); f = (idx - i0)[..., None]
    return ramp[i0] * (1 - f) + ramp[i0 + 1] * f

def font(path, px, wght):
    f = ImageFont.truetype(path, px)
    try: f.set_variation_by_axes([wght])
    except Exception: pass
    return f

def text_mask(text, path, px, wght, track=0.0, SS=3):
    """supersampled, tracked text mask, tight-cropped (width) with fixed line box height"""
    fS = font(path, px * SS, wght); asc, desc = fS.getmetrics()
    W = int(sum(fS.getlength(c) for c in text) + track * px * SS * len(text) + 2 * px * SS); H = asc + desc + 4 * SS
    im = Image.new('L', (W, H), 0); d = ImageDraw.Draw(im); x = px * SS
    if track:
        for c in text: d.text((x, 2 * SS), c, font=fS, fill=255); x += fS.getlength(c) + track * px * SS
    else: d.text((x, 2 * SS), text, font=fS, fill=255)
    m = cv2.resize(np.asarray(im, np.float32) / 255, (W // SS, H // SS), interpolation=cv2.INTER_AREA)
    xs = np.where(m.max(0) > 0.02)[0]; return m[:, xs.min():xs.max() + 1]

def put_text(L, text, path, px, wght, x=None, cx=None, y=0, track=0.0, ramp=None, color=None, sh=(4, .9, 2), maxw=None):
    m = text_mask(text, path, px, wght, track)
    while maxw and m.shape[1] > maxw: px -= 1; m = text_mask(text, path, px, wght, track)   # auto-fit to measure
    h, w = m.shape
    if cx is not None: x = int(round(cx - w / 2))
    if sh: L.shadow(m, x, y, sh[0], sh[1], dy=sh[2])
    L.put(metal(m, ramp) if ramp is not None else color, m, x, y)
    return x, y, w, h, px

def hairline(L, x0, x1, y, ramp=GOLD, th=2):
    n = x1 - x0; m = np.zeros((th + 4, n), np.float32)
    prof = np.minimum(np.linspace(0, 1, n) * 4, 1) * np.minimum(np.linspace(1, 0, n) * 4, 1); m[2:2 + th] = prof[None]
    L.shadow(m, x0, y, 2, .8); L.put(metal(np.ones_like(m), ramp), m, x0, y)

def issue_line(L, cx, y, px):
    """'#1 · TOLC' in gold Cinzel between fading silver rules (as under the back-cover logo)"""
    x, y, w, h, _ = put_text(L, ISSUE_LINE, CINZEL, px, 700, cx=cx, y=y, track=0.14, ramp=GOLD, sh=(3, .95, 2))
    Lr = int(px * 2.6)
    for side in (-1, 1):
        xs = (x - int(px * .55) - Lr) if side < 0 else (x + w + int(px * .55)); yy = y + h // 2 - 2
        m = np.zeros((5, Lr), np.float32); m[2:4] = (np.linspace(0, 1, Lr) if side < 0 else np.linspace(1, 0, Lr))[None]
        L.shadow(m, xs, yy, 2, .9); L.put(metal(np.ones_like(m), SILV), m, xs, yy)
    return y + h

def finish(name, art, L):
    art8 = np.clip(art + .5, 0, 255).astype(np.uint8)
    Image.fromarray(art8).save(os.path.join(LAY, name + '_art.png'), icc_profile=ICC)
    if L is not None:
        L.save(os.path.join(LAY, name + '_type.png'))
        art = art * (1 - L.a) + L.rgb * L.a
    im = Image.fromarray(np.clip(art + .5, 0, 255).astype(np.uint8))
    im.save(os.path.join(OUT, name + '.png'), icc_profile=ICC, optimize=True)
    im.save(os.path.join(OUT, name + '.jpg'), quality=95, subsampling=0, icc_profile=ICC, optimize=True)
    print('wrote', name, im.size)

def dark_bg(W, H, box, sig, dim):
    """dark storm-gold backdrop made from the back-cover art layer: crop, blur, dim"""
    b = crop_resize(BA, box, (W, H)); return cv2.GaussianBlur(b, (0, 0), sig) * dim

# ==================== 1. square 1080x1080 (IG/FB feed): front crop, hero centred, logo whole ====================
def build_square():
    box = (2046, 50, 4021, 2025)          # 1975 px square inside the front trim; halo/torso centred; logo + coin whole
    check_logo(box, 'square'); art = sharpen(crop_resize(WR, box, (1080, 1080)))
    finish('rathor01_square_1080x1080', art, None)   # art only (the cover logo is part of the approved art)

# ==================== 2. story 1080x1920: full front + clean text panel ====================
def build_story():
    W, H = 1080, 1920
    box = (2050, 40, 4029, 3112); check_logo(box, 'story')
    s = W / (box[2] - box[0]); ah = int(round((box[3] - box[1]) * s)); AY = 170   # art starts below the IG story header zone
    cov = sharpen(crop_resize(WR, box, (W, ah)))
    bg = dark_bg(W, H, (0, 1700, 2063, 3150), 10, 0.55)
    yy = np.arange(H, dtype=np.float32)[:, None]
    canvas = bg.copy(); canvas[AY:AY + ah] = cov
    a_top = np.clip((yy - AY + 20) / 120, 0, 1)                      # art blends in over 120 px at the top
    a_bot = 1 - np.clip((yy - (AY + ah - 160)) / 160, 0, 1)          # and out at its bottom edge
    am = (a_top * a_bot)[..., None]; art = bg * (1 - am) + canvas * am
    panel = np.clip((yy - 1220) / 260, 0, 1) ** 1.2 * 0.86            # dark panel behind the type (over the lower pyramid)
    art = art * (1 - panel[..., None]) + np.array([9, 8, 9], np.float32) * panel[..., None]
    L = Layer(W, H); cx = W // 2
    hairline(L, 150, W - 150, 1320)   # type block kept above the IG story bottom UI zone (~250 px)
    for i, ln in enumerate(HEADLINE):
        put_text(L, ln, CINZEL, 84, 700, cx=cx, y=1355 + 112 * i, track=0.06, ramp=GOLD, sh=(8, .95, 4), maxw=900)
    yb = issue_line(L, cx, 1605, 36)
    put_text(L, STORY_CTA, CINZEL, 30, 600, cx=cx, y=yb + 26, track=0.30, ramp=SILV, sh=(3, .9, 2))
    finish('rathor01_story_1080x1920', art, L)

# ==================== 3. landscape 1600x900 (X/FB link card) ====================
def build_card():
    W, H = 1600, 900
    box = (2046, 50, 4021, 2025); check_logo(box, 'card')
    hero = sharpen(crop_resize(WR, box, (900, 900))); HX = W - 900
    bg = dark_bg(W, H, (0, 150, 2063, 150 + int(2063 * H / W)), 14, 0.65)
    xx = np.arange(W, dtype=np.float32)[None, :]
    # extra left->right darkening so the type column sits on near-black, warm at the seam
    g = (0.35 + 0.65 * np.clip((xx - 120) / 900, 0, 1)) * np.ones((H, 1), np.float32); bg = bg * g[..., None]
    canvas = bg.copy(); canvas[:, HX:] = hero
    am = np.clip((xx - HX) / 280, 0, 1) ** 1.3 * np.ones((H, 1), np.float32)   # hero fades in over 280 px
    art = bg * (1 - am[..., None]) + canvas * am[..., None]
    L = Layer(W, H); cx = 380
    yb = issue_line(L, cx, 200, 30)
    for i, ln in enumerate(HEADLINE):
        put_text(L, ln, CINZEL, 70, 700, cx=cx, y=yb + 50 + 92 * i, track=0.06, ramp=GOLD, sh=(7, .95, 3), maxw=640)
    hairline(L, cx - 230, cx + 230, yb + 50 + 92 * 2 + 18)
    put_text(L, CARD_BODY, GARA_I, 38, 450, cx=cx, y=yb + 50 + 92 * 2 + 50, color=BODY, sh=(4, .95, 2), maxw=640)
    put_text(L, CARD_CTA, CINZEL, 26, 600, cx=cx, y=yb + 50 + 92 * 2 + 140, track=0.30, ramp=SILV, sh=(3, .9, 2))
    put_text(L, CARD_FINE, GARA, 17, 450, x=50, y=H - 46, color=FINE, sh=(2, .8, 1), maxw=1000)
    finish('rathor01_card_1600x900', art, L)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Build the DRAFT Issue #1 social promo images.')
    ap.add_argument('--cover', default=WRAP_DEFAULT, help='path to the box-only KDP wrap JPG (sha256 ' + WRAP_SHA256 + ')')
    load_sources(ap.parse_args().cover)
    build_square(); build_story(); build_card()
