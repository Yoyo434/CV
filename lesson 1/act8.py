import cv2
import numpy as np
from vcam import vcam, meshGen
def build_maps(height, width):
    camera = vcam(H=height, W=width)
    plane = meshGen(height, width)
    plane.Z += 20 * np.exp(-0.5 * ((plane.X / plane.W) / 0.1) ** 2) / (0.1 * np.sqrt(2 * np.pi))
    points_3d = plane.getPlane()
    points_2d = camera.project(points_3d)
    return camera.getMaps(points_2d)

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    raise RuntimeError("Could not open webcam.")
map_x = None
map_y = None
frame_size = None

while True:
    success, frame = capture.read()
    if not success:
        break
    height, width = frame.shape[:2]    
    current_size = (height, width)
    if frame_size != current_size:
        map_x, map_y = build_maps(height, width)
    frame_size = current_size
    output = cv2.remap(frame, map_x, map_y, interpolation=cv2.INTER_LINEAR)
    combined = np.hstack((frame, output))
    cv2.imshow("Original and Runny Mirror", combined)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
capture.release()
cv2.destroyAllWindows()