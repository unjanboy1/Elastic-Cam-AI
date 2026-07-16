# Elastic Cam AI

Elastic Cam AI is an advanced, high-performance computer vision application designed to simulate skin elasticity and deformation in real time. By leveraging state-of-the-art AI-based facial and body landmark tracking, the system continuously analyzes skin surfaces from a live webcam feed. Users can interactively select, pinch, stretch, and manipulate target skin regions while a dynamic image-warping pipeline renders physically plausible elastic movement.

This project sits at the intersection of artificial intelligence, real-time computer vision, and digital geometry processing, serving as a robust foundation for interactive visual effects, clinical simulation, and academic research.

---

## 🌟 Key Features

* **Real-Time High-Fidelity Tracking:** Utilizes deep-learning models to track facial and somatic landmarks with millisecond-level inference speeds.
* **Interactive Mesh-Free Deformation:** Implements smooth geometric deformation fields controlled via mouse clicks, drags, or custom-mapped gesture coordinates.
* **Dynamic Image Warping:** Employs advanced spatial transformation algorithms to translate mathematical stretching vectors into visually seamless pixel remapping.
* **Intelligent Motion Compensation:** Features dynamic anchor-point tracking, allowing the warped effect to move naturally and stay pinned even when the user moves their head or body.
* **Low-Latency Architecture:** Highly optimized asynchronous capture and rendering pipeline designed to run smoothly at $30+$ FPS on consumer-grade CPUs.
* **Visual Debugging Mode:** Toggleable overlays showing active landmark points, vector displacement lines, and bounding boxes for real-time visualization of the system's underlying mathematics.

---

## 🛠 Tech Stack & Core Libraries

The application is written entirely in Python, utilizing standard, industry-proven libraries for maximum speed, compatibility, and ease of deployment:

* **Python:** Used for application logic, state estimation, and coordinating frame-by-frame processing.
* **OpenCV (Open Source Computer Vision Library):** Handles hardware-level webcam capture, pixel-matrix transformations, frame rendering, and interactive UI windows.
* **Google MediaPipe:** Powers the AI-based facial mesh and landmark localization, offering robust spatial tracking under varying lighting conditions.
* **NumPy:** Conducts high-speed vector math, distance-field calculations, and matrix-level coordinate mapping.

---

## ⚙️ How It Works: Under the Hood

The application relies on a fast, multi-stage processing loop that updates on every frame. Below is a detailed breakdown of the system pipeline.


# Elastic Cam AI

## 📌 Project Description

**Elastic Cam AI** is a real-time computer vision application that simulates skin elasticity using AI-based landmark detection. The system detects key points on a person's skin from a live camera feed and allows users to interact with the detected region by pinching and stretching it naturally.

Using advanced image processing and AI landmark tracking, the application continuously follows the selected skin area and deforms it in real time, creating a smooth and realistic stretching effect. This project demonstrates the integration of computer vision, facial/body landmark detection, and image warping techniques for interactive visual manipulation.

---

## ✨ Features

* Real-time webcam capture
* AI-based skin landmark detection
* Interactive pinch and stretch functionality
* Dynamic image warping
* Smooth tracking of skin movement
* Low-latency real-time processing
* User-friendly interface
* Accurate landmark localization

---

## 🛠 Technologies Used

* Python
* OpenCV
* MediaPipe (Landmark Detection)
* NumPy
* AI-based Image Processing
* Computer Vision Techniques


## ▶️ How It Works

1. The webcam captures the user's live image.
2. AI detects skin landmarks in real time.
3. The user selects a region using pinch gestures or mouse interaction.
4. The selected skin area is stretched or compressed using image warping algorithms.
5. The deformation updates continuously while maintaining smooth visual quality.

---

## 📌 Applications

* Augmented Reality (AR)
* Medical and Dermatology Visualization
* AI and Computer Vision Research
* Interactive Image Editing
* Educational Demonstrations
* Entertainment and Visual Effects

---

## 🔮 Future Improvements

* Multi-touch gesture support
* More realistic physics-based skin deformation
* GPU acceleration
* Mobile application support
* 3D skin deformation
* AI-enhanced elasticity simulation
