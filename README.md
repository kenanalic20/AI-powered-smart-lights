# AI Powered Smart Lights

Automated LED control system using Python Flask, MediaPipe, and ESP32 microcontroller.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Introduction

This project implements an AI-powered smart lights system that uses hand gestures to control LED lights. The system comprises a Python Flask server for hand gesture recognition using MediaPipe and an ESP32 microcontroller for LED control.

## Features

- Real-time hand gesture recognition.
- LED lights controlled based on the number of detected fingers.
- Seamless integration of Python and ESP32 for efficient IoT applications.

## Hardware Requirements

- ESP32 development board.
- Webcam for hand gesture recognition.
- LED diode (5x) (addressable or standard).
- Power supply.
- Connecting wires, breadboard, etc.

## Setup

1. **Connect Hardware:**
   - Connect the ESP32, webcam, and LED lights according to the hardware setup guidelines.

2. **Install Dependencies:**
   - Ensure that the required Python libraries (Flask, OpenCV, MediaPipe) are installed for the server and the ESP32 libraries are installed in the Arduino IDE.

3. **Upload Code:**
   - Upload the provided Python and Arduino sketches to your server and ESP32, respectively.

## Usage

- Start the Python Flask server.
- Open the provided URL in your browser to view the real-time webcam feed with hand gesture overlays.
- The LED lights will respond to your hand gestures, adjusting based on the number of detected fingers.


## Customization

- Adjust hand gesture recognition parameters and LED control logic in the Python and Arduino code based on your preferences.

## Troubleshooting

- **LEDs Not Responding:**
  - Ensure that the ESP32 is connected to the server.
  - Check for any errors in the server logs and Arduino Serial Monitor.
  
## License

This project is licensed under the [MIT License](LICENSE).
