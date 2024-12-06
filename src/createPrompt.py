from serveCSS import getCSS

css_file = getCSS()

prompt = f"""
Come up with a random idea for a basic webapp with the following parameters:
- Provide a brief one-sentence description in a 'description' field.
- Include a field called 'html' with the code for a functional webpage in vanilla HTML.
  The source to the script you will create should be 'static/generated.js'
- Include a field called 'javascript' with the code for a functional webpage with vanilla JavaScript.
- If any JavaScript is generated keep it without any errors. It is of utmost importance to generate JavaScript without 
  errors. No identidier expected errors. No missing name after . operator error. Generate code that is ready to run as is.
  Do not use any APIs that require api keys. Ensure to use the whole screen.
- Include a field called 'css' with the css code to syle the html page according to this css file {css_file}
- Keep the code minimal and self-contained.
Respond only with a valid JSON object, no additional text. The description is 
"""

def createPrompt(input):
  return str(prompt + input)