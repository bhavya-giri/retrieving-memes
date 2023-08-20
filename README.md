retrieving-memes
==============================

Using Semantic Search to retrieve memes

[Try it out!](https://huggingface.co/spaces/bhavyagiri/retrieving-memes)

### Data

The [Orginal Dataset](https://github.com/eujhwang/meme-cap) is small dataset with 6k memes which are annotated by [OpenFlamingo-9B](https://github.com/mlfoundations/open_flamingo) and [MiniGPT4](https://github.com/Vision-CAIR/MiniGPT-4) models for their zero-shot and few-shot experiments. 

Final Dataset and Embeddings are also available on [🤗 HuggingFace](https://huggingface.co/datasets/bhavyagiri/semantic-memes)

Project Organization
------------
    ├── README.md          <- The top-level README for developers using this project.
    |
    ├── app
    │   ├── app.py               <- Gradio App
    │   ├── requirements.txt     <- Requirements for Gradio App
    |
    ├── data
    │   ├── input.csv                <- Final dataset that was used for encoding
    │   ├── meme-embeddings.pkl      <- Embedding of the memes in the dataset
    │   ├── raw_memes.json           <- Raw Dataset from meme-cap
    |   ├── string_data.csv          <- Dataset before concatenating input sequence
    │   └── required_cols.csv        <- Dataset with string columns
    │
    ├── notebooks          
    |   ├── EDA and Cleaning Data.ipynb       <- Exploring and cleaning the raw data to input.csv
    │   ├── Semantic Search.ipynb             <- Using Sentence Transformer create semantic search based on cosine similarity
    │
    └──  requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.

 ## Run Locally

Clone the project

```bash
  git clone https://github.com/bhavya-giri/retrieving-memes
```

Go to the project directory

```bash
  cd retrieving-memes
```

Install dependencies

```bash
  pip install requirements.txt
```

Start the notebook

```bash
  jupyter notebook
```
or open with Juoyter Lab

```bash
 jupyter lab
```
