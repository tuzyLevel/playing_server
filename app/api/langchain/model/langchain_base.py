import os
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.tools import tool

from langchain.agents import create_openai_functions_agent, AgentExecutor


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    api_key=OPENAI_API_KEY,
    verbose=True
)
prompt = hub.pull("hwchase17/openai-functions-agent")


@tool
def add(a, b):
    """
        add two numbers
    """
    return a+b


system_template = "あなたは、質問者からの質問を{language}で回答するAIです。"
human_template = "質問者：{question}"
system_message_prompt = SystemMessagePromptTemplate.from_template(
    system_template)
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt])
prompt_message_list = chat_prompt.format_prompt(
    language="日本語", question="ITエンジニアについて30文字で教えて。").to_messages()
tools = [add]

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


def get_answer(messages: str):
    response = agent_executor.invoke(
        {
            "input": messages,
        }
    )
    print(response)

    return response
