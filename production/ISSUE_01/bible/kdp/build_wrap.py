# ISSUE01-KDP-WRAP-1: parametric KDP paperback full cover (back | spine | front) for Issue 1.
# usage: python3 build_wrap.py --pages N --paper {premium-color,standard-color,white,cream} [--out DIR] [--placeholder] [--spine-text TEXT]
# Council ruling (Wild, 2026-10-15 11:01 PM ET): interior 24 pages (or the next even count up to ~32) from the story as written plus
# front/back matter; white paper, Premium Color ink ('premium-color'); trim 6.625 x 10.25 in, bleed on; spine BLANK (no text) with the
# cover background carried across; a separate text-ready spine layer is kept for a future collected edition over 79 pages.
#
# Spec source (checked 2026-10-15 ET): KDP "Create a Paperback Cover", https://kdp.amazon.com/en_US/help/topic/G201953020
#   Cover Width  = Bleed + Back Cover Width + Spine Width + Front Cover Width + Bleed;  Cover Height = Bleed + Trim Height + Bleed
#   bleed 0.125 in;  spine = pages x 0.002252 (white / standard color), 0.0025 (cream), 0.002347 (premium color) in per page
#   spine text only on books with more than 79 pages, 0.0625 in clear each side of the spine;  allow 0.0625 in variance at each fold
# Page minimums (KDP "Paperback Submission Guidelines" / trim-size table, https://kdp.amazon.com/en_US/help/topic/G201834180):
#   24 pages (black ink white/cream, premium color), 72 pages (standard color).  Trim 6.625 x 10.25 in is a custom, large trim.
# Barcode (KDP Print Publishing Guidelines PDF): 2.0 x 1.2 in, bottom 0.25 in above bottom trim, right edge 0.25 in left of the spine (LTR).
#
# Inputs (all in this repo, never modified):
#   back art  ../back/back_art_v2.png            back type ../back/back_type_layer_v2.png     (print = art*(1-a) + type*a)
#   front art ../RaThor_Issue01_Cover_V18_art_notext_4x_4608x6912.png, fitted exactly as v18/build_v18.py (INTER_AREA to h 3150, centre crop 2063)
#   front type ../v18/type_layer_final_v18.png
# Each 2063 px sheet = 0.125 in bleed (37 px) + trim + bleed.  The wrap keeps the back sheet's left bleed and the front sheet's right bleed,
# drops the bleed that would sit on the spine, and fills the spine with a smooth per-row blend of the two facing edge columns (no hard edge,
# no text, no new art).  The type layers stay separate (wrap_type_layer); type meets art only in the final print / PDF export.
import argparse, os, sys, json, cv2, numpy as np
from PIL import Image, ImageCms

PER_PAGE = {'white': 0.002252, 'cream': 0.0025, 'premium-color': 0.002347, 'standard-color': 0.002252}
MIN_PAGES = {'white': 24, 'cream': 24, 'premium-color': 24, 'standard-color': 72}
DPI, BLEED_IN, TRIM_W, TRIM_H = 300, 0.125, 6.625, 10.25
SHEET_W, SHEET_H, BL = 2063, 3150, 37                       # existing sheets (front #91 / back #92)
PANEL = 2025                                                 # bleed + trim = 6.75 in x 300 dpi, taken from each sheet
HERE = os.path.dirname(os.path.abspath(__file__)); BIB = os.path.dirname(HERE)

def spec(pages, paper):
    spine = pages * PER_PAGE[paper]
    w_in = BLEED_IN + TRIM_W + spine + TRIM_W + BLEED_IN; h_in = BLEED_IN + TRIM_H + BLEED_IN
    return dict(pages=pages, paper=paper, per_page_in=PER_PAGE[paper], spine_in=round(spine, 6), spine_mm=round(spine * 25.4, 3),
                cover_w_in=round(w_in, 6), cover_h_in=h_in, cover_w_mm=round(w_in * 25.4, 3), cover_h_mm=round(h_in * 25.4, 3),
                px_w=round(w_in * DPI), px_h=round(h_in * DPI), spine_text_allowed=pages > 79,
                source='https://kdp.amazon.com/en_US/help/topic/G201953020')

def front_art():
    U = cv2.imread(os.path.join(BIB, 'RaThor_Issue01_Cover_V18_art_notext_4x_4608x6912.png'))
    k = SHEET_H / U.shape[0]; W = round(U.shape[1] * k)
    A = cv2.resize(U, (W, SHEET_H), interpolation=cv2.INTER_AREA); cx = (W - SHEET_W) // 2
    return A[:, cx:cx + SHEET_W].astype(np.float32)

def rgba(path):
    T = cv2.imread(path, -1).astype(np.float32); return T[..., :3], T[..., 3:] / 255

def save_rgb(path, bgr, quality=95, icc=True):
    im = Image.fromarray(cv2.cvtColor(np.clip(bgr + .5, 0, 255).astype(np.uint8), cv2.COLOR_BGR2RGB))
    kw = dict(dpi=(DPI, DPI))
    if icc: kw['icc_profile'] = ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes()
    if path.lower().endswith('.jpg'): kw.update(quality=quality, subsampling=0)
    im.save(path, **kw)

def write_pdf(path, jpg_path, w_in, h_in, px_w, px_h):
    """one-page PDF, MediaBox at the exact KDP size in points, the JPEG embedded as-is (DCTDecode, DeviceRGB, no ICC, no marks)"""
    data = open(jpg_path, 'rb').read(); W, H = w_in * 72, h_in * 72
    content = b'q %.4f 0 0 %.4f 0 0 cm /Im0 Do Q' % (W, H)
    objs = [b'<< /Type /Catalog /Pages 2 0 R >>',
            b'<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
            b'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 %.4f %.4f] /TrimBox [0 0 %.4f %.4f] /Resources << /XObject << /Im0 4 0 R >> >> /Contents 5 0 R >>' % (W, H, W, H),
            b'<< /Type /XObject /Subtype /Image /Width %d /Height %d /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length %d >>\nstream\n' % (px_w, px_h, len(data)) + data + b'\nendstream',
            b'<< /Length %d >>\nstream\n' % len(content) + content + b'\nendstream',
            b'<< /Title (Ra-Thor Living Thunder #1 - KDP paperback cover) /Producer (build_wrap.py) >>']
    out = b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n'; offs = []
    for i, o in enumerate(objs, 1):
        offs.append(len(out)); out += b'%d 0 obj\n' % i + o + b'\nendobj\n'
    x = len(out); out += b'xref\n0 %d\n0000000000 65535 f \n' % (len(objs) + 1) + b''.join(b'%010d 00000 n \n' % o for o in offs)
    out += b'trailer\n<< /Size %d /Root 1 0 R /Info 6 0 R >>\nstartxref\n%d\n%%%%EOF\n' % (len(objs) + 1, x)
    open(path, 'wb').write(out)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--pages', type=int, required=True); ap.add_argument('--paper', choices=PER_PAGE, required=True)
    ap.add_argument('--out', default=os.path.join(HERE, 'out')); ap.add_argument('--placeholder', action='store_true',
                    help='label outputs PLACEHOLDER (page count / paper not ruled)')
    ap.add_argument('--spine-text', default='', help='only for books over 79 pages (future collected edition); rendered to the separate spine layer only')
    a = ap.parse_args()
    if a.spine_text and a.pages <= 79: sys.exit('REFUSED: KDP prints spine text only on books with more than 79 pages (got %d); Issue 1 spine stays blank' % a.pages)
    if a.pages < MIN_PAGES[a.paper]: sys.exit('REFUSED: %s needs at least %d pages on KDP (got %d)' % (a.paper, MIN_PAGES[a.paper], a.pages))
    S = spec(a.pages, a.paper); os.makedirs(a.out, exist_ok=True)
    tag = '%dp_%s%s' % (a.pages, a.paper, '_PLACEHOLDER' if a.placeholder else '')
    W, H = S['px_w'], S['px_h']; SP0, SP1 = PANEL, W - PANEL               # spine px span
    # --- layers ---
    BA = cv2.imread(os.path.join(BIB, 'back/back_art_v2.png')).astype(np.float32); BT, Ba = rgba(os.path.join(BIB, 'back/back_type_layer_v2.png'))
    FA = front_art(); FT, Fa = rgba(os.path.join(BIB, 'v18/type_layer_final_v18.png'))
    for nm, art, t, al, prn in (('back', BA, BT, Ba, 'RaThor_Issue01_BackCover_v2_6.625x10.25_bleed_300dpi.jpg'),
                                ('front', FA, FT, Fa, 'RaThor_Issue01_Cover_BIBLE_FINAL_6.625x10.25_bleed_300dpi.jpg')):
        d = np.abs(art * (1 - al) + t * al - cv2.imread(os.path.join(BIB, prn)).astype(np.float32))
        print('%s layers vs committed print: mean |diff| %.2f (JPEG q97 noise)' % (nm, d.mean())); assert d.mean() < 2
    ART = np.zeros((H, W, 3), np.float32); TR = np.zeros((H, W, 3), np.float32); TA = np.zeros((H, W, 1), np.float32)
    ART[:, :PANEL] = BA[:, :PANEL]; TR[:, :PANEL] = BT[:, :PANEL]; TA[:, :PANEL] = Ba[:, :PANEL]           # back: left bleed + trim
    ART[:, SP1:] = FA[:, BL:BL + PANEL]; TR[:, SP1:] = FT[:, BL:BL + PANEL]; TA[:, SP1:] = Fa[:, BL:BL + PANEL]  # front: trim + right bleed
    if SP1 > SP0:                                                           # spine: per-row blend of the facing edge columns, softened
        L = cv2.GaussianBlur(BA[:, PANEL - 6:PANEL].mean(1), (1, 31), 0)
        R = cv2.GaussianBlur(FA[:, BL:BL + 6].mean(1), (1, 31), 0)
        t = np.linspace(0, 1, SP1 - SP0 + 2)[1:-1][None, :, None]
        ART[:, SP0:SP1] = L[:, None, :] * (1 - t) + R[:, None, :] * t
    assert float(TA[:, SP0:SP1].max(initial=0)) == 0.0, 'no type on the spine'
    # --- barcode zone (KDP: 2.0 x 1.2 in; bottom 0.25 in above bottom trim; right edge 0.25 in left of the spine fold) ---
    bx1 = SP0 - 0.25 * DPI; bx0 = bx1 - 2.0 * DPI; by1 = H - BLEED_IN * DPI - 0.25 * DPI; by0 = by1 - 1.2 * DPI
    zone = (int(np.floor(bx0)), int(np.floor(by0)), int(np.ceil(bx1)), int(np.ceil(by1)))
    bz = int((TA[zone[1]:zone[3], zone[0]:zone[2]] > 0.02).sum()); print('KDP barcode zone px', zone, 'type pixels inside:', bz); assert bz == 0
    # --- text-ready spine layer (separate RGBA, never merged into this build's print unless --spine-text is given for an 80+ page book) ---
    sm_px = int(round(0.0625 * DPI)); SPL = np.zeros((H, max(SP1 - SP0, 1), 4), np.uint8)
    if a.spine_text:
        from PIL import ImageDraw, ImageFont
        fnt = '/usr/share/fonts/truetype/sand-box/google/Cinzel/Cinzel-VariableFont_wght.ttf'
        avail = SP1 - SP0 - 2 * sm_px; px = int(avail); assert px >= 7 / 72 * DPI, 'spine too thin for 7 pt text at this page count'
        f = ImageFont.truetype(fnt, px); tw = int(f.getlength(a.spine_text)) + 20
        im = Image.new('L', (tw, int(px * 1.5)), 0); ImageDraw.Draw(im).text((10, int(px * .2)), a.spine_text, font=f, fill=255)
        m = np.asarray(im.rotate(-90, expand=True)); y0 = (H - m.shape[0]) // 2; x0 = (SPL.shape[1] - m.shape[1]) // 2
        SPL[y0:y0 + m.shape[0], x0:x0 + m.shape[1], :3] = (110, 200, 240); SPL[y0:y0 + m.shape[0], x0:x0 + m.shape[1], 3] = m
        sa = SPL[..., 3:].astype(np.float32) / 255; TR[:, SP0:SP1] = SPL[..., :3] * sa + TR[:, SP0:SP1] * (1 - sa); TA[:, SP0:SP1] = np.maximum(TA[:, SP0:SP1], sa)
    cv2.imwrite(os.path.join(a.out, 'RaThor_Issue01_KDPwrap_%s_spine_text_layer.png' % tag), SPL)
    # --- outputs ---
    PRINT = ART * (1 - TA) + TR * TA
    jpg = os.path.join(a.out, 'RaThor_Issue01_KDPwrap_%s.jpg' % tag); save_rgb(jpg, PRINT, 95, icc=True)
    pdf_jpg = os.path.join(a.out, '_pdf_payload.jpg'); save_rgb(pdf_jpg, PRINT, 95, icc=False)
    pdf = os.path.join(a.out, 'RaThor_Issue01_KDPwrap_%s.pdf' % tag); write_pdf(pdf, pdf_jpg, S['cover_w_in'], S['cover_h_in'], W, H); os.remove(pdf_jpg)
    Ls = np.dstack([np.clip(TR + .5, 0, 255), np.clip(TA * 255 + .5, 0, 255)]).astype(np.uint8)
    cv2.imwrite(os.path.join(a.out, 'RaThor_Issue01_KDPwrap_%s_type_layer.png' % tag), Ls)
    # guides (preview only, never uploaded)
    G = np.clip(PRINT + .5, 0, 255).astype(np.uint8).copy(); b = int(round(BLEED_IN * DPI)); s = int(round(0.25 * DPI)); sm = int(round(0.0625 * DPI))
    cv2.rectangle(G, (b, b), (W - 1 - b, H - 1 - b), (0, 0, 255), 3)                       # trim (red)
    for x in (SP0, SP1): cv2.line(G, (x, 0), (x, H), (0, 255, 255), 3)                       # spine folds (yellow)
    for x in (SP0 - sm, SP1 + sm): cv2.line(G, (x, 0), (x, H), (0, 160, 255), 1)              # fold variance 0.0625 in (orange)
    cv2.rectangle(G, (b + s, b + s), (SP0 - s, H - 1 - b - s), (255, 255, 0), 2)              # back safe 0.25 in (cyan)
    cv2.rectangle(G, (SP1 + s, b + s), (W - 1 - b - s, H - 1 - b - s), (255, 255, 0), 2)      # front safe
    cv2.rectangle(G, zone[:2], zone[2:], (255, 0, 255), 4); cv2.putText(G, 'KDP BARCODE 2.0x1.2 in (KDP places it)', (zone[0] + 14, zone[1] + 44), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 255), 2, cv2.LINE_AA)
    lab = '%s | %d pages, %s | spine %.4f in | %.4f x %.4f in | %d x %d px @300 | %s' % ('PLACEHOLDER' if a.placeholder else 'SPEC', a.pages, a.paper, S['spine_in'], S['cover_w_in'], S['cover_h_in'], W, H, 'spine text allowed' if S['spine_text_allowed'] else 'NO spine text (<=79 pages)')
    cv2.putText(G, lab, (b + 20, H - b - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.25, (255, 255, 255), 3, cv2.LINE_AA)
    save_rgb(os.path.join(a.out, 'RaThor_Issue01_KDPwrap_%s_guides.jpg' % tag), G.astype(np.float32), 90)
    pv = cv2.resize(G, (W * 620 // H, 620), interpolation=cv2.INTER_AREA); save_rgb(os.path.join(a.out, 'RaThor_Issue01_KDPwrap_%s_guides_620.jpg' % tag), pv.astype(np.float32), 90)
    S.update(spine_px=SP1 - SP0, spine_safe_px=[SP0 + sm_px, SP1 - sm_px], spine_text=a.spine_text or None, barcode_zone_px=zone,
             range_24_32=[dict(pages=p, spine_in=round(p * PER_PAGE[a.paper], 6), cover_w_in=round(2 * BLEED_IN + 2 * TRIM_W + p * PER_PAGE[a.paper], 6),
                               px_w=round((2 * BLEED_IN + 2 * TRIM_W + p * PER_PAGE[a.paper]) * DPI)) for p in range(24, 34, 2)],
             outputs=sorted(os.listdir(a.out)))
    json.dump(S, open(os.path.join(a.out, 'spec_%s.json' % tag), 'w'), indent=1); print(json.dumps(S, indent=1))

if __name__ == '__main__': main()
