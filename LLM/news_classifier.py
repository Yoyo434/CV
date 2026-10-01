import requests
from config import HF_API_KEY

MODEL_ID="facebook/bart-large-mnli"
API_URL=f"https://router.huggingface.co/hf-interface/models/{MODEL_ID}"
HEADERS={"Authorization": f"Bearer {HF_API_KEY}"}
TOPICS=["Sports","Technology","Business","Politics","Health"]

def ask_hf(headline:str):
    payload={"inputs": headline, "parameters": {"candidate_labels": TOPICS}}
    r=requests.post(API_URL, headers=HEADERS, json=payload,timeout=30)
    if not r.ok:
        raise RuntimeError(f"HF error {r.status_code}: {r.text}")
    return r.json()
