# app.py

# Import required libraries
import os
from dotenv import load_dotenv
from llama_index.llama_dataset import download_llama_dataset
from llama_index.vector_stores import AstraDBVectorStore
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
)

# Load API keys from .env file
load_dotenv()

ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Load documents
documents = SimpleDirectoryReader(r"/Users/lily/git/hello-llamaindex-astra/data").load_data()
print(f"Total documents: {len(documents)}")
print(f"First document, id: {documents[0].doc_id}")
print(f"First document, hash: {documents[0].hash}")
print(
    "First document, text"
    f" ({len(documents[0].text)} characters):\n"
    f"{'=' * 20}\n"
    f"{documents[0].text[:360]} ..."
)

# Create a vector store instance
astra_db_store = AstraDBVectorStore(
    token=ASTRA_DB_APPLICATION_TOKEN,
    api_endpoint=ASTRA_DB_API_ENDPOINT,
    collection_name=collection,
    embedding_dimension=1536,
)

storage_context = StorageContext.from_defaults(vector_store=astra_db_store)

index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context
)

# Query the index
query_engine = index.as_query_engine()
query_string_1 = "Why did the author choose to work on AI?"
response = query_engine.query(query_string_1)

print(query_string_1)
print(response.response)

# Retrieve results
retriever = index.as_retriever(
    vector_store_query_mode="default",
    similarity_top_k=3,
)

nodes_with_scores = retriever.retrieve(query_string_1)

print(query_string_1)
print(f"Found {len(nodes_with_scores)} nodes.")
for idx, node_with_score in enumerate(nodes_with_scores):
    print(f"    [{idx}] score = {node_with_score.score}")
    print(f"        id    = {node_with_score.node.node_id}")
    print(f"        text  = {node_with_score.node.text[:90]} ...") 

# Set the retriever to sort results by Maximal Marginal Relevance (MMR)
retriever = index.as_retriever(
    vector_store_query_mode="mmr",
    similarity_top_k=3,
    vector_store_kwargs={"mmr_prefetch_factor": 4},
)

nodes_with_scores = retriever.retrieve(query_string_1)

print(query_string_1)
print(f"Found {len(nodes_with_scores)} nodes.")
for idx, node_with_score in enumerate(nodes_with_scores):
    print(f"    [{idx}] score = {node_with_score.score}")
    print(f"        id    = {node_with_score.node.node_id}")
    print(f"        text  = {node_with_score.node.text[:90]} ...")
