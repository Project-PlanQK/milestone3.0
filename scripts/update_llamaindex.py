import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

# Pfade für Daten und Storage
DATA_DIR = "data"
PERSIST_DIR = "storage"

def update_embeddings():
    # Falls der Storage existiert, lade bestehenden Index
    if os.path.exists(PERSIST_DIR):
        print("load index...")
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
    else:
        print("create new index...")
        documents = SimpleDirectoryReader(DATA_DIR).load_data()
        index = VectorStoreIndex.from_documents(documents)

    # save new embeddings
    index.storage_context.persist(STORAGE_DIR)
    print("updated and saved embeddings")

if __name__ == "__main__":
    update_embeddings()