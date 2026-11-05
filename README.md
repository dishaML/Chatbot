# Chatbot

A small Streamlit chatbot powered by LangChain and Groq.

## Requirements

- Python 3.10 or later
- A Groq API key

## Setup

Create and activate a virtual environment, then install the project dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Create a `.env` file in the project root and add your Groq API key:

```text
GROQ_API_KEY=your_groq_api_key
```

Keep the `.env` file private. It is excluded from Git by `.gitignore`.

## Run

```powershell
streamlit run langchain_models.py
```

Enter a prompt in the app and select **Submit** to get a response. The current model is `openai/gpt-oss-120b`, configured in `langchain_models.py`.

## Dependencies

Install the packages listed in [`requirements.txt`](requirements.txt).

## License

This project is distributed under the MIT License; see [`LICENSE`](LICENSE).