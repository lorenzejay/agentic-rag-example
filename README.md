# AgenticRag Crew

Welcome to the AgenticRag Crew project, powered by [crewAI](https://crewai.com), made by [Lorenze Jay](https://github.com/lorenzejay). This template shows off a hierarchical agentic process leverages multi agents with specific rag tools.

Taken inspration from [this](https://weaviate.io/blog/what-is-agentic-rag) blog post from the Weaviate team, we are able to have specific agents with specific rag tools:
1. WeaviateTool: This agent is responsible for searching the Weaviate database for relevant information. Use cases for these are:
    - Retrieving information on internal documents
2. ExaSearchTool: This agent is responsible for searching the ExaSearch database for relevant information. Use cases for these are:
    - Retrieving information from the web
3. Groq: Fast AI Inference


![Agentic RAG Architecture](/assets/practical_agentic_rag.png)


## Process
Using the hierarchical process, we are able to have a manager agent that is responsible for assigning tasks to the other agents. The manager agent will determine the best agent to use based on the task at hand. The task is determined by the user's question / query. 

This enables us to have a flexible system that can be used for a variety of use cases. QA Agents, Workflow Automation, etc.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/agentic_rag/config/agents.yaml` to define your agents
- Modify `src/agentic_rag/config/tasks.yaml` to define your tasks
- Modify `src/agentic_rag/crew.py` to add your own logic, tools and specific args
- Modify `src/agentic_rag/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the agentic-rag Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The agentic-rag Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the AgenticRag Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
