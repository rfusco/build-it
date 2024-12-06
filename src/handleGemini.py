from initGemini import initGemini

model = initGemini()

def generateResponse(prompt):
  """
    Returns gemini response based on prompt.

    Args:
      prompt (str): The prompt.

    Returns:
      str: The Gemini response to the prompt.
    """
  try:
    return model.generate_content(prompt).text
  except Exception as e:
    return str(e)
  
def validateCode(json_object):
  """
  Returns the valid code files as a JSON object. This includes html, js, and css.

  Args:
    js_code (str): The code we want to validate

  Returns:
    str: The valid js code.
  
  """
  prompt = """Does this HTML, JavaScript, and CSS code have correct syntax that will allow it to be executed properly in the web?
  Do the seperate files integrate with each other correctly?
  The code should result in no errors when ran in the web. Do not change any of the file paths assume they are all correct.
  Repond with only a json object the same form as the one input. Do not change the functionality of the input.
  """

  return generateResponse(json_object + prompt)