
---

## 🧠 `summarizer.py`
```python
from transformers import pipeline

def summarize_text(text, model_choice="bart", summary_length="medium"):
    if model_choice == "t5":
        summarizer = pipeline("summarization", model="t5-small")
    else:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    max_len = {"short": 80, "medium": 150, "detailed": 250}[summary_length]
    min_len = int(max_len / 2)

    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return summary[0]['summary_text']
