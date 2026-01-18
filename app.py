from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

comments = []  # In-memory storage (use SQLite for prod)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        comments.append({'name': name, 'comment': comment})
        return jsonify({'status': 'success'})
    return render_template('index.html', comments=comments)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
