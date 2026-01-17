# 🎤 Voice-Controlled AI Agent for Mobile Automation

## 🚀 Overview
This project presents a voice-controlled AI agent that understands natural language commands and automates actions across mobile applications. The objective is to simplify everyday mobile interactions by allowing users to perform tasks using simple voice commands instead of manual navigation.

The solution is designed to be compatible with Droidrun’s framework and cloud, enabling scalable mobile automation.

---

## 🧩 Problem Statement
Mobile applications require users to manually navigate multiple screens for repetitive tasks such as booking rides, checking attendance, adjusting system settings, or setting reminders. This process is time-consuming, inefficient, and confusing for many users.

Existing voice assistants primarily provide information but lack the ability to perform real actions within mobile applications. There is a need for an intelligent AI agent that can understand user intent and directly automate mobile app workflows.

---

## 💡 Solution
We developed a voice-controlled AI agent that converts natural language voice commands into actionable tasks on mobile applications. The system captures user voice input, converts it to text, detects user intent using an AI-based logic layer, and maps the intent to a specific app action.

For Round 1, the project demonstrates the complete end-to-end workflow using a Droidrun mock execution layer to validate feasibility and system design. The same architecture can be extended to real mobile devices using Droidrun’s cloud APIs in later stages.

---

## ⚙️ System Architecture
Voice Input → Intent Detection → Action Mapping → Droidrun Execution

---

## 🛠️ Tech Stack
- Python 3.10  
- SpeechRecognition  
- PyAudio  
- Rule-based AI intent detection  
- Droidrun (Mock Integration)  

---

## 📂 Project Structure
