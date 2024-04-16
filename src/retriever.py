from dotenv import load_dotenv
import os
import google.generativeai as genai
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import GoogleGenerativeAI



if __name__ == '__main__':
    print("when file execution is ivoked by direct rather importing this block gets executed")
    # load environment
    load_dotenv()
    prompt = "what best name for the company which is provides IT services like {services}"
    template = PromptTemplate(
        input_variables=['services'],
        template=prompt
    )
    api_key = os.getenv("GOOGLE_API_KEY")
    llm= GoogleGenerativeAI(model='models/text-bison-001', google_api_key=api_key)
    chain= LLMChain(llm = llm, prompt=template )
    service =  "web development"
    input_data = {"services": service}
    response = chain.invoke(input=input_data)
    print(response)