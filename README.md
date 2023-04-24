openai-ask-api
================
openai-ask-api is a JSON Web API written in Python that uses the OpenAI to resolve text-based prompts.

Running Locally
------------
Navigate to the openai-ask-api directory.
```
cd openai-ask-api
```

Install dependencies with pip
```
pip install -r requirements.txt
```

Set the 'OPENAI_API_KEY' environment variable:
```
export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Run the application with python
```
python app.py
```

API
-----
POST /prompt
```
curl --location 'http://127.0.0.1:5000/prompt' --header 'Content-Type: application/json' \
--data '{
    "prompt": "What is the meaning of life?"
}
```

Response
```
{"prompt": "What is the meaning of life?", "response": "To be happy."}
```

Docker
------

We also provide a Docker image to make it easier to run *openai-ask-api*
```
docker build . -t openai-ask-api -f docker/Dockerfile
```

Then run the image
```
docker run --rm -p 5000:5000 --env OPENAI_API_KEY=<YOUR_OPENAI_API_KEY> openai-ask-api
```
