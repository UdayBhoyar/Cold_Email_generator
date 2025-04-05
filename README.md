
---

## 📧 Cold Email Generator using LLaMA 3

This project automatically generates personalized cold emails based on job postings using the **LLaMA 3.1 model** via the [Together.ai API](https://www.together.ai/). It scrapes job descriptions from a given link, analyzes them, and generates a tailored cold email suited to the role.

---

### 🚀 Features

- 🔗 **URL-based job description scraping**  
- 🧠 **LLaMA 3.1 model integration** for natural-sounding email generation  
- ✍️ Includes subject line, intro, matching skills, call to action, and sign-off  
- 📄 Outputs cold email to a `.txt` file  

---

### 🛠️ Tech Stack

- Python  
- LangChain  
- Together.ai API (LLaMA 3.1)  
- BeautifulSoup (for web scraping)  
- dotenv (for secure API key loading)

---

### 📦 Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/UdayBhoyar/Cold_email_generator.git
   cd Cold_email_generator/email_gen
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your Together.ai API key to `.env`:**
   ```
   TOGETHER_API_KEY=your_api_key_here
   ```

4. **Run the app:**
   ```bash
   python main.py
   ```

---

### 💡 How It Works

1. Enter a job posting link.
2. The script scrapes the job description.
3. It feeds the job details to the LLaMA 3.1 model.
4. A cold email is generated and printed + saved to `cold_email_output.txt`.

---

### 📄 Example Output

```txt
Subject: Software Engineer Interested in Your Opening

Hi [Hiring Manager],

I came across the job listing for Software Engineer and was excited to see that the role aligns with my skills in Java, C++, and software development...

...
```

---

### 🧠 Powered By

- [Together.ai](https://www.together.ai/)
- [Meta LLaMA 3](https://ai.meta.com/llama/)
- [LangChain](https://www.langchain.com/)

---

### 📬 Contact

Made with ❤️ by [Uday Bhoyar](https://github.com/UdayBhoyar)

---

Let me know if you want this in `README.md` format or want to add badges, demo GIFs, or contribution guidelines too!
