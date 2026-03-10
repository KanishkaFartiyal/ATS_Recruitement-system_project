from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = "college_project_secret_key"  # Required for flash messages

# Database Configuration
# Get the absolute path to the instance folder
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(BASE_DIR, 'instance', 'recruitment.db')

# Ensure the instance folder exists
os.makedirs('instance', exist_ok=True)

def get_db_connection():
    """Helper function to connect to SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

def init_db():
    """Initialize the database and create the candidates table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            skills TEXT,
            experience INTEGER,
            education TEXT,
            status TEXT DEFAULT 'Applied'
        )
    ''')
    conn.commit()
    conn.close()

# Initialize DB on startup
init_db()

@app.route('/')
def dashboard():
    """
    Dashboard: View all candidates.
    Uses Pandas to fetch and display data.
    """
    conn = get_db_connection()
    # Fetch all data
    df = pd.read_sql_query("SELECT * FROM candidates", conn)
    conn.close()
    
    # Convert DataFrame to list of dictionaries for Jinja2 template
    candidates = df.to_dict('records')
    return render_template('index.html', candidates=candidates)

@app.route('/add', methods=['GET', 'POST'])
def add_candidate():
    """Handle adding a new candidate."""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        skills = request.form['skills']
        experience = request.form['experience']
        education = request.form['education']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO candidates (name, email, phone, skills, experience, education, status)
            VALUES (?, ?, ?, ?, ?, ?, 'Applied')
        ''', (name, email, phone, skills, experience, education))
        conn.commit()
        conn.close()
        
        flash('Candidate added successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('add_candidate.html')

@app.route('/update_status/<int:id>', methods=['GET', 'POST'])
def update_status(id):
    """Handle updating the application status."""
    conn = get_db_connection()
    candidate = conn.execute('SELECT * FROM candidates WHERE id = ?', (id,)).fetchone()
    
    if request.method == 'POST':
        new_status = request.form['status']
        cursor = conn.cursor()
        cursor.execute('UPDATE candidates SET status = ? WHERE id = ?', (new_status, id))
        conn.commit()
        conn.close()
        
        flash('Status updated successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    conn.close()
    return render_template('update_status.html', candidate=candidate)

@app.route('/delete/<int:id>')
def delete_candidate(id):
    """Delete a candidate record."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM candidates WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    flash('Candidate deleted successfully!', 'danger')
    return redirect(url_for('dashboard'))

@app.route('/search')
def search_candidates():
    """
    Search functionality using Pandas.
    Filters by Name, Skills, or Experience.
    """
    query = request.args.get('q', '')
    min_exp = request.args.get('min_exp', type=int)
    
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM candidates", conn)
    conn.close()
    
    # Filter using Pandas
    if query:
        # Case-insensitive search in Name or Skills
        mask = df['name'].str.contains(query, case=False, na=False) | \
               df['skills'].str.contains(query, case=False, na=False)
        df = df[mask]
    
    if min_exp:
        df = df[df['experience'] >= min_exp]
    
    candidates = df.to_dict('records')
    return render_template('index.html', candidates=candidates, search_query=query)

if __name__ == '__main__':
    app.run(debug=True)