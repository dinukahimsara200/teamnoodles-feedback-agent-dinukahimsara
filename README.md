
# SteamNoodles Feedback Agent - Dinuka Himsara

**Repo:** `https://github.com/dinukahimsara/steamnoodles-feedback-agent-dinukahimsara`  
Two-agent **LangChain + Groq (Llama-3-70B)** Python framework for the SteamNoodles restaurant chain:

| Agent | Function |
|-------|----------|
| 1 | Reads a customer review and replies politely in one sentence. |
| 2 | Generates a daily sentiment line chart for a given date range. |

---

## 📂 Structure
```

├── agent1.py        # Feedback response
├── agent2.py        # Sentiment plot
├── main.py          # Demo runner
├── requirements.txt
├── .env.example     # API key template
├── reviews.csv      # Your dataset

````

---

## ⚡ Setup

```bash
git clone https://github.com/dinukahimsara/steamnoodles-feedback-agent-dinukahimsara.git
cd steamnoodles-feedback-agent-dinukahimsara
pip install -r requirements.txt
cp .env.example .env   # Add GROQ_API_KEY
````

**Dataset:** `reviews.csv` must include a `date` column in `8-Oct-20` format.

---

## ▶ Quick Start

```bash
python main.py
```

Output:

```
--- Agent 1 ---
Review: ...
Response: ...

--- Agent 2 ---
Plot saved as 'sentiment_plot.png'
```

---

## 💻 Usage

```python
from agent1 import generate_response
print(generate_response("Food was amazing!"))

from agent2 import plot_sentiment
plot_sentiment("2020-09-01 to 2020-10-08")
plot_sentiment("last 30 days")
```

---

**Author:** Dinuka Himsara, University of Moratuwa (2025)

**Deadline:** 15 Aug 2025 
