import dotenv

dotenv.load_dotenv()

from crewai import Crew, Agent, Task
from crewai.project import CrewBase, agent, task, crew
from tools import search_tool, scrape_tool

@CrewBase
class NewsReaderAgent:
    
    @agent
    def news_hunter_agent(self):
        return Agent(
            config=self.agents_config["news_hunter_agent"],
            tools=[
                search_tool,
                scrape_tool,
            ],
        )
        
    @agent
    def summarizer_agent(self):
        return Agent(
            config=self.agents_config["summarizer_agent"],
            tools=[scrape_tool,],
        )
    
    @agent
    def curator_agent(self):
        return Agent(
            config=self.agents_config["curator_agent"],
            tools=[scrape_tool,],
        )
    
    @agent
    def translator_agent(self):
        return Agent(
            config=self.agents_config["translator_agent"],
        )


    @task
    def content_harvesting_task(self):
        return Task(           
            config=self.tasks_config["content_harvesting_task"],
        )
        
    @task
    def summarization_task(self):
        return Task(           
            config=self.tasks_config["summarization_task"],
        )
        
    @task
    def final_report_assembly_task(self):
        return Task(           
            config=self.tasks_config["final_report_assembly_task"],
        )
        
    @task
    def translate_task(self):
        return Task(           
            config=self.tasks_config["translate_task"],
        )


    @crew
    def crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )
    

result = NewsReaderAgent().crew().kickoff(inputs={"topic": "최신 글로벌 소식"})



# (task에서 markdown으로 output을 저장하지만)
# 각 개별 작업의 출력(output)을 프로그래밍적으로 접근할 수 있는 방법
#for task_output in result.tasks_output:
#    print(task_output)