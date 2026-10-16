# Back-projection: keep the AI upscale's detail but force its 1x downscale to match the source (no tone shift,
# no invented low-frequency changes). Usage: consistency.py up.png src_1x.png out.png
import cv2, numpy as np, sys
U=cv2.imread(sys.argv[1]).astype(np.float32); N=cv2.imread(sys.argv[2]).astype(np.float32)
h,w=N.shape[:2]; S=U.shape[1]//w
for it in range(3):
    R=N-cv2.resize(U,(w,h),interpolation=cv2.INTER_AREA)
    U=U+cv2.GaussianBlur(cv2.resize(R,(w*S,h*S),interpolation=cv2.INTER_CUBIC),(0,0),S*0.35)
    print('iter',it,'MAE vs source after downscale %.2f'%np.abs(N-cv2.resize(np.clip(U,0,255),(w,h),interpolation=cv2.INTER_AREA)).mean())
cv2.imwrite(sys.argv[3],np.clip(U+0.5,0,255).astype(np.uint8))
