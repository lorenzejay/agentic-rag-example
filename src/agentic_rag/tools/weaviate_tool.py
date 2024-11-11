from crewai_tools import BaseTool
import weaviate
from pydantic import BaseModel, Field
from typing import Type, Optional, Any
from weaviate.classes.config import Configure
import json


class WeaviateToolSchema(BaseModel):
    """Input for WeaviateTool."""

    query: str = Field(
        ...,
        description="The query to search retrieve relevant information from the Weaviate database. Pass only the query, not the question.",
    )


class WeaviateTool(BaseTool):
    """Tool to search the Weaviate database"""

    name: str = "WeaviateTool"
    description: str = "A tool to search the Weaviate database for relevant information on internal documents"
    args_schema: Type[BaseModel] = WeaviateToolSchema
    query: Optional[str] = None

    def _run(self, query: str) -> str:
        """Search the Weaviate database

        Args:
            query (str): The query to search retrieve relevant information from the Weaviate database. Pass only the query as a string, not the question.

        Returns:
            str: The result of the search query
        """
        client = weaviate.connect_to_local()
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

        response = internal_docs.query.near_text(
            query=query,
            limit=3,
        )
        json_response = ""
        for obj in response.objects:
            json_response += json.dumps(obj.properties, indent=2)
        print("response", json_response)
        client.close()
        return json_response
