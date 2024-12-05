import os
import json
import google.generativeai as genai
from flask import Flask, render_template, request

# Load environment variables
API_KEY = os.getenv("API_KEY")

genai.configure(api_key = API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Explain how AI works")
# print(response.text)

#prompt
prompt = """Come up with a random idea for an basic webapp with these parameters. Respond only with a json object with a 
field for a brief one sentence description and other needed fields for the code segments. There should be a field called
html which is an html file where the idea can be viewed. It should be vanilla javascript and html this is very important"""


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/lets-see')
def index():
    return render_template('main.html')

@app.route('/result', methods=['POST'])
def process():
    # Get user input from the form
    user_input = request.form['user_input']

    try:
        #clean data and turn into json object for easy manipulation
        response = model.generate_content(prompt + user_input ).text
        response = response.replace('json', '')
        response = response.replace('`', '')
        response = json.loads(response)
        print(response)

    except Exception as e:
        response += f"An error occurred: {str(e)}"

    # Return the result to the user
    return response

if __name__ == '__main__':
    app.run(debug=True)
