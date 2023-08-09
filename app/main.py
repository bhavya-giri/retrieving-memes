from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
import torch
from sentence_transformers import SentenceTransformer, util
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


# def load_from_pkl_file(path):
#     with open(path,'rb') as f:
#         return pickle.load(f)
# embeddings = load_from_pkl_file("meme-embeddings.pkl")
with open('meme-embeddings.pkl', "rb") as fIn:
    stored_data = pickle.load(fIn)
    embeddings = stored_data
df = pd.read_csv("input.csv")
model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

def generate_memes(prompt):
    prompt_embedding = model.encode(prompt, convert_to_tensor=True)
    hits = util.semantic_search(prompt_embedding, embeddings, top_k=5)
    hits = pd.DataFrame(hits[0], columns=['corpus_id', 'score'])
    desired_ids = hits["corpus_id"]
    filtered_df = df.loc[df['id'].isin(desired_ids)]
    return (
       list(filtered_df["url"]) 
    )

@app.get("/")
async def root():
    return {"message": "Welcome to Semantic Search for Memes!"}


@app.post("/retrieve")
async def get_net_image_prediction(prompt: str = ""):
    if prompt == "":
        return {"message": "No Pompt"}
    list_memes = generate_memes(prompt)
    return {"memes": list_memes }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    run(app, host="0.0.0.0", port=port)