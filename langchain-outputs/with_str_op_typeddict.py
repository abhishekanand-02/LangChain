# step 1: Normal invoke
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from typing import TypedDict

# load_dotenv()

# model  = ChatOpenAI()

# result = model.invoke("Started with promise, but quickly turned into a rambling mess that explained almost nothing.")
# print(result)


# step 2:  with class and with str output 

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

# Schema 
class Review(TypedDict):
    # summary : str
    # sentiment : str
    summary : Annotated[str,"A brief summary of the review"]
    sentiment : Annotated[str, "Return setiment of the review either negative , positive or neutral"]

model  = ChatOpenAI()

structured_model  = model.with_structured_output(Review)


result = structured_model.invoke("Started with promise, but quickly turned into a rambling mess that explained almost nothing.")
print(result)
print(result['summary'])
