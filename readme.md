# Face Authentication System

This project is a face authentication system built using Python and Streamlit. It allows users to register and authenticate using their email, password, and facial recognition.

## Features

- **User Registration**: Users can sign up with their name, email, and password.
- **User Login**: Users can log in using their email and password.
- **Face ID Registration**: Users can register their face for authentication.
- **Face ID Authentication**: Users can log in using facial recognition.
- **Database Storage**: User data and facial descriptors are stored in an SQLite database.


### Key Files

- **[`config.py`](config.py)**: Contains database setup and user management functions (`add_user`, `login_user`).
- **[`main.py`](main.py)**: Provides a simple Google authentication interface.
- **[`recognition.py`](recognition.py)**: Handles facial recognition, including capturing photos, extracting face descriptors, and comparing faces.
- **[`pages/inscription.py`](pages/inscription.py)**: Implements user registration and login functionality.
- **[`pages/Face ID.py`](pages/Face%20ID.py)**: Implements Face ID registration and authentication.

## Requirements

- Python 3.10 or higher
- Streamlit
- OpenCV
- face_recognition
- SQLite3

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. Set up a virtual environment:
   ```bash    
    python -m venv env
    source env/Scripts/activate  # On Windows
    source env/bin/activate      # On macOS/Linux

3. Install dependencies:
   ```bash
    pip install -r env/requirements.txt

4. Create the database:
   ```bash
   python config.py

5. Run the Streamlit app:
   ```bash
    streamlit run main.py