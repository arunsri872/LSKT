from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route('/')
def home_page():
    return render_template('temp-landing.html')

@views.route('/school')
def school_landing():
    return render_template('school-landing.html')

@views.route('/school/safety')
def school_safety():
    return render_template('school-health-safety.html')

@views.route('/school/apply')
def school_apply():
    return render_template('school-apply.html')

@views.route('/school/pannisai')
def school_pannisai():
    return render_template('school-pannisai.html')

@views.route('/school/tamil')
def school_tamil():
    return render_template('school-tamil.html')

@views.route('/school/dance')
def school_dance():
    return render_template('school-dance.html')

@views.route('/school/vocal')
def school_vocal():
    return render_template('school-vocal.html')

@views.route('/school/keyboard')
def school_keyboard():
    return render_template('school-keyboard.html')

@views.route('/temple')
def temple_page():
    return render_template('coming-soon.html')

@views.route('/charity')
def charity_page():
    return render_template('coming-soon.html')

@views.route('/services')
def services_page():
    return render_template('coming-soon.html')

@views.route('/about')
def about_page():
    return render_template('coming-soon.html')

@views.route('/calendar')
def calendar_page():
    return render_template('coming-soon.html')


