# SteamNoodles Feedback Agent -- Dinuka Himsara  
**Repo:** `https://github.com/dinukahimsara/steamnoodles-feedback-agent-dinukahimsara`

## Overview
Two LangChain + Groq agents for SteamNoodles restaurant chain:

1. **Agent1** – auto-replies to single reviews  
2. **Agent2** – plots daily sentiment for **any** user-supplied date range

## Setup & Run

```bash
git clone https://github.com/dinukahimsara/steamnoodles-feedback-agent-dinukahimsara.git
cd steamnoodles-feedback-agent-dinukahimsara
pip install -r requirements.txt
python main.py
```

## Testing

* **Agent 1:** Enter any review text when prompted, get a polite one-sentence reply.
* **Agent 2:** Uses a `reviews.csv` file in the project root.
  I downloaded [Madrid\_reviews.csv](https://www.kaggle.com/datasets/inigolopezrioboo/a-tripadvisor-dataset-for-nlp-tasks?resource=download&select=Madrid_reviews.csv) from Kaggle and modified it for testing.
  Since the dataset is static, inputs like `last 7 days` will not work — use fixed date ranges instead.

## Sample

| Agent | Input                                             | Output Example                                                                  |
| ----- | ------------------------------------------------- | ------------------------------------------------------------------------------- |
| 1     | `Great cocktails and Javier was really friendly.` | `Thank you for your kind words! We’re delighted you enjoyed your time with us.` |
| 2     | `2019-09-01 to 2020-09-01`                        | Displays sentiment trend plot for that range.                                   |


