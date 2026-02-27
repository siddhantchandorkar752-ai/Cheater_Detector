# 🕵️‍♂️ Cheater_Detector: AI-Powered Exam Surveillance System

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange.svg)
![OpenVINO](https://img.shields.io/badge/Intel-OpenVINO-blueviolet.svg)

## 📌 Project Overview
**Cheater_Detector** is a real-time, AI-driven computer vision pipeline designed to automate exam hall surveillance. Built primarily for CPU-constrained environments (like Intel Core i3), this engine leverages hardware acceleration to track student behavior, gaze direction, and posture to flag suspicious activities without requiring heavy GPU clusters.

## 🚀 Core Architecture & Features
* **Blazing Fast Pose Estimation:** Utilizes **YOLOv8 Nano Pose**, dynamically optimized with **Intel OpenVINO** for maximum CPU frame rates.
* **Trigonometry-Based Gaze Tracking:** Calculates the spatial distance ratio between facial keypoints (Nose to Left/Right Ears) to accurately determine Head Yaw (Looking Left/Right).
* **Temporal Suspicion Scoring Engine:** Eliminates false positives by implementing a continuous time-threshold logic (triggers a Red Alert only if anomalous behavior exceeds a continuous 3-second window).
* **Automated Audit Logging:** Seamlessly logs chronological suspicious events into a `cheating_logs.csv` database for post-exam review.

## 🧠 The Mathematics (Heuristic Logic)
Instead of running heavy secondary neural networks for gaze classification, the system uses localized trigonometric ratios:
- `Distance Ratio = (Distance from Nose to Left Ear) / (Distance from Nose to Right Ear)`
- **Looking Right:** Ratio > 2.5
- **Looking Left:** Ratio < 0.4

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/siddhantchandorkar752-ai/Cheater_Detector.git](https://github.com/siddhantchandorkar752-ai/Cheater_Detector.git)
   cd Cheater_Detector
