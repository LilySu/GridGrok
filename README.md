# GridGrok
LlamaIndex/Astra pdf table parser for the LlamaIndex and FutureProof Hackathon in Sunnyvale, CA Feb 2 - Feb 4, 2024.

Our aim is to enable semantic search on academic paper evaluation-metrics-tables data at a petabyte-capable scale through recursive approaches, resulting in a comprehensive knowledge graph.


## Getting Started

1. Create a `.env` file based on the `.env` example (see below)
2. Navigate to the frontend directory --> 
`npm install`
`npm run dev`
3. Navigate to the backend directory --> Install the dependencies with e.g. `pip install -r requirements.txt`. _(Python 3.8+ required. Working in a virtual environment is suggested as general best practice)_.
4. Within the backend directory, run the app with `python main.py` !

### The dot-env file

The environment variables expected in the `.env` file are:

- `OPENAI_API_KEY`, your OpenAI API key.
- `ASTRA_DB_APPLICATION_TOKEN`, the Token to access your Astra DB instance. The token must be created with role "Database Administrator".
- `ASTRA_DB_API_ENDPOINT`, the API ENDPOINT of your Astra DB, which you can find at the top of your dashboard to the right of your AstraDB instance, near the Token.
