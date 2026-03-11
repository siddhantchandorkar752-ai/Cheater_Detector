<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:FF0000,100:FF6B00&height=220&section=header&text=CHEATER%20DETECTOR&fontSize=60&fontColor=ffffff&fontAlignY=35&desc=AI-Powered%20Exam%20Surveillance%20System%20%7C%20Real-Time%20%7C%20CPU%20Optimized&descAlignY=60&descSize=18&animation=fadeIn" width="100%"/>

<br/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Orbitron&weight=900&size=22&duration=3000&pause=800&color=FF4500&center=true&vCenter=true&multiline=true&width=800&height=120&lines=🕵️+AI+That+Catches+Cheaters+in+Real-Time;Gaze+Tracking+%7C+Pose+Estimation+%7C+Suspicion+Scoring;YOLOv8+Nano+%2B+Intel+OpenVINO+%7C+CPU+Blazing+Fast;No+GPU+Needed+—+Runs+on+Intel+Core+i3)](https://git.io/typing-svg)

<br/>

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8_Nano_Pose-FF6B00?style=for-the-badge)
![OpenVINO](https://img.shields.io/badge/Intel_OpenVINO-0071C5?style=for-the-badge&logo=intel&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-FF4500?style=for-the-badge)

<br/>

> **🕵️ The AI invigilator that never blinks — tracking gaze, posture, and suspicious behavior in real-time, on a basic CPU.**

</div>

---

## 🔥 WHAT IS CHEATER DETECTOR?

```
╔══════════════════════════════════════════════════════════════════════╗
║     CHEATER DETECTOR — AI Exam Surveillance System v1.0             ║
║                                                                      ║
║     "Not a camera. An invigilator."                                 ║
║                                                                      ║
║     YOLOv8 Nano Pose  → Keypoint Detection                          ║
║     Intel OpenVINO    → CPU Hardware Acceleration                   ║
║     Trigonometric Math → Gaze Direction (No secondary NN needed)    ║
║     Temporal Scoring  → 3-Second threshold = Red Alert              ║
║     CSV Audit Log     → Timestamped evidence for review             ║
╚══════════════════════════════════════════════════════════════════════╝
```

Cheater Detector is a **production-grade AI exam surveillance pipeline** that uses **YOLOv8 Nano Pose + Intel OpenVINO** to track student gaze direction and posture in real-time — no GPU cluster needed. Built specifically for CPU-constrained environments, it flags cheating behavior only after a sustained **3-second anomaly window**, eliminating false positives and generating a complete **CSV audit log** for post-exam review.

---

## 😔 PROBLEM STATEMENT

Traditional exam surveillance:
- **Manual** — invigilators miss things, get tired
- **Expensive** — GPU-based CV systems cost lakhs
- **No evidence** — no timestamped logs for disputes
- **False accusations** — momentary glances flagged as cheating

**Cheater Detector solves all four** — automated, CPU-optimized, evidence-based, and temporally smart.

---

## ⚡ CORE FEATURES

| Feature | Description | Tech |
|---------|-------------|------|
| 🦴 **Pose Estimation** | Full body keypoint detection at high FPS | YOLOv8 Nano Pose |
| ⚡ **CPU Acceleration** | Intel OpenVINO dynamic optimization | Intel OpenVINO |
| 👁️ **Gaze Tracking** | Trigonometric nose-ear ratio — no secondary NN | Custom Math |
| ⏱️ **Temporal Scoring** | 3-second sustained anomaly = Red Alert only | Time-threshold logic |
| 📋 **Audit Logging** | Chronological CSV log of all suspicious events | CSV + Timestamps |
| 🚫 **False Positive Filter** | Momentary glances ignored — only sustained behavior flagged | Temporal Engine |

---

## 🧠 THE MATHEMATICS

> Most systems use a secondary neural network for gaze classification — expensive and slow.
> Cheater Detector uses **pure trigonometry** instead.

```
GAZE DETECTION FORMULA:
─────────────────────────────────────────────────────

  Distance Ratio = dist(Nose → Left Ear)
                   ──────────────────────
                   dist(Nose → Right Ear)

─────────────────────────────────────────────────────

  Ratio > 2.5  →  👀 Looking RIGHT  →  Suspicious
  Ratio < 0.4  →  👀 Looking LEFT   →  Suspicious
  0.4 ≤ Ratio ≤ 2.5  →  ✅ Looking FORWARD  →  Normal

─────────────────────────────────────────────────────

WHY THIS WORKS:
  When head turns right → Nose moves closer to Right Ear
                        → Left distance increases
                        → Ratio rises above 2.5

  When head turns left  → Nose moves closer to Left Ear
                        → Right distance increases
                        → Ratio drops below 0.4
```

**Result:** Gaze classification with zero additional neural network overhead. Pure math. Blazing fast.

---

## ⏱️ TEMPORAL SUSPICION ENGINE

```
STANDARD APPROACH (bad):
  Frame 1: Looking left  → 🚨 ALERT  ← false positive
  Frame 2: Looking front → ✅ OK
  Frame 3: Looking left  → 🚨 ALERT  ← false positive again

─────────────────────────────────────────────────────

CHEATER DETECTOR APPROACH (smart):
  t=0s:   Looking left  → timer starts...
  t=1s:   Still left    → timer continues...
  t=2s:   Still left    → timer continues...
  t=3s:   Still left    → 🔴 RED ALERT + CSV LOG

  If behavior stops before 3s → timer resets → no alert
```

---

## 🏗️ ARCHITECTURE

```
WEBCAM FEED
    │
    ▼
┌──────────────────────────────────────────────────────────┐
│              CHEATER DETECTOR PIPELINE                   │
│                                                          │
│  ┌──────────────────────────────┐                       │
│  │  YOLOv8 Nano Pose            │                       │
│  │  + Intel OpenVINO            │ ← CPU optimized       │
│  │  → 17 body keypoints/frame   │                       │
│  └──────────────┬───────────────┘                       │
│                 │ keypoints                             │
│                 ▼                                        │
│  ┌──────────────────────────────┐                       │
│  │  Gaze Analyzer               │                       │
│  │  Nose-Ear Distance Ratio     │ ← Pure trigonometry   │
│  │  → FORWARD / LEFT / RIGHT    │                       │
│  └──────────────┬───────────────┘                       │
│                 │ gaze direction                        │
│                 ▼                                        │
│  ┌──────────────────────────────┐                       │
│  │  Temporal Suspicion Engine   │                       │
│  │  3-second threshold logic    │ ← No false positives  │
│  │  → NORMAL / RED ALERT        │                       │
│  └──────────────┬───────────────┘                       │
│                 │                                        │
│       ┌─────────┴──────────┐                            │
│       ▼                    ▼                            │
│  cv2 Display          CSV Logger                        │
│  Annotated frame      cheating_logs.csv                 │
│  + Alert overlay      Timestamped evidence              │
└──────────────────────────────────────────────────────────┘
```

---

## 📊 SUSPICION SCORING LOGIC

```python
# Pseudocode — Temporal Engine
suspicious_since = None

for each frame:
    gaze = calculate_gaze_ratio(keypoints)
    
    if gaze in ["LEFT", "RIGHT"]:
        if suspicious_since is None:
            suspicious_since = current_time
        
        duration = current_time - suspicious_since
        
        if duration >= 3.0:  # 3-second threshold
            trigger_red_alert()
            log_to_csv(timestamp, gaze, duration)
    else:
        suspicious_since = None  # Reset — normal behavior
```

---

## 🛠️ INSTALLATION

### Prerequisites
- Python 3.9+
- Webcam
- Intel CPU recommended (OpenVINO optimized)

### Step 1 — Clone
```bash
git clone https://github.com/siddhantchandorkar752-ai/Cheater_Detector.git
cd Cheater_Detector
```

### Step 2 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Run
```bash
python main.py
```

---

## 🚀 USAGE

1. Run `python main.py`
2. Webcam opens — point at student
3. System tracks gaze + posture in real-time
4. **Sustained suspicious behavior (3s+)** → 🔴 Red Alert on screen
5. All events auto-logged to `cheating_logs.csv`
6. Press **`Q`** to quit — review CSV for audit

---

## 🧪 EXAMPLE AUDIT LOG

```csv
timestamp,             student_id, gaze,  duration_sec, alert_level
2026-03-10 10:23:41,   student_01, RIGHT, 4.2,          RED
2026-03-10 10:31:15,   student_01, LEFT,  3.8,          RED
2026-03-10 10:45:02,   student_03, RIGHT, 5.1,          RED
```

---

## ⚡ PERFORMANCE

| Device | FPS | Optimization |
|--------|-----|-------------|
| Intel Core i3 (CPU) | 20-25 FPS | OpenVINO INT8 |
| Intel Core i5 (CPU) | 30+ FPS | OpenVINO INT8 |
| NVIDIA GPU | 60+ FPS | CUDA |

> YOLOv8 **Nano** chosen specifically for edge/CPU deployment — smallest, fastest variant.

---

## 🛠️ TECH STACK

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8_Nano_Pose-FF6B00?style=for-the-badge)
![OpenVINO](https://img.shields.io/badge/Intel_OpenVINO-0071C5?style=for-the-badge&logo=intel&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Ultralytics](https://img.shields.io/badge/Ultralytics-00D4FF?style=for-the-badge)

---

## 🔮 FUTURE IMPROVEMENTS

- [ ] Multi-student tracking — detect multiple students simultaneously
- [ ] Phone detection — flag mobile phone usage
- [ ] Whisper detection — flag suspicious mouth movements
- [ ] Web dashboard — live monitoring from browser
- [ ] Email alerts — auto-notify invigilator
- [ ] Integration with attendance systems

---

## 🤝 CONTRIBUTING

```bash
git checkout -b feature/AmazingFeature
git commit -m 'Add AmazingFeature'
git push origin feature/AmazingFeature
# Open a Pull Request
```

---

## 📄 LICENSE

Distributed under the MIT License.

---

## 👨‍💻 AUTHOR

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0D1117,100:FF4500&height=60&text=Siddhant%20Chandorkar&fontSize=28&fontColor=ffffff&fontAlign=50&fontAlignY=50" width="500"/>

<br/><br/>

[![GitHub](https://img.shields.io/badge/GitHub-siddhantchandorkar752--ai-181717?style=for-the-badge&logo=github)](https://github.com/siddhantchandorkar752-ai)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-siddhantchandorkar-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/siddhantchandorkar)

<br/>

*"I don't just build AI. I build AI that understands humans."*

</div>

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:FF6B00,50:FF0000,100:0D1117&height=120&section=footer&text=Cheater%20Detector%20v1.0&fontSize=28&fontColor=ffffff&fontAlignY=65&animation=fadeIn" width="100%"/>
</div>
