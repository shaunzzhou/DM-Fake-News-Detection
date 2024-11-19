# From Detection to Credibility: A Machine Learning Framework for Assessing News Source Reliability

## Project Overview

This project focuses on assessing the credibility of news sources by analyzing their articles and determining whether the content is real or fake. Using natural language processing (NLP) techniques and machine learning algorithms, the project assigns a credibility score to different news websites and ranks them based on this score.

### Objectives:

-   Utilise a myriad of classification models to determine the best performing model.
-   Scrape news articles from various websites.
-   Use NLP techniques to analyze and classify news as real or fake.
-   Assign credibility scores to news sources based on classification results.
-   Rank news sources by credibility for better public information access.

---

## Table of Contents

1. [Project Setup](#project-setup)
2. [Installation](#installation)
3. [Dataset](#dataset)
4. [Data Collection](#data-collection)
5. [Description of ipynb Notebooks](#notebooks)
6. [Contributors](#contributors)

---

## Project Setup

Before running the project, ensure you have the required libraries installed. The project is based on Python and utilizes several NLP and machine learning libraries.

---

## Installation

To set up the environment, follow these steps:

1.  Clone the repository:

        git clone https://github.com/your-repo/fake-news-detection.git

2.  Navigate to the project directory:

        cd fake-news-detection

3.  Create a virtual environment:

        python -m venv venv

    source venv/bin/activate # For Linux/macOS
    venv\Scripts\activate # For Windows

4.  Install the required dependencies:

        pip install -r requirements.txt

The requirements.txt file includes the following packages:

-   pandas
-   numpy
-   scipy
-   tqdm
-   matplotlib
-   seaborn
-   langdetect
-   langid
-   nltk
-   spacy
-   wordcloud
-   scikit-learn
-   tensorflow
-   torch
-   transformers
-   tokenizers
-   keras
-   gensim

---

## Dataset

The project uses a labelled dataset of real and fake news articles, which can be downloaded from Kaggle. This dataset provides the foundational data for training the models.

-   **Dataset link:** [Kaggle: Fake and Real News Dataset](https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification)

## Data Collection

This project uses news articles scraped from various sources, including reliable and unreliable websites. The structure of the dataset is as follows:

-   source_name: Name of the source where article is found
-   url: The URL of the article.
-   title: The title of the article.
-   content: The main text of the article.

---

## Description of `ipynb` notebooks

── model_experiments
│ ├── `BERT.ipynb`
│ ├── `CNN.ipynb`
│ ├── `DistilBERT.ipynb`
│ ├── `LSTM.ipynb`
│ ├── `RNN.ipynb`
│ ├── `SimpleNN.ipynb`
│ ├── `SVM.ipynb`
├── processing_experiments
│ ├── `booster_words.ipynb`
│ ├── `count_vectoriser.ipynb`
│ ├── `lemmatisation.ipynb`
│ ├── `stemming.ipynb`
├── web_scraping
│ ├── `scraped_data_preprocessing.ipynb`
├── `EDA.ipynb`

---

## Contributors

This project was developed by:

-   Shaun Zhou
    [GitHub](https://github.com/shaunzzhou)
-   Darius Ng
    [GitHub](https://github.com/dariusnggg)
-   Gabriel Chua
    [GitHub](https://github.com/deseyebags)
-   Ryan Lee
    [GitHub](https://github.com/ryan99324)
-   Abhay
    [GitHub](https://github.com/Helliad)
-   Sakthivel
    [GitHub](https://github.com/sakthivelg2022)
-   See Jae
    [GitHub](https://github.com/seejaee)

---
