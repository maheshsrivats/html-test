from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/streamlit')
def streamlit_app():
     subprocess.Popen(["streamlit", "run", "streamlit_app.py"])
     return "Streamlit app is running"

if __name__ == '__main__':
     app.run(debug=True)
