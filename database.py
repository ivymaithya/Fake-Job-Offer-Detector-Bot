import sqlite3
import datetime

DB_NAME = 'scans.db'

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database table if it doesn't exist."""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS JobScans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_text TEXT NOT NULL,
            score INTEGER NOT NULL,
            classification TEXT NOT NULL,
            reasons TEXT NOT NULL,
            date_scanned TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_scan(job_text, score, classification, reasons):
    """Inserts a new scan result into the database."""
    conn = get_db_connection()
    date_scanned = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Join reasons list into a string delimited by |
    reasons_str = "|".join(reasons)
    conn.execute(
        'INSERT INTO JobScans (job_text, score, classification, reasons, date_scanned) VALUES (?, ?, ?, ?, ?)',
        (job_text, score, classification, reasons_str, date_scanned)
    )
    conn.commit()
    conn.close()

def get_all_scans():
    """Retrieves all previous scans from the database, ordered by newest first."""
    conn = get_db_connection()
    scans = conn.execute('SELECT * FROM JobScans ORDER BY date_scanned DESC').fetchall()
    conn.close()
    
    # Process the reasons string back into a list
    processed_scans = []
    for scan in scans:
        scan_dict = dict(scan)
        scan_dict['reasons'] = scan_dict['reasons'].split("|") if scan_dict['reasons'] else []
        processed_scans.append(scan_dict)
    
    return processed_scans

def get_dashboard_stats():
    """Retrieves aggregate statistics for the dashboard."""
    conn = get_db_connection()
    total = conn.execute('SELECT COUNT(*) FROM JobScans').fetchone()[0]
    safe = conn.execute('SELECT COUNT(*) FROM JobScans WHERE classification = "Safe"').fetchone()[0]
    suspicious = conn.execute('SELECT COUNT(*) FROM JobScans WHERE classification = "Suspicious"').fetchone()[0]
    scam = conn.execute('SELECT COUNT(*) FROM JobScans WHERE classification = "Likely Scam"').fetchone()[0]
    conn.close()
    
    return {
        'total': total,
        'safe': safe,
        'suspicious': suspicious,
        'scam': scam
    }
