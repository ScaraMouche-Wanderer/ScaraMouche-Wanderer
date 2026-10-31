<p align="center">
  <img src="./assets/hero.svg" width="100%" alt="Prathmesh Narwaria — hardware roots, software reach. Embedded systems, Linux tools, and computer vision." />
</p>

<p align="center">
  <a href="#selected-builds">Selected builds</a> &nbsp; / &nbsp;
  <a href="./PROJECTS.md">Project index</a> &nbsp; / &nbsp;
  <a href="#engineering-toolkit">Toolkit</a>
</p>

I'm **Prathmesh Narwaria**, also known as **ScaraMouche**. I build across the boundary between hardware and software: ESP32 firmware, Linux desktop tools, and local computer vision.

My projects connect low-level behavior to interfaces you can inspect, test, and demonstrate.

## Selected builds

### 01 / ESP32 IoT Firewall
<a href="https://github.com/ScaraMouche-Wanderer/Iot-Firewall-main">
  <img src="./assets/iot-firewall.svg" width="100%" alt="ESP32 IoT Firewall — wireless observations, threat detection, and an operator dashboard. C++, ESP32, FreeRTOS, PlatformIO." />
</a>

An ESP32 wireless intrusion detection project with a packet-processing pipeline, rule-based detectors, alert lifecycles, and a Web Serial dashboard.

**Engineering focus:** queue-based processing, bounded device tracking, native host tests, and a laptop demo with explicitly simulated telemetry.

[Source](https://github.com/ScaraMouche-Wanderer/Iot-Firewall-main) · [Project brief](https://github.com/ScaraMouche-Wanderer/Iot-Firewall-main/blob/main/PROJECT_BRIEF.md) · [Run the demo](https://github.com/ScaraMouche-Wanderer/Iot-Firewall-main/blob/main/docs/PRESENTATION.md) · [Tests & firmware CI](https://github.com/ScaraMouche-Wanderer/Iot-Firewall-main/actions)

### 02 / FaceGATE Linux
<a href="https://github.com/ScaraMouche-Wanderer/FaceGATE-Linux">
  <img src="./assets/facegate.svg" width="100%" alt="FaceGATE Linux — local face recognition and application access control. Python, PySide6, OpenCV, InsightFace, ONNX Runtime." />
</a>

A Linux application locker that combines local face recognition, an encrypted profile vault, a password fallback, and a native desktop interface.

**Engineering focus:** process monitoring, authentication state, encrypted storage, and a documented threat model for a user-level daemon.

[Source](https://github.com/ScaraMouche-Wanderer/FaceGATE-Linux) · [Project brief](https://github.com/ScaraMouche-Wanderer/FaceGATE-Linux/blob/master/PROJECT_BRIEF.md) · [User guide](https://github.com/ScaraMouche-Wanderer/FaceGATE-Linux/blob/master/GUIDE.md) · [Security model](https://github.com/ScaraMouche-Wanderer/FaceGATE-Linux/blob/master/SECURITY.md)

<details>
<summary>See the desktop interface</summary>
<br />
<img src="https://raw.githubusercontent.com/ScaraMouche-Wanderer/FaceGATE-Linux/master/assets/screenshots/locked-apps.png" width="850" alt="FaceGATE application settings and protected application list" />
</details>

### 03 / CodeWriter
<a href="https://github.com/ScaraMouche-Wanderer/CodeWriter">
  <img src="./assets/codewriter.svg" width="100%" alt="CodeWriter — native Linux code editing, formatting, typing playback, and input automation. Python, GTK4, GtkSourceView, ydotool." />
</a>

A native Linux utility for staging and formatting code, previewing typing playback, and automating input in your own desktop workflows.

**Engineering focus:** GTK event handling, controllable background typing, Wayland/X11 integration, and reusable text-processing tools.

[Source](https://github.com/ScaraMouche-Wanderer/CodeWriter) · [Project brief](https://github.com/ScaraMouche-Wanderer/CodeWriter/blob/main/PROJECT_BRIEF.md) · [User guide](https://github.com/ScaraMouche-Wanderer/CodeWriter/blob/main/USER_GUIDE.md) · [Test suite](https://github.com/ScaraMouche-Wanderer/CodeWriter/tree/main/tests)

<details>
<summary>See the editor and playback demo</summary>
<br />
<img src="https://raw.githubusercontent.com/ScaraMouche-Wanderer/CodeWriter/main/docs/assets/codewriter_demo.gif" width="850" alt="CodeWriter editor and typing playback demonstration" />
</details>

## Engineering toolkit

| Area | Tools used in my projects |
| :--- | :--- |
| Embedded & wireless | C / C++, ESP32, FreeRTOS, PlatformIO, Arduino, IEEE 802.11 |
| Linux & desktop | Python, GTK4, PySide6, systemd user services, Bash |
| Computer vision | OpenCV, InsightFace, ONNX Runtime |
| Testing & delivery | pytest, unittest, native C++ tests, Git, GitHub Actions |

## How I approach a build

- **Trace the whole path.** Follow an input from the hardware or operating system through processing, storage, and the interface.
- **Make it demonstrable.** Provide a repeatable demo, setup instructions, and code a reviewer can navigate.
- **Explain the boundary.** Separate simulations from hardware results and document the limitations behind security claims.

More repositories, the earlier IoT implementation, and upstream projects I explore are organized in the **[project index](./PROJECTS.md)**.

<p align="center"><sub>From packets and processes to a working interface.</sub></p>

