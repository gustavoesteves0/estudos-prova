from flask import Flask, request, redirect, url_for, render_template
from tinydb import TinyDB, Query

app = Flask(__name__)

# Inicializa o banco de dados TinyDB
db = TinyDB('db.json')
toDo_list = db.all()
toDo = Query()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', toDo_list=toDo_list)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        db.insert({'item': item})
    return render_template('index.html', toDo_list=toDo_list)

@app.route('/edit', methods=['POST'])
def edit_item():
    old_item = request.form.get('old_item')
    new_item = request.form.get('new_item')
    if db.search(toDo.item == old_item):
        db.update({'item': new_item}, toDo.item == old_item)
    return render_template('index.html', toDo_list=toDo_list)

@app.route('/delete', methods=['POST'])
def delete_item():
    item = request.form.get('item')
    db.remove(toDo.item == item)
    return render_template('index.html', toDo_list=toDo_list)

if __name__ == '__main__':
    app.run(debug=True)
