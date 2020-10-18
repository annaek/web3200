from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/links')
def links():
    return render_template('links.html')

@app.route('/links/horror')
def horror():
    return render_template('horror.html')

@app.route('/links/business')
def business():
    return render_template('business.html')

@app.route('/links/science')
def science():
    return render_template('science.html')

@app.route('/links/horror/horror_book1')
def horror_book1():
    return render_template('horror_book1.html')

@app.route('/links/horror/horror_book2')
def horror_book2():
    return render_template('horror_book2.html')

@app.route('/links/horror/horror_book3')
def horror_book3():
    return render_template('horror_book3.html')

@app.route('/links/business/business_book1')
def business_book1():
    return render_template('business_book1.html')

@app.route('/links/business/business_book2')
def business_book2():
    return render_template('business_book2.html')

@app.route('/links/business/business_book3')
def business_book3():
    return render_template('business_book3.html')

@app.route('/links/science/science_book1')
def science_book1():
    return render_template('science_book1.html')

@app.route('/links/science/science_book2')
def science_book2():
    return render_template('science_book2.html')

@app.route('/links/science/science_book3')
def science_book3():
    return render_template('science_book3.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")