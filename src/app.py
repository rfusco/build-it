import os, json
from flask import Flask, render_template, request

from createPrompt import createPrompt
from handleGemini import generateResponse, validateCode

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static')
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/lets-see')
def index():
    return render_template('main.html')

@app.route('/generated')
def generated():
    return render_template('generated.html')

@app.route('/result', methods=['POST'])
def process():
    user_input = request.form['user_input']

    prompt = createPrompt(user_input)

    try:
        # Generate the response from the AI
        raw_response = generateResponse(prompt)

        valid_code = validateCode(raw_response)

        print("Validating code: ", valid_code)
        raw_response = valid_code


        raw_response = raw_response.replace('json', '')
        raw_response = raw_response.replace('```', '')

        print("Raw Response: ", raw_response)

        # Parse the JSON
        response_data = json.loads(raw_response.strip())
        print("Parsed Response: ", response_data)

        # Extract the HTML code
        html_code = response_data.get('html', '<p>No HTML provided</p>')

        # Save the HTML code to a file in the templates folder
        with open(os.path.join(BASE_DIR, 'templates', 'generated.html'), 'w', encoding='utf-8') as html_file:
            html_file.write(html_code)

        #extract the js
        js_code = response_data.get('javascript', '//No js provided')
        with open(os.path.join(BASE_DIR, 'static', 'generated.js'), 'w', encoding='utf-8') as js_file:
            js_file.write(js_code)

        #extract the css
        css_code = response_data.get('css', '/* No css */')
        with open(os.path.join(BASE_DIR, 'static', 'generated.css'), 'w', encoding='utf-8') as css_file:
            css_file.write(css_code)
        

        return f"""Description: {response_data['description']} 
        Page has been generated successfully! Visit <a href='/generated'>here</a>."""
    except json.JSONDecodeError as e:
        return f"Error: Invalid JSON response - {str(e)}. Raw response: {raw_response}"
    except Exception as e:
        return f"An error occurred: {str(e)}"



if __name__ == '__main__':
    app.run(debug=True)
