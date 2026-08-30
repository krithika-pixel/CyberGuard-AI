from flask import Flask, render_template, request, redirect, url_for, session
from database import db, init_db
from models import CyberSecurity
import os
import logging

app = Flask(__name__)

app.secret_key = 'replace_with_a_secure_key'

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True




database_url = os.environ.get('DATABASE_URL') or 'sqlite:///cybersecurity.db'

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# =========================================================
# INITIALIZE DATABASE
# =========================================================

try:

    init_db(app)

except Exception:

    logging.exception(
        'Database initialization failed with %s',
        app.config['SQLALCHEMY_DATABASE_URI']
    )

    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('mysql'):

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cybersecurity.db'

        init_db(app)


# =========================================================
# LOGIN
# =========================================================

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form.get(
            "username",
            ""
        ).strip()

        password = request.form.get(
            "password",
            ""
        ).strip()


        existing_user = None


        if username and password:

            existing_user = CyberSecurity.query.filter_by(
                username=username
            ).first()


        # Create user if not already present

        if existing_user is None and username and password:

            user = CyberSecurity(
                username=username,
                password=password
            )

            db.session.add(user)

            db.session.commit()


       

        if username:

            session['username'] = username

            return redirect(
                url_for('dashboard')
            )


    return render_template(
        'login.html'
    )



@app.route('/dashboard')
def dashboard():

    if 'username' not in session:

        return redirect(
            url_for('login')
        )


    total_requests = CyberSecurity.query.count()

    threats_detected = 0

    blocked_attacks = 0


    return render_template(

        'dashboard.html',

        username=session.get(
            'username',
            'User'
        ),

        total_requests=total_requests,

        threats_detected=threats_detected,

        blocked_attacks=blocked_attacks

    )




@app.route(
    '/detection',
    methods=['GET', 'POST']
)
def detection():

    

    prediction = None

    confidence = None

    severity = None


    # =====================================================

    if request.method == 'POST':

        file = request.files.get('file')


        if file and file.filename != '':

         

            prediction = "Normal"

            confidence = "95%"

            severity = "Low"


   

    return render_template(

        'detection.html',

        username=session.get(
            'username',
            'User'
        ),

        prediction=prediction,

        confidence=confidence,

        severity=severity

    )




@app.route('/analytics')
def analytics():

    return '<h1>Analytics page coming soon</h1>'




@app.route('/logout')
def logout():

    session.pop(
        'username',
        None
    )

    return redirect(
        url_for('login')
    )




if __name__ == '__main__':

    app.run(
        debug=True
    )
