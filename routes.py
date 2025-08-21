from flask import render_template

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/register')
    def register():
        return render_template('register.html')

    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html')

    @app.route('/settings')
    def settings():
        return render_template('settings.html')

    @app.route('/history')
    def history():
        return render_template('history.html')

    @app.route('/legal')
    def legal():
        return render_template('legal/index.html')

    @app.route('/landing')
    def landing():
        return render_template('landing/index.html')

    @app.route('/email/<template>')
    def email_template(template):
        return render_template(f'email/{template}.html')

    @app.route('/pdf/<doc>')
    def pdf_doc(doc):
        return render_template(f'pdf/{doc}.html')
