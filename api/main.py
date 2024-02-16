from fastapi import FastAPI
from transformers import pipeline



app = FastAPI()

@app.post("/api")
async def get_output(input):
    # prediction
    pipe = pipeline("text-classification", model="facebook/roberta-hate-speech-dynabench-r4-target")
    response = pipe(input)[0]
    # get scoring
    if response["label"] == "nothate":
        score = 1 - response["score"]
    else:
        score = response["score"]
    score = f"{score:.0%}"
    return score