from flask import Flask, render_template, request, redirect, url_for
from database import init_db, insert_scan, get_all_scans, get_dashboard_stats
from detector import analyze_job_text
import os

app = Flask(__name__)

# Initialize the database when the app starts
init_db()

@app.route('/')
def dashboard():
    """Renders the dashboard with summary statistics."""
    stats = get_dashboard_stats()
    return render_template('dashboard.html', stats=stats)

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    """Handles the job text analysis form."""
    if request.method == 'POST':
        job_text = request.form.get('job_text', '')
        
        # Analyze the text
        result = analyze_job_text(job_text)
        
        # Save to database
        insert_scan(
            job_text=job_text, 
            score=result['score'], 
            classification=result['classification'], 
            reasons=result['reasons']
        )
        
        return render_template('analyze.html', result=result, job_text=job_text)
        
    return render_template('analyze.html', result=None)

@app.route('/history')
def history():
    """Displays all previously scanned job offers."""
    scans = get_all_scans()
    return render_template('history.html', scans=scans)

@app.route('/about')
def about():
    """Displays information about the project."""
    return render_template('about.html')

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True, port=5000)
