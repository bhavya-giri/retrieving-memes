retrieving-memes
==============================

The model trained from [roberta-base](https://huggingface.co/roberta-base) on the [imdb-spoiler](https://huggingface.co/datasets/bhavyagiri/imdb-spoiler) dataset for classification.
The model was trained using `AutoModelForSequenceClassification.from_pretrained` for 3 epochs with a learning rate of 2e-5 and weight decay of 0.01.

[Check it out!](https://huggingface.co/bhavyagiri/roberta-base-finetuned-imdb-spoilers)

### Data

[imdb-spoiler](https://huggingface.co/datasets/bhavyagiri/imdb-spoiler) is a subset of a [large-dataset](https://www.kaggle.com/datasets/rmisra/imdb-spoiler-dataset) for classifying whether a movie review is a spoiler or not.

### Evaluation using the dataset validation split gives:
- F1 0.585
- Accuracy 0.474


Project Organization
------------
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── notebooks          
    |   ├── EDA and Split.ipynb       <- Exploring and split the original data in a small subset
    │   ├── Fine-Tuning.ipynb             <- Fine-tuning Roberta-base for Text-Classification
    │
    └──  requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.

 ## Run Locally

Clone the project

```bash
  git clone https://github.com/bhavya-giri/spoiler-alert
```

Go to the project directory

```bash
  cd spoiler-alert
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
