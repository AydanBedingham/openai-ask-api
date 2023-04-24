from flask import Flask, request
import json
import openai
import os
import logging
import structlog

log = structlog.getLogger(__name__)

structlog.configure(
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY == None:
    raise Exception("OPENAI_API_KEY environment variable is missing!")

log.debug("Found OPENAI_API_KEY: {}".format(OPENAI_API_KEY))

openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

def ask_chatgpt(prompt): 
    response = openai.Completion.create(engine="davinci", prompt=prompt, temperature=0)
    response_text = response['choices'][0]['text']
    return response_text

@app.route('/prompt', methods=['POST']) 
def prompt(): 
    if not request.is_json or 'prompt' not in request.json: 
        return 'No valid data', 400 
        
    request_data = request.get_json() 
    prompt = request_data['prompt']

    log.debug("Received Prompt: {}".format(prompt))

    response_text = ask_chatgpt(prompt)

    log.debug("Generated Response: {}".format(response_text))
    
    response = { 'prompt': prompt, 'response': response_text }
    
    return json.dumps(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0')