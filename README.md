# AI-Powered Candidate Matcher for Client Job Posts
This AI-powered application streamlines the candidate shortlisting process by extracting relevant skills from job postings and matching them with aspirant profiles. It generates personalized emails to client companies, highlighting the best-fit candidates based on the required skill set.

---

## Features
- Skill Extraction from raw job descriptions using LLaMA 3 70B (via ChatGroq)
- Semantic Matching of extracted skills with candidate tech stacks in ChromaDB
- Automated Email Drafting for client communication
- Streamlit-based Interface for easy use
- Simple pandas integration for managing candidate metadata

---

## Installation & Setup
#### Clone the Repository
```bash
git clone <repository-url>
cd Email_Gen
```

#### Install requirements:
```
pip install -r requirements.txt
```

#### Set up environment variables (.env file): *(in app folder)*
```bash
GROQ_API_KEY = your_groq_key
```
> **Note:** *Sign up at- https://console.groq.com/keys and get api key*

#### Run the main.py: *(in app folder)*
```
streamlit run main.py
```

#### Sample Email Output:
![image](https://github.com/user-attachments/assets/acd70432-bcf2-4ba7-b379-10e8e128cc43)

---

## Technologies Stack
  - **LLM:** LLaMA 3 70B (via LangChain ChatGroq)
  - **Framework:** LangChain
  - **Database:** ChromaDB
  - **Frontend:** Streamlit
  - **Data Handling:** pandas

---

## License
  - This project is licensed under the Apache License 2.0.
