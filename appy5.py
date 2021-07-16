from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def items():
    return render_template('moreitems.html')

@app.route('/showitems', methods=['POST'])
def show_Items():
    if request.method == 'POST':
        result = request.form
        return render_template('showitems.html', result = result)


if __name__ == '__main__':
    app.debug=True
    app.run()

