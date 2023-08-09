from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
from sentence_transformers import SentenceTransformer, util
from huggingface_hub import hf_hub_download
import os
import pickle
import pandas as pd

app = FastAPI()

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers,
)

embeddings = pickle.load("meme-embeddings.pkl", "rb")
df = 

@app.get("/")
async def root():
    return {"message": "Welcome to Semantic Search for Memes!"}


@app.post("/retrieve")
async def get_net_image_prediction(prompt: str = ""):
    if image_link == "":
        return {"message": "No image link provided"}
    pred, idx, prob = learn.predict(PILImage.create(urlopen(image_link)))
    return {"predcition": pred, "probability": float(prob[0])}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    run(app, host="0.0.0.0", port=port)