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
5. [How to Run the Project](#how-to-run-the-project)
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

## How to Run the Project

To run the Fake News Source Credibility Scoring project, follow these steps:

1. Install Dependencies:
   Ensure you have installed all required libraries by running the following command in the project directory:

    `pip install -r requirements.txt`

2. Prepare the Dataset:

    - Download the dataset from [Kaggle: Fake and Real News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset).
    - Alternatively, you can scrape articles using the built-in scraping functionality (ensure you comply with the terms of use of the websites you're scraping).

3. Run the Jupyter Notebook:
   Open the Jupyter notebook provided in the repository (project.ipynb) to train and test the models. You can run it by executing:

    `jupyter notebook project.ipynb`

    This will launch the notebook interface where you can interactively execute cells to see the project pipeline, from data preprocessing to model evaluation.

4. Running the Python Script:
   If you prefer to run the project via a Python script (if provided), you can execute it by running:

    `python main.py`

5. Review Results:
   After running the notebook or script, results such as model accuracy, precision, recall, and credibility scores will be displayed.

6. Customizations:
   You can modify the dataset, change the models, or adjust the hyperparameters directly in the Jupyter notebook to suit your needs.

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

ª .gitignore
ª EDA.ipynb
ª hierarchy.txt
ª part1.csv
ª part2.csv
ª part3.csv
ª processed_data.csv
ª README.md
ª requirements.txt
ª  
+---model_experiements
ª BERT.ipynb
ª CNN.ipynb
ª DistilBERT.ipynb
ª LSTM.ipynb
ª LSTM_working.ipynb
ª RNN.ipynb
ª SimpleNN.ipynb
ª SVM.ipynb
ª  
+---processing_experiments
ª booster_words.ipynb
ª count_vectoriser.ipynb
ª lemmatisation.ipynb
ª stemming.ipynb
ª  
+---web scraping
ª scraped_articles.csv
ª scraped_data_preprocessing_final.ipynb
ª test_news_scraper.py
ª trafilatura example.py
ª trafilatura scraper.py
ª trafilatura scraper_final.py
ª  
 +---reliable websites
ª ap_articles.csv
ª ap_scraper.py
ª bbc_articles.csv
ª bbc_scraper.py
ª cnn_articles.csv
ª cnn_scraper.py
ª guardian_articles.csv
ª guardian_scraper.py
ª npr_articles.csv
ª npr_scraper.py
ª  
 +---test_websites
ª ap_articles_1.csv
ª bbc_articles_1.csv
ª breitbart_articles_1.csv
ª cnn_articles_1.csv
ª daily_caller_articles_1.csv
ª guardian_articles_1.csv
ª naturalnews_articles_1.csv
ª newsmax_articles_1.csv
ª npr_articles_1.csv
ª zerohedge_articles_1.csv
ª  
 +---unreliable websites
ª breitbart_articles.csv
ª breitbart_scraper.py
ª dailycaller_articles.csv
ª dailycaller_scraper.py
ª naturalnews_articles.csv
ª naturalnews_scraper.py
ª newsmax_articles.csv
ª newsmax_scraper.py
ª nypost_scraper.py
ª zerohedge_articles.csv
ª zerohedge_scraper.py
ª  
 +---**pycache**
final_news_scraper.cpython-312.pyc
