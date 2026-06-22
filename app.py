import cv2
import numpy as np

from tracking.hand_tracker import HandTracker
from ui.overlays import Overlays

# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize modules
tracker = HandTracker()
overlay = Overlays()

# Engine state configuration matching the repository's physics layout
anchor_pt = None
stretching_active = False

# Hysteresis parameters to ensure the pinch mechanics don't flicker or jitter
PINCH_ENGAGE_DIST = 36   
PINCH_RELEASE_DIST = 55  
EFFECT_RADIUS = 90      # Control size for the localized deformation mask

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Natural camera mirror inversion
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    
    # Pristine array structure for calculations
    deformed_frame = frame.copy()

    # Process hand coordinate landmarks
    hands = tracker.find_hands(frame)

    if hands:
        lmList = hands[0]
        # Index finger tip vector boundary terminal (ID 8)
        x, y = int(lmList[8][1]), int(lmList[8][2])
        # Thumb tracking node terminal (ID 4)
        tx, ty = int(lmList[4][1]), int(lmList[4][2])
        
        # Real-time pinch vector distance tracking
        pinch_dist = np.sqrt((x - tx)**2 + (y - ty)**2)

        # Dynamic Hysteresis State Machine
        if not stretching_active and pinch_dist < PINCH_ENGAGE_DIST:
            anchor_pt = (x, y)
            stretching_active = True
        elif stretching_active and pinch_dist > PINCH_RELEASE_DIST:
            stretching_active = False
            anchor_pt = None

        # Execute Smooth Vector Field Spline Deformation
        if stretching_active and anchor_pt is not None:
            ax, ay = anchor_pt
            
            # Displacement pull calculation vectors
            dx, dy = x - ax, y - ay
            pull_len = np.sqrt(dx**2 + dy**2)

            if pull_len > 0:
                # Initialize structured coordinate mapping matrices
                map_x, map_y = np.meshgrid(np.arange(w), np.arange(h))
                map_x = map_x.astype(np.float32)
                map_y = map_y.astype(np.float32)

                # Distance metrics from structural tissue grid to anchor point
                dist_x = map_x - ax
                dist_y = map_y - ay
                grid_dist = np.sqrt(dist_x**2 + dist_y**2)

                # Volume conservation curve: Thinner as it stretches out
                thickness_taper = 1.0 / (1.0 + (pull_len / EFFECT_RADIUS) * 0.4)

                # Vector directional normalization
                ux = dx / pull_len
                uy = dy / pull_len

                # Project mesh mapping vertices onto the main deformation path axis
                proj = dist_x * ux + dist_y * uy
                perp = np.abs(-dist_x * uy + dist_y * ux)

                # Construct an organic Gaussian envelope constraint mask
                # This tapers the edges beautifully so your face features don't rip or clip
                gaussian_envelope = np.exp(- (perp**2) / (2 * ((EFFECT_RADIUS * thickness_taper)**2)))

                # Length-wise influence bounds
                length_envelope = np.where(
                    proj < 0,
                    np.exp(- (proj**2) / (2 * (EFFECT_RADIUS**2))),
                    np.where(proj > pull_len, np.exp(- ((proj - pull_len)**2) / (2 * (EFFECT_RADIUS**2))), 1.0)
                )

                # Combine mesh interpolation constraint weights
                total_weight = gaussian_envelope * length_envelope

                # Calculate smooth interpolation displacement shift factor along the vector field
                t = np.clip(proj / pull_len, 0, 1) if pull_len > 0 else 0
                
                # Deform coordinate map grid vertices smoothly matching the vector path
                map_x -= dx * t * total_weight
                map_y -= dy * t * total_weight

                # Remap physical image array channel pixels according to the calculated transformation
                deformed_frame = cv2.remap(frame, map_x, map_y, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)

            # Draw clean, stylized tracking dots
            cv2.circle(deformed_frame, anchor_pt, 5, (0, 0, 255), -1)   # Fixed origin point
            cv2.circle(deformed_frame, (x, y), 6, (0, 255, 0), -1)       # Live pinch point
        else:
            cv2.circle(deformed_frame, (x, y), 6, (255, 0, 0), -1)       # Idle tracker position

    # Render clean Text UI Hud layout overlay
    overlay.draw_text(deformed_frame, "GUM-GUM STRETCH ACTIVE", (20, 40))

    # Output application frame view
    cv2.imshow("ElasticCam AI", deformed_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()