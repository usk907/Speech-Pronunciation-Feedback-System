# 🎙️ Speech Pronunciation Feedback System

A powerful, interactive application built with **Gradio** and **OpenAI Whisper** that provides real-time, detailed feedback on speech pronunciation accuracy. Users speak a target sentence, and the system transcribes the audio, calculates an accuracy score, identifies specific errors, and generates natural language feedback.

---

## ✨ Features

* **Accurate Transcription:** Uses the **Whisper** model for state-of-the-art Automatic Speech Recognition (ASR).
* **Levenshtein Accuracy Score:** Provides a quantitative percentage score for the similarity between spoken and target text.
* **Word-Level Error Detection:** Highlights specific words that were misspoken, omitted, or added.
* **Phonetic Suggestions:** Uses the CMU Pronouncing Dictionary to offer phonetic hints and similar-sounding words for improved pronunciation.
* **AI-Generated Feedback:** Leverages a **T5 model** to provide clear, human-readable feedback and corrections.
* **Simple Web Interface:** Hosted via **Gradio** for easy access and testing.

---

## 🛠️ Installation and Setup

### Prerequisites

You must have Python (version 3.8 or higher) installed.

### 1. Clone the Repository

```bash
git clone [YOUR_REPO_URL]
cd speech-pronunciation-feedback-system
