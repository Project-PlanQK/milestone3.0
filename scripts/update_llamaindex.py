import os
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
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
    #load new docs
    documents = SimpleDirectoryReader(DATA_DIR).load_data()

    if documents:
        print(f"{len(documents)} found new docs, update index")
        index = VectorStoreIndex.from_documents(documents)

        # save new embeddings
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
        print("updated and saved embeddings")
    else:
        print("no new docs found")

if __name__ == "__main__":
    update_embeddings()