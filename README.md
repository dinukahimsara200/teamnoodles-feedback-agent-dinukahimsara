```markdown
# SteamNoodles Feedback Agent – Dinuka Himsara  
**Repo:** `https://github.com/dinukahimsara/steamnoodles-feedback-agent-dinukahimsara`

## Overview
Two LangChain + Groq agents for SteamNoodles restaurant chain:

1. **Agent1** – auto-replies to single reviews  
2. **Agent2** – plots daily sentiment for **any** user-supplied date range

## Quick Start
```bash
git clone https://github.com/dinukahimsara/steamnoodles-feedback-agent-dinukahimsara.git
cd steamnoodles-feedback-agent-dinukahimsara
pip install -r requirements.txt
echo "GROQ_API_KEY=your_key" > .env
python main.py
```
- Follow the **on-screen prompt** for the date range.  
- Plot saved as `sentiment_plot.png`.

## Dataset
Keep only three columns in `reviews.csv`:
```
rating_review,review_full,date
```
Example row:  
```
5,"Awesome ramen","8-Oct-20"
```

## Manual Use
```python
from agent1 import generate_response
print(generate_response("Food was amazing!"))

from agent2 import plot_sentiment
plot_sentiment("2020-09-01 to 2020-10-08")
```

## Author
Dinuka Himsara – University of Moratuwa – 2025  
Submitted 15 Aug 2025 ✅
```