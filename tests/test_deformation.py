import cv2
import numpy as np

from deformation.stretch_engine import StretchEngine
from deformation.image_warp import ImageWarp
from deformation.rubber_physics import RubberPhysics
from ui.overlays import Overlays
from ui.effects import Effects

# Initialize modules
stretch = StretchEngine(strength=0.6)
warp = ImageWarp()
physics = RubberPhysics()
overlay = Overlays()
effects = Effects()

# Dummy image
frame = np.zeros((480, 640, 3), dtype=np.uint8)

# Fake points (like hand landmarks)
points = [(100, 100), (200, 150), (300, 200), (400, 250)]
anchor = (150, 150)

# Apply stretch
stretched = stretch.apply_stretch(frame, points, anchor)

print("Original Points:", points)
print("Stretched Points:", stretched)

# Draw points for visualization
for x, y in stretched:
    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

# UI overlay test
frame = overlay.draw_text(frame, "Deformation Test Mode")

# Show result
cv2.imshow("Test Deformation", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()