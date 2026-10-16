# ISSUE01-KDP-WRAP-1: FLAGGED FALLBACK ONLY (council ruling, Wild 2026-10-15 11:01 PM ET). Not the upload: the upload is the flattened RGB PDF.
# Made because the GRACoL 2013 (CRPC6) soft proof shows the obsidian blacks lifting ~10 L* when black ink is simulated (see softproof JSON).
# usage: python3 cmyk_fallback.py WRAP.jpg OUT.pdf --w-in W --h-in H [--profile icc/GRACoL2013_CRPC6.icc]
# sRGB -> CMYK (CRPC6, relative colorimetric + black-point compensation, profile TAC 320%), one page, DeviceCMYK, Flate + PNG predictor,
# MediaBox at the exact KDP size, no ICC embedded (KDP strips profiles), no marks.
import argparse, os, zlib, numpy as np
from PIL import Image, ImageCms
HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(); ap.add_argument('wrap'); ap.add_argument('out'); ap.add_argument('--w-in', type=float, required=True); ap.add_argument('--h-in', type=float, required=True)
ap.add_argument('--profile', default=os.path.join(HERE, 'icc/GRACoL2013_CRPC6.icc')); a = ap.parse_args()
src = Image.open(a.wrap).convert('RGB')
cmyk = ImageCms.applyTransform(src, ImageCms.buildTransform(ImageCms.createProfile('sRGB'), ImageCms.getOpenProfile(a.profile), 'RGB', 'CMYK',
                               ImageCms.Intent.RELATIVE_COLORIMETRIC, flags=ImageCms.Flags.BLACKPOINTCOMPENSATION))
C = np.asarray(cmyk, np.uint8); h, w, _ = C.shape
print('TAC max %.1f%%' % (C.astype(np.float32).sum(2).max() * 100 / 255))
# PNG 'Up' predictor (type 2) per row, then Flate
up = C.reshape(h, w * 4).astype(np.int16); diff = np.vstack([up[:1], up[1:] - up[:-1]]) % 256
raw = np.hstack([np.full((h, 1), 2, np.uint8), diff.astype(np.uint8)]).tobytes(); data = zlib.compress(raw, 9)
W, H = a.w_in * 72, a.h_in * 72; content = b'q %.4f 0 0 %.4f 0 0 cm /Im0 Do Q' % (W, H)
objs = [b'<< /Type /Catalog /Pages 2 0 R >>', b'<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
        b'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 %.4f %.4f] /TrimBox [0 0 %.4f %.4f] /Resources << /XObject << /Im0 4 0 R >> >> /Contents 5 0 R >>' % (W, H, W, H),
        b'<< /Type /XObject /Subtype /Image /Width %d /Height %d /ColorSpace /DeviceCMYK /BitsPerComponent 8 /Filter /FlateDecode /DecodeParms << /Predictor 12 /Colors 4 /Columns %d /BitsPerComponent 8 >> /Length %d >>\nstream\n' % (w, h, w, len(data)) + data + b'\nendstream',
        b'<< /Length %d >>\nstream\n' % len(content) + content + b'\nendstream',
        b'<< /Title (Ra-Thor Living Thunder #1 - KDP cover - FLAGGED CMYK FALLBACK, GRACoL 2013 CRPC6 - not the upload) /Producer (cmyk_fallback.py) >>']
out = b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n'; offs = []
for i, o in enumerate(objs, 1): offs.append(len(out)); out += b'%d 0 obj\n' % i + o + b'\nendobj\n'
x = len(out); out += b'xref\n0 %d\n0000000000 65535 f \n' % (len(objs) + 1) + b''.join(b'%010d 00000 n \n' % o for o in offs)
out += b'trailer\n<< /Size %d /Root 1 0 R /Info 6 0 R >>\nstartxref\n%d\n%%%%EOF\n' % (len(objs) + 1, x)
open(a.out, 'wb').write(out); print(a.out, '%.1f MB' % (len(out) / 1e6))
