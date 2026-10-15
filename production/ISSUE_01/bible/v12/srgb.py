# Every delivered PNG/JPG is sRGB-tagged RGB. No CMYK conversion.
import numpy as np
from PIL import Image, ImageCms

_ICC = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()


def save(path, rgb, dpi=None, quality=95):
    """rgb: uint8 HxWx3 RGB."""
    im = Image.fromarray(np.asarray(rgb), mode="RGB")
    kw = {"icc_profile": _ICC}
    if dpi:
        kw["dpi"] = (dpi, dpi)
    if path.lower().endswith((".jpg", ".jpeg")):
        kw.update(quality=quality, subsampling=0)
    im.save(path, **kw)


def icc_bytes():
    return _ICC
