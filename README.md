# Elastic Cam AI

Elastic Cam AI is a high-performance, real-time computer vision application that simulates skin elasticity using AI-based landmark detection. By tracking key facial and body landmarks from a live camera feed, the system allows users to interactively pinch, pull, and deform specific skin regions. The application utilizes advanced coordinate mapping and image warping algorithms to deliver a highly responsive, physically plausible, and visually smooth deformation effect in real time.

---

## Key Features

* **Real-Time Landmark Tracking:** High-fidelity, low-latency tracking of facial and body skin landmarks.
* **Interactive Mesh Deformation:** Intuitive pinch-and-stretch interactions via mouse control or coordinate-based inputs.
* **Dynamic Image Warping:** Seamless real-time rendering of skin elasticity using advanced mathematical warping techniques.
* **Robust Motion Compensation:** Algorithms continuously track and adjust the deformed mesh even as the subject moves or rotates in front of the camera.
* **Highly Optimized Pipeline:** Designed with a focus on low latency and high frame rates (FPS) for a lag-free user experience.
* **User-Friendly Interface:** Minimalist and intuitive runtime window displaying both the original tracking overlay and the warped output.

---

## Technical Architecture

The application operates on a continuous, closed-loop processing pipeline designed to handle high-frequency video frames without bottle-necking the CPU.

### System Pipeline