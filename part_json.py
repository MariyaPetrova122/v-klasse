from flask import Flask
from flask import url_for, render_template, request, redirect
import json
import re


app = Flask(__name__)

@app.route('/')
def form():
    list_of_sentences = {
        '1':'Молодец',
        '2':'Ой, какой ты молодец',
        '3':'Иди куда хочешь',
        '4':'Нет, не обиделась',
        '5':'Все хорошо'}
    return render_template('form.html',list_of_sentences = list_of_sentences)




final_data = []
@app.route('/json')
def data():
    f = open('results.json', 'a', encoding = 'UTF-8')
    f.write(json.dumps(request.args)) 
    f.close()
    with open ('results.json','r', encoding = 'UTF-8') as f:
        for line in f:
            final_data.append(json.loads(line, encoding = 'UTF-8'))  
    final_json = json.dumps(final_data, ensure_ascii=False)
    return final_json 
    


@app.route('/stats')
def data_json():
    return render_template('stats.html', need_for_stats = need_for_stats) 

       
if __name__ == '__main__':
    app.run(debug=True)
