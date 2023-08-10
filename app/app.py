from sentence_transformers import SentenceTransformer, util
from huggingface_hub import hf_hub_download
import os
import pickle
import pandas as pd
from PIL import Image
import requests
from io import BytesIO
import gradio as gr

pd.options.mode.chained_assignment = None  # Turn off SettingWithCopyWarning

embeddings = pickle.load(open(hf_hub_download("bhavyagiri/semantic-memes", repo_type="dataset", filename="meme-embeddings.pkl"), "rb"))
df = pd.read_csv(hf_hub_download("bhavyagiri/semantic-memes", repo_type="dataset", filename="input.csv"))

model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

def generate_memes(prompt):
    prompt_embedding = model.encode(prompt, convert_to_tensor=True)
    hits = util.semantic_search(prompt_embedding, embeddings, top_k=6)
    hits = pd.DataFrame(hits[0], columns=['corpus_id', 'score'])
    desired_ids = hits["corpus_id"]
    filtered_df = df.loc[df['id'].isin(desired_ids)]
    filtered_list = list(filtered_df["url"]) 
    images = [Image.open(BytesIO(requests.get(img).content)) for img in filtered_list]
    return (
       images
    )
input_textbox = gr.inputs.Textbox(lines=1, label="Search something cool")
output_gallery = gr.Gallery(
            label="Retrieved Memes", show_label=False, elem_id="gallery"
        ).style(columns=[3], rows=[2], object_fit="contain", height="auto")
title = "Semantic Search for Memes"
description = "Search Memes from small dataset of 6k memes"
examples = ['Spiderman giving lecture', 'Some super hero']
interpretation='default'
enable_queue=True

iface = gr.Interface(fn=generate_memes, inputs=input_textbox, outputs=output_gallery,examples=examples,title=title,description=description,interpretation=interpretation,enable_queue=enable_queue)
iface.launch(inline=False)
