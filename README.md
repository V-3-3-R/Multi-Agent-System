# 🤖 Multi-Agent Research System

<div align="center">

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-00A3FF?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

### 🔍 Search → 📖 Read → ✍️ Write → 🧠 Critique

An autonomous AI-powered research system that combines multiple specialized agents to generate high-quality research reports from a single query.

Built with Streamlit, LangChain, Groq, and Tavily.

</div>

---

## ✨ Overview

The Multi-Agent Research System simulates a professional research workflow through a sequence of specialized AI agents.

Instead of relying on a single LLM response, the system divides the research process into multiple stages:

1. 🔍 Search for relevant sources
2. 📖 Read and extract information
3. ✍️ Generate a structured report
4. 🧠 Critique and evaluate the output

This approach produces more accurate, organized, and reliable research reports.

---

## 🚀 Features

### 🔍 Agent 1: Search Agent

* Intelligent web search using Tavily
* Finds relevant and up-to-date sources
* Optimized for research-focused queries

### 📖 Agent 2: Reader Agent

* Scrapes web pages automatically
* Extracts meaningful content
* Removes unnecessary noise from sources

### ✍️ Agent 3: Writer Chain

* Generates professional research reports
* Creates structured sections and summaries
* Produces clean Markdown output

### 🧠 Agent 4: Critic Agent

* Reviews report quality
* Identifies missing information
* Provides constructive feedback

### 🎨 User Experience

* Modern Streamlit interface
* Real-time pipeline progress tracking
* Download reports as Markdown files
* Fast responses powered by Groq
* Clean and intuitive workflow

---

## 🏗️ System Architecture

```text
User Query
    │
    ▼
🔍 Search Agent
    │
    ▼
📖 Reader Agent
    │
    ▼
✍️ Writer Chain
    │
    ▼
🧠 Critic Agent
    │
    ▼
📄 Final Research Report
```

---

## 🛠️ Tech Stack

| Category                | Technology           |
| ----------------------- | -------------------- |
| 🎨 Frontend             | Streamlit            |
| 🤖 LLM                  | Groq (Llama 3.3 70B) |
| 🔗 Agent Framework      | LangChain            |
| 🌐 Search Engine        | Tavily               |
| 📄 Web Scraping         | BeautifulSoup4       |
| 📡 HTTP Requests        | Requests             |
| 🐍 Programming Language | Python               |

---

## 📂 Project Structure

```text
multi-agent-system/
│
├── app.py                 # Streamlit UI
├── agents.py              # Search, Reader, Writer & Critic agents
├── pipeline.py            # Workflow orchestration
├── tools.py               # Search and scraping utilities
├── requirements.txt       # Dependencies
├── .env.example           # Environment variables template
├── README.md
├── LICENSE
├── .gitignore
│
└── attachments/
    ├── screenshots/
    └── development-files/
```

---

## ⚡ Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/V-3-3-R/multi-agent-system.git
cd multi-agent-system
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file:

#### Windows

```bash
copy .env.example .env
```

#### macOS / Linux

```bash
cp .env.example .env
```

Add your API keys:

```env
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
```

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

Open your browser and start researching. 🚀

---

## 💡 Example Use Cases

### 🎓 Academic Research

Generate structured reports for assignments and research papers.

### 📈 Market Analysis

Analyze industries, competitors, and emerging trends.

### 🏢 Business Research

Gather insights on companies, technologies, and markets.

### 🔬 Technical Exploration

Research AI, Machine Learning, Software Engineering, and more.

### 📚 Literature Reviews

Collect and summarize information from multiple sources.

---

## 📸 Screenshots

> Add application screenshots here.

```md
![Dashboard](attachments/screenshots/dashboard.png)

![Research Pipeline](attachments/screenshots/pipeline.png)

![Generated Report](attachments/screenshots/report.png)
```

---

## 🌟 Why Multi-Agent Systems?

Traditional AI systems rely on a single model response.

This project separates responsibilities among specialized agents:

| Agent           | Responsibility                     |
| --------------- | ---------------------------------- |
| 🔍 Search Agent | Finds relevant sources             |
| 📖 Reader Agent | Extracts and processes information |
| ✍️ Writer Agent | Creates the research report        |
| 🧠 Critic Agent | Evaluates report quality           |

This results in:

* Better research quality
* Improved organization
* Reduced hallucinations
* More reliable outputs

---

## 🔮 Future Improvements

* 📄 PDF Export
* 📚 Automatic Citations
* 🧠 Memory-Enabled Agents
* 🔄 Iterative Research Loops
* 🌍 Multi-Language Support
* 📊 Research Analytics Dashboard
* 🤖 Additional Specialized Agents

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

See the `LICENSE` file for additional information.

---

## ⭐ Support the Project

If you found this project useful:

🌟 Star the repository

🍴 Fork the project

📢 Share it with others

Your support helps improve and grow the project.

---

<div align="center">

### 🚀 Built with Streamlit, LangChain, Groq & Python

⭐ If you like the project, don't forget to leave a star!

</div>
