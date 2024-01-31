
# Abusive_Comment_Detector_BERT

## Problem statement
- This project aims to identify and filter out content that is offensive, harmful, or disrespectful to provide safer online environment. 

- With the rapid growth of online platforms and social media, there is an increasing need to address critical natural language processing task of Abusive Comment Detection in Low Resource Languages like Telugu.

## Demo
- [Streamlit Abusive Comment Detector App](https://abusive-comment-detector.streamlit.app)
  
- Before Prediction

<img width="1452" alt="Screenshot 2024-01-31 at 8 32 02 PM" src="https://github.com/Revanth-Reddy-Pingala/Abusive_Comment_Detector_BERT/assets/125516124/ab2742f5-0995-4e76-9866-4fc87ae3f92d">

- After Prediction

<img width="1452" alt="Screenshot 2024-01-31 at 8 42 34 PM" src="https://github.com/Revanth-Reddy-Pingala/Abusive_Comment_Detector_BERT/assets/125516124/bb094e98-358b-4d86-98c3-1defc90f4716">


## Run Locally

Clone the project

```bash
  git clone https://github.com/Revanth-Reddy-Pingala/Abusive_Comment_Detector_BERT
```

Go to the project directory

```bash
  cd my-project
```

After setting up environment and installing packages using requirements.txt, Run the following command to Deploy app Locally

```bash
  streamlit run ./app.py
```
## Sequence of steps followed until Deployment
- Github and Code Set Up.
- Text Preprocessing.
- Exploratory Data Analysis.
- Model Hyper Parameters tuning.
- Finetuning the BERT model using Google Colab's GPU.
- Saving the Finetuned BERT model locally.
- Pushing the saved model to Hugging Face.
- Development of web app using Streamlit.
- Getting the saved model using transformers from Hugging Face.
- Deploying the app to Streamlit Community Cloud.

## Dataset Description
- This project provided in this repository is just a sample version of my Main Project at Central University of Tamil Nadu.

- The dataset is a real time dataset from Research paper using SnapChat data and another dataset from Codalab Competition. The final dataset used is a combination of both datasets.

- The Abusive Comment Dataset contains Comments in native Telugu script, Code-Mixed(combination of Telugu and English in the same comment, telugu comments written in English alphabet) Telugu and combination of Telugu-English Comments. 

## Dataset information
- Data : Comments present in native Telugu, code-mixed Telugu and Telugu-English.
- Sentiment : Abusive or Not Abusive

## Data Checks Performed
- Missing values
- Duplicates
- data type
- Count of Abusive class and Not Abusive class

## Exploratory Data Analysis (EDA)
- More Description can be found in the files of notebook folder.
## Inference from Plots
- This is a balanced Dataset. So we don't have to perform dataset balancing tasks.
## Models used for Training in this Repo
- BERT
## Models used in my Main Project
- mBERT
- XLMRoBERTa

## Evaluation metrics after Training
- loss
- accuracy
- precision
- recall
- f1 score

## Accuracy for the Models
- BERT - 69% (sample dataset of 1k comments)
- mBERT - 86% (Entire dataset of 34.5k Comments)
- XLMRoBERTa - 89% (Entire dataset of 34.5k Comments)

## Why sample dataset in this Repo for Deployment
- Due to limited access of cloud RAM after Deployment.

- The finetuned mBERT and XLMRoBERTa use lot of RAM while fetching and Predicting.

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/revanth-reddy-pingala/)
[![Blogger](https://img.shields.io/badge/Blogger-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://rrdatadiaries.blogspot.com/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/revanth_reddy.1459/)
