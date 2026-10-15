# 4x AI upscale with spandrel (tiled, overlap-blended), CPU
import sys, torch, numpy as np, cv2, spandrel, time
model_path, src, dst = sys.argv[1:4]
torch.set_num_threads(8)
m = spandrel.ModelLoader().load_from_file(model_path).eval()
S = m.scale
img = cv2.imread(src)[:, :, ::-1].astype(np.float32) / 255
H, W = img.shape[:2]; T = 192; OV = 16
out = np.zeros((H*S, W*S, 3), np.float32); wsum = np.zeros((H*S, W*S, 1), np.float32)
t0 = time.time()
for y in range(0, H, T-2*OV):
    for x in range(0, W, T-2*OV):
        y0, x0 = max(0, min(y, H-T)), max(0, min(x, W-T)); y1, x1 = min(H, y0+T), min(W, x0+T)
        tile = torch.from_numpy(img[y0:y1, x0:x1].transpose(2, 0, 1).copy())[None]
        with torch.no_grad(): r = m(tile)[0].clamp(0, 1).numpy().transpose(1, 2, 0)
        h, w = r.shape[:2]
        wy = np.minimum(np.arange(h)+1, h-np.arange(h)).astype(np.float32); wx = np.minimum(np.arange(w)+1, w-np.arange(w)).astype(np.float32)
        wt = np.minimum(np.minimum.outer(wy, wx), OV*S)[..., None]
        out[y0*S:y0*S+h, x0*S:x0*S+w] += r*wt; wsum[y0*S:y0*S+h, x0*S:x0*S+w] += wt
        if x1 >= W and x+T-2*OV >= W: pass
    print('row', y, '%.0fs' % (time.time()-t0), flush=True)
out /= np.maximum(wsum, 1e-6)
cv2.imwrite(dst, (out[:, :, ::-1]*255+0.5).clip(0, 255).astype(np.uint8))
print('done', out.shape, '%.0fs' % (time.time()-t0))
