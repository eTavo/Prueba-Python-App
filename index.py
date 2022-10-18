from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/programas')
def programas():
    return render_template('programas.html')

@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    if request.method == 'POST':
        valor = request.form(input('cash'))
        return valor
    return render_template('calculadora.html')


if __name__ == '__main__':
    app.run(debug=True)

#https://www.youtube.com/watch  ?v=fxavwHPJ36o tutorial de web python 59min de 1.04hs
#https://j2logo.com/tutorial-flask-leccion-3-formularios-wtforms/
#https://www.youtube.com/watch?v=TK6DlBl63aI
#https://getbootstrap.com/docs/5.1/components/button-group/