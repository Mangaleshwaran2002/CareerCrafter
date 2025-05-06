# **CareerCrafter**

A Python-based application that simulates a realistic job interview using AI-powered agents. The system leverages CrewAI and large language models to conduct mock interviews by processing a candidate's resume, generating tailored interview questions, and providing actionable feedback. Designed to help job seekers practice and improve their interview skills in a professional, structured environment.

## Project Overview

The Mock Interview System uses two AI agents: an HR Interviewer and a Candidate. The HR Agent reviews the provided resume, generates a mix of common and job-specific questions, and evaluates responses with constructive feedback. The Candidate Agent responds to questions based on the resume, employing the STAR method for behavioral questions to ensure professional and relevant answers. The system is built with modularity and extensibility in mind, making it a valuable tool for career preparation.

## Features

- **Resume Processing**: Extracts text from PDF resumes using PyPDF2 for personalized question generation.
- **AI-Powered Agents**: Utilizes CrewAI and LangChain with OpenRouter's LLaMA and Qwen models for dynamic interview simulation.
- **Question Variety**: Generates common (e.g., "Tell me about yourself"), behavioral, technical, and situational questions tailored to the resume.
- **STAR Method Responses**: Candidate Agent structures behavioral responses using the Situation, Task, Action, Result framework.
- **Actionable Feedback**: HR Agent provides detailed, specific feedback on responses, highlighting strengths and areas for improvement.
- **Sequential Workflow**: Ensures a structured interview process with one question asked and answered at a time.

## Tech Stack

- **Python**: Core programming language for the application.
- **CrewAI**: Framework for orchestrating AI agents and tasks.
- **LangChain**: Integration with OpenAI-compatible models for natural language processing.
- **PyPDF2**: Library for extracting text from PDF resumes.
- **OpenRouter API**: Powers the HR and Candidate agents with LLaMA and Qwen models.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mangaleshwaran2002/CareerCrafter.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables for OpenRouter API:
   ```bash
   export OPENROUTER_API_KEY='your-api-key'
   export OPENROUTER_URL='https://openrouter.ai/api/v1'
   ```
4. Run the script:
   ```bash
   python CareerCrafter.py
   ```

## Screenshots
![CareerCrafter-s1](https://raw.githubusercontent.com/Mangaleshwaran2002/AI-Trip-Planner/refs/heads/master/Screenshot/AI-Trip-planner-s1.png)
![CareerCrafter-s1](https://raw.githubusercontent.com/Mangaleshwaran2002/AI-Trip-Planner/refs/heads/master/Screenshot/AI-Trip-planner-s2.png)

## Usage

1. Provide the path to a PDF resume when prompted.
2. The HR Agent will generate and ask interview questions based on the resume.
3. The Candidate Agent responds, and the HR Agent provides feedback.
4. Review the output for a structured interview transcript with questions, responses, and feedback.

## Future Enhancements

- Add support for multiple resume formats (e.g., DOCX, TXT).
- Implement a user interface for easier interaction (e.g., web or CLI).
- Enable customization of question types and interview duration.
- Integrate with a database to store interview sessions for progress tracking.

## Contributions

Contributions are welcome! Feel free to submit issues, fork the repository, or create pull requests to enhance the system.

## License

This project is licensed under the MIT License.
