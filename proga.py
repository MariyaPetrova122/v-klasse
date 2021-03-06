from flask import Flask
from flask import url_for, render_template, request, redirect


app = Flask(__name__)

@app.route('/thank')
def thank():
    return render_template('thank.html')

@app.route('/form')
def form():
    list_of_sentences = {
        '1':'Молодец',
        '2':'Ой,какой ты молодец',
        '3':'Иди куда хочешь',
        '4':'Нет, не обиделась',
        '5':'Все хорошо'}
    if request.args:
        name = request.args['name']
        age = request.args['age']
        st_m = True if 'man' in request.args else False
        st_w = True if 'woman' in request.args else False
        return render_template('question.html', list_of_sentences = list_of_sentences)
    return render_template('form.html')

@app.route('/question')
def question():
    list_of_sentences = {
        '1':'Молодец',
        '2':'Ой,какой ты молодец',
        '3':'Иди куда хочешь',
        '4':'Нет, не обиделась',
        '5':'Все хорошо'}
    if request.args:
        st_happiness = True if 'happiness' in request.args else False
        st_sadness = True if 'sadness' in request.args else False
        st_anger = True if 'anger' in request.args else False
        st_reproach = True if 'reproach' in request.args else False
        st_sarcasm = True if 'sarcasm' in request.args else False
        return render_template('thank.html')
    return render_template ('question.html', list_of_sentences=list_of_sentences)
    

        
if __name__ == '__main__':
    app.run(debug=True)
