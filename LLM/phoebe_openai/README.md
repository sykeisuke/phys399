# PHYS399 Lecture 11, Exercise 1: Phoebe with the OpenAI API

This small Streamlit app turns the Fall 2025 Physics course CSV into searchable
documents. It uses OpenAI embeddings, an in-memory Chroma database, and a
LangChain agent with one search tool. **Ollama is not required.**

## Download and install

1. On the [PHYS399 GitHub page](https://github.com/sykeisuke/phys399), choose
   **Code → Download ZIP** and unzip it. Download the complete repository because
   the app uses `JupyterNote/data/lec11_ex1.csv`.
2. Open Terminal (macOS) or Anaconda Prompt (Windows), and go to the unzipped
   `phys399` directory. Make a fresh Python 3.11 environment so older LangChain
   packages from other exercises cannot conflict:

   ```bash
   conda create -n phys399-phoebe python=3.11 -y
   conda activate phys399-phoebe
   ```

3. Install the required packages and launch the app:

   ```bash
   python -m pip install -r LLM/phoebe_openai/requirements.txt
   python -m streamlit run LLM/phoebe_openai/app.py
   ```

4. Open the local URL shown in the terminal, usually `http://localhost:8501`.
   Enter **your own OpenAI API key** in the sidebar. Do not save the key in a
   notebook, source file, screenshot, or GitHub commit. An API key with billing
   access is required; ChatGPT access alone does not supply an API key.

The first launch sends the CSV rows to the OpenAI embeddings API. Each question
also calls the API. Usage may incur charges. The app does not write the key or
the vector database to disk. Close the terminal to stop the app.

Try: “Which courses are taught by Prof. Yoshihara in Fall 2025?” The CSV is a
**Fall 2025 teaching dataset**, not a current course schedule. Semantic search
finds similar text; it does not guarantee a complete or exact database filter.

## What to look at in the code

- `load_documents`: one CSV row becomes one LangChain `Document`.
- `build_store`: OpenAI turns the document text into embedding vectors, and
  Chroma stores them in memory.
- `search_courses`: the agent's tool retrieves similar course rows.
- `build_agent`: the chat model decides when to call the tool and answers from
  its results.

If you see `ModuleNotFoundError`, make sure `phys399-phoebe` is activated and
rerun the install command with the same Python that launches Streamlit. If the
app reports an API error, check your key and your API account's billing and
model access.
