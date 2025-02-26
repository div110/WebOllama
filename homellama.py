from flask import Flask, request, render_template
import ollama

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ollama', methods=['POST'])
def query_ollama():
    user_input = request.form.get("input")
    if user_input:
        try:
            response = ollama.chat(
                    model="deepseek-r1:1.5b",
                    messages=[{"role":"user","content": user_input}]
                )
            model_response = response['message']['content']

            return render_template('index.html', response=model_response, user_input=user_input)
        except Exception as e:
            return render_template('index.html',error=str(e))
        return render_template('index.html',error="no input!!")

if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1",port=5000) #can modify this
