from llama_index import SimpleDirectoryReader
from llama_index.llama_pack import download_llama_pack
# from app.engine.loader import get_documents

# download and install dependencies
NebulaGraphQueryEnginePack = download_llama_pack(
  "NebulaGraphQueryEnginePack", "./nebulagraph_pack"
)

# Load the docs (example of Paleo diet from Wikipedia)
# from llama_index import download_loader

# WikipediaReader = download_loader("WikipediaReader")
# loader = WikipediaReader()
# docs = loader.load_data(pages=['Paleolithic diet'], auto_suggest=False)

documents_for_graph = SimpleDirectoryReader(r"/Users/lily/git/GridGrokGrind/backend/data").load_data()

# docs = NebulaGraphQueryEnginePack(documents_for_graph)
# print(f'Loaded {len(docs)} documents')

# get NebulaGraph credentials (assume it's stored in credentials.json)

username = "root"
password = "nebula"
ip_and_port = "127.0.0.1:9669"

space_name = "book"
edge_types, rel_prop_names = ["relationship"], ["relationship"]
tags = ["entity"]
max_triplets_per_chunk = 10

# create the pack
nebulagraph_pack = NebulaGraphQueryEnginePack(
  username = username,
  password = password,
  ip_and_port = ip_and_port,
  space_name = space_name,
  edge_types = edge_types,
  rel_prop_names = rel_prop_names,
  tags = tags,
  max_triplets_per_chunk = max_triplets_per_chunk,
  docs = documents_for_graph
)