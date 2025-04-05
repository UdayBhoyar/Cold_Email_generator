import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain_together import Together
from langchain_core.prompts import PromptTemplate

# Load API Key
load_dotenv()

# Setup LLaMA 3.1 Model
llm = Together(
    model="meta-llama/Llama-3-8b-chat-hf",
    temperature=0.7,
    max_tokens=800,
    together_api_key=os.getenv("TOGETHER_API_KEY")
)

# Prompt Template
prompt = PromptTemplate.from_template(
    """
    You are an expert cold email writer.

    Based on the following job listing, write a cold email introducing the sender as a great fit for the position.

    The email should include:
    - Subject line relevant to the role
    - Friendly intro
    - Experience matching job role
    - Tech stacks or skills required
    - Call to action to schedule interview or send resume
    - Professional sign off

    ### JOB LISTING:
    {job_details}

    ### EMAIL:
    """
)

def scrape_job_post(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else "Job Opening"
        text = soup.get_text(separator='\n')
        lines = [line.strip() for line in text.splitlines() if len(line.strip()) > 30]
        combined = "\n".join(lines)
        return f"Job Title: {title}\n\nFull Description:\n{combined[:3000]}"
    except Exception as e:
        return f"Error scraping job page: {e}"

# Main Logic
if __name__ == "__main__":
    job_url = input("Paste the URL of the job opening: ")
    job_details = scrape_job_post(job_url)

    email_chain = prompt | llm
    response = email_chain.invoke({"job_details": job_details})

    # Output the result
    print("\nGenerated Cold Email:\n")
    print(response)

    # Save to file
    with open("cold_email_output.txt", "w", encoding="utf-8") as f:
        f.write(response)
        print("\n✅ Email saved to cold_email_output.txt")
