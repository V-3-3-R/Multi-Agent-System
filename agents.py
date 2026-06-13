from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, web_scrape

# Initialize the Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# Create the first agent 
def build_search_agent():
    return create_agent(
        model = llm,
        tools = [web_search]
    )

# Create the second agent
def build_reader_agent():
    return create_agent(
        model = llm,
        tools = [web_scrape]
    )

# Writer Chain
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.
     
Topic: {topic}
     
Research gathered: {research}
Structure the report as:
1. Introduction
2. Key Findings
3. Conclusion
4. Sources (List all URLs found in the research)

Be detailed, factual, and professional.""")
])

writer_chain = writer_prompt | llm | StrOutputParser()

#Crtic Chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.
Report: {report}

Respond in this exact format:
Score: X/10

Strengths:
-...
-...
-...

Areas for Improvement:
-...
-...

One line verdict:
-...
     
     """)
])

critic_chain = critic_prompt | llm | StrOutputParser()


