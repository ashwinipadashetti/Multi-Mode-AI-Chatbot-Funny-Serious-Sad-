from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage

model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)
print("Choose your AI Mode")
print("1. Funny AI Agent")
print("2. Serious AI Agent")
print("3.Sad AI Agent")
choice=int(input("Enter your choice: "))
if choice==1:
    mode=" You are a funny AI agent.You respond with humor and jokes"
 
elif choice==2:
    mode=" You are a serious AI agent.You respond with seriousness and professionalism"
elif choice==3:
    mode=" You are a sad AI agent.You respond with sadness and empathy"


messages=[
    SystemMessage(content=mode)
]
print("-------Welcome type 0 to exit the chat------- ")
while True:
    prompt=input("You:")
    messages.append(HumanMessage(content=prompt))
    if prompt=="0":
        break
    response=model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot:", response.content)
print(messages)
