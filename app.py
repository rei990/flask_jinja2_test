from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', name='World', age=20, items=['apple', 'banana', 'cherry'], tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<string:task>')
def delete_task(task):
    if task in tasks:
        tasks.remove(task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)