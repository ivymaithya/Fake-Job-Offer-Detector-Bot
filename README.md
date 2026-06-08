# Fake Job Offer Detector Bot 🕵️‍♀️

A full-stack web application designed to help students, recent graduates, and job seekers identify potentially fraudulent job advertisements, internship opportunities, and recruitment messages. 

This project was built as a University Software Engineering Project.

## ✨ Features
- **Scam Analysis Engine**: Rule-based algorithm that flags suspicious phrases (e.g., "registration fee", "guaranteed employment", "send money via M-Pesa").
- **Risk Scoring**: Calculates a risk percentage (0-100%) and categorizes the offer as Safe, Suspicious, or Likely Scam.
- **Detailed Reasoning**: Explains exactly which red flags triggered the score.
- **Scan History**: Saves all previous scans into an SQLite database for easy reference.
- **Dashboard**: Visualizes statistics on all analyzed job offers.

## 🛠️ Technology Stack
- **Backend**: Python, Flask
- **Database**: SQLite
- **Frontend**: HTML5, Vanilla CSS (Modern UI, Glassmorphism, Responsive), JavaScript

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ installed on your system.

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/ivymaithya/Fake-Job-Offer-Detector-Bot.git
   cd Fake-Job-Offer-Detector-Bot
   ```

2. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   # Activate on Windows:
   venv\Scripts\activate
   # Activate on macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:5000`

## 📄 Documentation
For detailed software engineering documentation (including Use Cases, Architecture, and Testing), please see the `documentation.md` file included in this repository.
