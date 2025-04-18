import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.schema import OutputParserException
from dotenv import load_dotenv

load_dotenv()
os.getenv("GROQ_API_KEY")

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature = 0,
            groq_api_key = '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',
            model_name="llama3-70b-8192"
        )

    def extract_jobs(self, cleaned_texts):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the careers page of a website.
            Your job is to extract the job posting and return it in JSON format containing the following keys: `role`, `experience`, `skills`, and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )

        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={'page_data': cleaned_texts})

        try:
            json_parser = JsonOutputParser()
            json_res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big, unable to parse jobs.")
        
        return json_res if isinstance(json_res, list) else [json_res]
    
    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}
            
            ### INSTRUCTION:
            You are a hiring manager at Abc company. Abc is an AI and software development company with seamless integration of business tools.
            Over our experience, we have numerous enterprises with tailored solutions, fostering scalability, process optimization, cost reduction and heightened efficiency.
            Your job is to write a code email to the client regarding the job mentioned above by fulfilling their needs.
            Also add the most relevant ones from the following links to showcase Abc's portfolio: {link_list}
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), 'link_list': links})

        return res.content