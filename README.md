# EDUNET Cybersecurity with generative AI

🚀 Cybersecurity & Network Security Learning Journey

This repository documents my step-by-step learning and hands-on implementation in networking and cybersecurity, completed over a structured three-week progression.
Each week focuses on a different core concept, moving from network fundamentals to system monitoring and finally to AI-based intrusion detection.

📌 Week 1: Network Fundamentals using Cisco Packet Tracer
🔹 Overview

In Week 1, I focused on understanding basic computer networking concepts using Cisco Packet Tracer. The goal was to design, configure, and test a simple network topology to understand how devices communicate across different subnets.

🔹 Network Design

A Cisco 1941 Router connects two different networks

One network uses a Switch (LAN – 192.168.1.0/24)

The other network uses a Hub (LAN – 10.0.0.0/24)

Multiple PCs are connected on both sides with static IP addressing

🔹 Key Concepts Learned

IP addressing and subnetting

Router configuration and interface IP assignment

Difference between Switch and Hub

Packet flow between different networks

End-to-end connectivity testing using ping

🔹 Outcome

Successfully established communication between devices on different networks using routing, gaining a strong foundation in networking basics.

📌 Week 2: Key Logger System (Python)
🔹 Overview

In Week 2, I developed a Key Logger application using Python to understand system-level monitoring and how keystroke logging works from a cybersecurity perspective.

⚠️ Note: This project is strictly for educational and ethical learning purposes, focusing on system security awareness.

🔹 Features

Captures keyboard inputs

Start and stop logging functionality

Logs keystrokes into a file

Graphical User Interface (GUI) using Tkinter

Uses multithreading to prevent GUI freezing

🔹 Technologies Used

Python

Tkinter (GUI)

Threading

File handling

🔹 Key Concepts Learned

Keyboard event handling

Thread management

GUI-based application design

Ethical implications of monitoring software

🔹 Outcome

Gained practical understanding of how monitoring tools work and how such techniques can be detected and prevented in cybersecurity systems.

📌 Week 3: AI-Based Network Intrusion Detection System (AI-NIDS)
🔹 Overview

In Week 3, I built an AI-based Network Intrusion Detection System that uses Machine Learning to identify malicious network traffic such as DDoS attacks.

🔹 System Description

Uses a Random Forest classifier

Trained on real network traffic data from the CIC-IDS2017 dataset

Classifies traffic into:

Benign (Normal Traffic)

Malicious (Attack Traffic)

🔹 Features

Data preprocessing and feature selection

Model training and testing

Performance metrics (accuracy, confusion matrix)

Live Traffic Simulator to test network packets in real time

Probability-based attack detection

Rule-based override for obvious attack patterns

Interactive Streamlit dashboard

🔹 Technologies Used

Python

Scikit-learn

Pandas & NumPy

Streamlit

Matplotlib & Seaborn

🔹 Key Concepts Learned

Machine learning in cybersecurity

Supervised classification

Real-world intrusion detection logic

Combining ML with rule-based security

Building interactive dashboards

🔹 Outcome

Developed a functional AI-based intrusion detection system capable of detecting malicious network behavior with high accuracy.

🧠 Overall Learning Outcome

This three-week journey helped me progress from network fundamentals to system monitoring and finally to AI-driven cybersecurity solutions.
The projects demonstrate practical skills in:

Networking

Python programming

Security awareness

Machine learning

Real-world problem solving
