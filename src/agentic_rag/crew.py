import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from agentic_rag.tools.weaviate_tool import WeaviateTool
from crewai_tools import EXASearchTool, WebsiteSearchTool


from dotenv import load_dotenv

load_dotenv()


@CrewBase
class AgenticRagCrew:
    """AgenticRag crew"""

    llm = LLM(model="groq/llama-3.1-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))

    @agent
    def document_rag_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["document_rag_agent"],
            tools=[WeaviateTool()],
            verbose=True,
            llm=self.llm,
        )

    @agent
    def web_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["web_agent"],
            tools=[EXASearchTool(), WebsiteSearchTool()],
            verbose=True,
            llm=self.llm,
        )

    @agent
    def code_execution_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["code_execution_agent"],
            verbose=True,
            llm=self.llm,
        )

    @task
    def fetch_tax_docs_task(self) -> Task:
        return Task(
            config=self.tasks_config["fetch_tax_docs_task"],
        )

    @task
    def answer_question_task(self) -> Task:
        return Task(
            config=self.tasks_config["answer_question_task"], output_file="report.md"
        )

    @task
    def business_trends_task(self) -> Task:
        return Task(config=self.tasks_config["business_trends_task"])

    @task
    def graph_visualization_task(self) -> Task:
        return Task(config=self.tasks_config["graph_visualization_task"])

    @crew
    def crew(self) -> Crew:
        """Creates the AgenticRag crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.hierarchical,
            verbose=True,
            manager_llm="openai/gpt-4o",
            memory=True,
        )
