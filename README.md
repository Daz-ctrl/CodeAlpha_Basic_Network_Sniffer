# CodeAlpha: Basic Network Sniffer

A lightweight Python-based network analysis tool engineered to intercept, parse, and log live Layer 3 network traffic. Developed as part of the **CodeAlpha Cybersecurity Internship program (Task 1)**.

## 📌 Project Overview
This project demonstrates the fundamentals of network protocols and packet anatomy by capturing real-time network traffic[cite: 1]. It handles packet parsing natively on Windows environments by utilizing Layer 3 raw sockets, bypassing traditional requirements for external packet capture drivers (like Npcap/WinPcap).

## 🚀 Key Features
* **Live Traffic Capture:** Intercepts real-time IPv4 network packets flowing through the active network interface[cite: 1].
* **Protocol Classification:** Dynamically identifies and separates **TCP** and **UDP** network traffic[cite: 1].
* **Data Extraction:** Outputs critical packet architecture components, including Source IP, Destination IP, and Protocol Type[cite: 1].
* **Payload Inspection:** Extracts and displays raw application payload segments in hexadecimal format for structural analysis[cite: 1].

## 🛠️ Tech Stack & Dependencies
* **Language:** Python 3.x
* **Core Library:** `scapy` (for packet manipulation and sniffing)[cite: 1]

## 💻 Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/Daz-ctrl/CodeAlpha_Basic_Network_Sniffer.git](https://github.com/Daz-ctrl/CodeAlpha_Basic_Network_Sniffer.git)
cd CodeAlpha_Basic_Network_Sniffer
