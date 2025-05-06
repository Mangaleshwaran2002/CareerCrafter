from dotenv import load_dotenv
import os
load_dotenv()
# print(os.environ['OPENROUTER_API_KEY'])
model_one_name="openrouter/meta-llama/llama-3.3-70b-instruct:free"
model_two_name="openrouter/qwen/qwen-2.5-72b-instruct:free"
from langchain_openai import ChatOpenAI
# Initialize the language model
llm_candidate = ChatOpenAI(
    model=model_one_name,
    api_key=os.environ['OPENROUTER_API_KEY'],
    base_url=os.environ['OPENROUTER_URL']
)
llm_hr = ChatOpenAI(
    model=model_two_name,
    api_key=os.environ['OPENROUTER_API_KEY'],
    base_url=os.environ['OPENROUTER_URL']
)

import PyPDF2
# Function to extract text from a PDF resume
def extract_text_from_pdf(pdf_path):
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            # Initialize PyPDF2 reader
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            # Loop through all pages and extract text
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n"
            return text.strip()  # Return the extracted text, removing trailing whitespace
    except Exception as e:
        return f"Error reading PDF: {str(e)}"
pdf_path = input("Enter resume path:")  # Update this with the actual path
resume_content = extract_text_from_pdf(pdf_path)

from crewai import Agent, Task, Crew, Process
import os

# HR Agent Definition
HRAgent = Agent(
    role='HR Interviewer',
    goal="""Conduct a realistic mock interview by asking relevant, job-specific questions based on the provided resume content and providing constructive feedback to the Candidate Agent.""",
    backstory="""This agent simulates an experienced HR professional with expertise in interview techniques and industry-standard questions. It creates a challenging yet supportive interview environment, evaluates responses, and offers actionable feedback to improve the candidate's performance.""",
    verbose=True,
    allow_delegation=False,
    llm=llm_hr
)

# Candidate Agent Definition
CandidateAgent = Agent(
    role='Candidate',
    goal="""Represent the user in a mock interview by providing accurate and polished responses to HR Agent's questions, using the provided resume content.""",
    backstory="""This agent embodies the user's professional persona by leveraging the provided resume details, including education, work experience, skills, and achievements. It responds confidently and authentically to various question types, ensuring alignment with the user's qualifications.""",
    verbose=True,
    allow_delegation=False,
    llm=llm_candidate
)

# Task for HR Agent
hr_interview_task = Task(
    description=f"""Conduct a mock interview with the Candidate Agent using the provided resume content as input.
    Steps:
    1. Review the resume content: {resume_content}.
    2. Generate a series of comman interview question like tell me about your self,what is your strenght?,what is your weakness?,etc...
    3. Generate a series of job-specific questions (introductory, behavioral, technical, situational) tailored to the job role and resume content.
    4. Ask one question at a time to the Candidate Agent.
    5. Evaluate the Candidate Agent's response and provide specific, actionable feedback, highlighting strengths and areas for improvement.
    6. Continue with the next question, repeating the process for a structured interview.""",
    expected_output="""A structured set of interview questions, each followed by specific, actionable feedback on the Candidate Agent's responses, highlighting strengths and areas for improvement.""",
    agent=HRAgent
    )

# Task for Candidate Agent
candidate_interview_task = Task(
    description=f"""Participate in a mock interview by responding to questions from the HR Agent using the provided resume content as input.
    Steps:
    1. Review the resume content: {resume_content}.
    2. Listen to the question asked by the HR Agent.
    3. Generate an accurate, polished, and professional response based on the resume content.
    4. Use the STAR method (Situation, Task, Action, Result) for behavioral questions and adapt responses to other question types (introductory, technical, situational) while aligning with the job role.""",
    expected_output="""Clear, concise, and relevant responses to each HR Agent question, reflecting the resume content, using the STAR method for behavioral questions, and maintaining a professional tone.""",
    agent=CandidateAgent
    )

# Optional: Create and run the crew
crew = Crew(
    agents=[HRAgent,CandidateAgent],
    tasks=[hr_interview_task,candidate_interview_task],
    process=Process.sequential
)

result = crew.kickoff()
print("##########################################")
print(result)
print("##########################################")