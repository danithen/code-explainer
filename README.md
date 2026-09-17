# Explain My Code

An LLM-powered Python code explanation tool.
## AI Usage Disclaimer:
ChatGPT (GPT-5.6 Luna), September 15-16, 2026: Used AI assistance to develop and document the Code Explainer application (app.py, Dockerfile, README, etc.). I created the Git repository setup, reviewed code and adapted for the project. I changed the streamlit configuration to only expose the localhost page, updated the model call to point to the proper model, and reworked the code to use litellm instead of openai so I could tinker with other models.
## What it does

Users paste Python code into the application. The application sends
the code to an LLM through the Duke AI Gateway and returns:

- An explanation of the code
- A step-by-step walkthrough
- Potential bugs and performance issues
- Suggestions for improvement
- An example of how the code behaves

## Technologies

- Python
- Streamlit
- LiteLLM API/SDK
- uv
- Docker

## Running locally

Create a `.env` file:

DUKE_AI_API_KEY=your_key_here

Then:

```bash
git clone https://github.com/danithen/code-explainer
```
```bash
sudo docker build --no-cache -t code-explainer .
```
```bash
sudo docker run --rm   --env-file .env   -p 127.0.0.1:8501:8501   code-explainer
```
browse to:
```
http://localhost:8501
```
