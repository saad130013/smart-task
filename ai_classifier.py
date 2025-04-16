
from transformers import pipeline

# نموذج HuggingFace مسبق التدريب
classifier = pipeline("text-classification", model="distilbert-base-uncased", top_k=1)

def classify_task_text(task_description):
    result = classifier(task_description)
    label = result[0]['label']
    score = result[0]['score']
    return label, score
