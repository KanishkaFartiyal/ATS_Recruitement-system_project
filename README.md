Recruitment Management System (ATS)

A comprehensive **Applicant Tracking System** built with Python, Flask, SQLite, and Pandas. This web application helps recruiters manage candidate applications, track their status, and filter candidates based on skills and experience.

## Features

- **Admin Dashboard** - View all candidates in a clean table format
- **Admin Login** - Secure admin authentication system
- **Candidate Portal** - Candidates can register and login
- **Add Candidate** - Form to input candidate details
- **Resume Upload** - Upload candidate resumes (PDF/DOC)
- **Search & Filter** - Filter candidates by name, skills, or experience
- **Status Tracking** - Update application status (Applied, Shortlisted, Interview, Selected, Rejected)
- **Email Notifications** - Automatic email when status changes
- **Interview Scheduling** - Schedule interviews with date, time, and link
- **Candidate Notes** - Add notes/comments to each candidate
- **Export to Excel** - Download candidate list as Excel file
- **Dashboard Statistics** - Visual stats showing candidate distribution
- **Dark Mode** - Toggle between light and dark themes
- **Responsive Design** - Works on desktop and mobile devices

## Project Structure
Recruitment_Management_System/
├── instance/                 # SQLite database storage
├── static/
│   ├── style.css             # CSS Styling
│   └── uploads/              # Resume files storage
├── templates/
│   ├── base.html             # Main admin layout
│   ├── base_candidate.html   # Candidate layout
│   ├── login.html            # Admin login page
│   ├── candidate_login.html  # Candidate login page
│   ├── candidate_register.html # Candidate registration
│   ├── dashboard.html        # Admin dashboard
│   ├── candidate_dashboard.html # Candidate dashboard
│   ├── add_candidate.html    # Form to add new candidate
│   ├── update_status.html    # Form to update status
│   ├── interview.html        # Interview scheduling
│   ├── notes.html            # Add notes to candidate
│   └── candidate_update_profile.html # Update profile
├── app.py                    # Main Flask Application
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore file
└── README.md                 # Project documentation


   
