from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/method_post', methods=['GET' , 'POST'])
def method_post():
    return render_template('method_post.html')

@app.route('/method_post_act', methods=['GET' , 'POST'])
def method_post_act():
    if request.method == 'POST':
        id = request.form["id"]
        password = request.form["password"]
        return render_template('method_post.html',id=id , password=password)


if __name__ == "__main__":
    app.run(debug=True , port=80 , host='0.0.0.0')