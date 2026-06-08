# Fake Job Offer Detector Bot
**Software Engineering Project Documentation**

---

## 1. Problem Statement
The rise of digital recruitment has unfortunately led to a parallel increase in employment scams. Students, recent graduates, and job seekers frequently encounter fraudulent job advertisements, internship opportunities, and recruitment messages via email, SMS, WhatsApp, and social media. These scams often trick applicants into paying "registration" or "training" fees, resulting in financial loss and emotional distress. There is a need for a simple, accessible tool that can analyze recruitment communications and flag potentially fraudulent offers based on known scam patterns.

## 2. Objectives
- **Primary Objective:** To develop a web application that allows users to analyze job advertisements and determine their likelihood of being a scam.
- **Educational Objective:** To demonstrate the application of software engineering principles, including requirements gathering, database design, backend development with Python/Flask, frontend UI design, and testing.
- **Functional Objective:** To classify job text into three risk levels: Safe, Suspicious, and Likely Scam, while providing transparent reasons for the classification.

## 3. Functional Requirements
1. **Text Input:** The system must provide a large text area for users to paste job advertisements or messages.
2. **Analysis Engine:** The system must process the text and compare it against a predefined list of suspicious keywords and phrases (e.g., "registration fee", "immediate hiring", "M-Pesa payment").
3. **Scoring System:** The system must calculate a risk score (0-100) based on weighted red flags.
4. **Classification:** The system must output a risk level: Safe (0-30), Suspicious (31-60), or Likely Scam (61-100).
5. **Reasoning:** The system must display the specific red flags triggered during the analysis.
6. **History Tracking:** The system must save every scan result, including the date, snippet, score, and classification, to a database.
7. **Dashboard:** The system must provide a dashboard summarizing total scans and counts for each classification level.

## 4. Non-Functional Requirements
1. **Usability:** The user interface must be clean, modern, intuitive, and responsive on both desktop and mobile devices.
2. **Performance:** The text analysis should execute rapidly, returning results within 2 seconds.
3. **Maintainability:** The codebase must be modular (e.g., separated routing, database, and logic files) and well-commented to allow for future keyword updates.
4. **Reliability:** The system must gracefully handle empty inputs or exceptionally long texts without crashing.

## 5. Use Cases
**Use Case 1: Analyze a Job Offer**
- **Actor:** Job Seeker
- **Action:** The user pastes a received WhatsApp message promising "guaranteed employment" if they send a "processing fee".
- **System Response:** The system analyzes the text, assigns a high score (e.g., 70%), classifies it as "Likely Scam", and lists "Requests payment" and "Promises guaranteed employment" as reasons.

**Use Case 2: View Scan History**
- **Actor:** Job Seeker
- **Action:** The user navigates to the "History" page to check an offer they analyzed yesterday.
- **System Response:** The system retrieves and displays a table of past scans from the database.

## 6. Database Design
The application uses SQLite with a single table to store scan history.

**Table: `JobScans`**
| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | INTEGER | Primary Key, Auto-increment |
| `job_text` | TEXT | The raw text submitted by the user |
| `score` | INTEGER | The calculated risk score (0-100) |
| `classification`| TEXT | The risk level (Safe, Suspicious, Likely Scam) |
| `reasons` | TEXT | Pipe-separated string of triggered red flags |
| `date_scanned` | TEXT | The date and time of the scan |

## 7. System Architecture
The application follows a standard Model-View-Controller (MVC) architectural pattern:
- **Model (Database Layer):** `database.py` manages connections and queries to `scans.db`.
- **Controller (Backend Logic):** `app.py` handles HTTP requests and routing. `detector.py` acts as a service layer performing the business logic (text analysis).
- **View (Frontend Layer):** Jinja2 templates (`templates/`) rendered with HTML5, styled with custom Vanilla CSS (`static/css/style.css`), and made interactive with JavaScript (`static/js/main.js`).

## 8. Installation Guide
### Prerequisites
- Python 3.8+ installed on your system.

### Steps
1. **Extract/Clone the Project Folder.**
2. **Open a Terminal** and navigate to the project directory.
3. **(Optional) Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the Application:**
   ```bash
   python app.py
   ```
6. **Access the App:** Open a web browser and go to `http://127.0.0.1:5000`.

## 9. Testing Plan
- **Unit Testing (Logic):** Manually test `analyze_job_text()` in `detector.py` using known scam phrases to ensure correct score aggregation and classification boundaries.
- **Integration Testing:** Verify that clicking "Analyze" correctly calls the backend, saves the result to the SQLite database, and redirects to display the results.
- **UI Testing:** Resize the browser window to verify the sidebar collapses into a mobile-friendly menu. Ensure colors contrast well and charts render properly.
- **Edge Cases:** Submit empty forms, massive blocks of text, and text containing special characters to ensure the app doesn't crash.

## 10. Future Improvements
- **Machine Learning Integration:** Upgrade from a rule-based system to an NLP model (e.g., Naive Bayes or fine-tuned BERT) trained on a dataset of real scam emails.
- **URL Scanning:** Add the ability to extract and scan URLs within the job text against known phishing databases.
- **User Authentication:** Allow users to create accounts so they can maintain private, personal scan histories.
- **Reporting Feature:** Enable users to report confirmed scams to build a community-driven database of fraudulent employers.
