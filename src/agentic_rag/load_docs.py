import os
import weaviate
from weaviate.classes.config import Configure
import json

client = weaviate.connect_to_local()


print(client.is_ready())

internal_docs = client.collections.get("tax_docs")
if not internal_docs:
    internal_docs = client.collections.create(
        name="tax_docs",
        vectorizer_config=Configure.Vectorizer.text2vec_ollama(  # Configure the Ollama embedding integration
            api_endpoint="http://host.docker.internal:11434",  # Allow Weaviate from within a Docker container to contact your Ollama instance
            model="nomic-embed-text",  # The model to use
        ),
        generative_config=Configure.Generative.ollama(
            model="llama3.2:1b",
            api_endpoint="http://host.docker.internal:11434",
        ),
    )

docs_dir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "internal_docs"
)
markdown_files = [f for f in os.listdir(docs_dir) if f.endswith(".md")]


with internal_docs.batch.dynamic() as batch:
    for filename in markdown_files:
        with open(os.path.join(docs_dir, filename), "r") as f:
            content = f.read()
            batch.add_object(
                {
                    "content": content,
                    "class_name": filename.split(".")[0],
                }
            )
            print(f"Added {filename.split('.')[0]} to Weaviate")
