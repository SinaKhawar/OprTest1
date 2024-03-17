from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    text1 = "This information is from text 1"
    text2 = "اسم من سینا خاور  است من شاگرد صحنف ۱۱ مکتب هست"
    # Define menu items
    menu_items = [
        {'name': 'Home', 'url': '#'},
        {'name': 'Contact', 'url': '/web/contact'},
        {'name': 'SignIn', 'url': '/web/login'}  # corrected URL path
    ]
    slider = [
        {'h1': 'Welcome','h2': 'This website is for education','p': 'To improve your skills, visit our website and its content', 'class': 'slide' },
        {'h1': 'Slider 2 ','h2': 'Slide 2 content for ','p': 'Slide 2 p content for your test', 'class': 'slide' },
        {'h1': 'Slider 3','h2': 'slider 3 h2 content','p': 'slider 3 p content following education for better understanding', 'class': 'slide' },
        {'h1': 'Slide 4 ', 'h2': 'Content for slide 4 for the test', 'p': 'This slide which is slide 4 is designed to demonstrate the usage of the slider', 'class': 'slide'}
    ]
    ramazan = [
        {'nation': 'YTC', 'km': '1222'},
        {'nation': 'RTC', 'km': '500'},
        {'nation': 'NEZ', 'km': '3334'},
    ]
    # Render the template with menu items
    return render_template('index.html', menu_items=menu_items, text1=text1, text2=text2, slider=slider, ramazan=ramazan)

@app.route('/web/login')
def login():
    uName = 'test@test.com'
    return render_template('web/login.html')

@app.route('/web/contact')
def contact():
    uName = 'test@test.com'
    return render_template('web/contact.html')

if __name__ == '__main__':
    app.run(debug=True)
