import streamlit as st
from st_functions import st_button, load_css
import numpy as np
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Define styles for prediction elements
prediction_container_style = """
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
    padding: 20px;
    background-color: #f5f5f5;
"""

prediction_text_style = """
    font-size: 24px;
    font-weight: bold;
    color: #333;
"""

load_css()
col1, col2, col3 = st.columns(3)
st.header('Abusive Comment Detector using :blue[_mBERT_] :computer:')

st.info('This model is a Finetuned version of mBERT on the Abusive Comment Dataset. The dataset contains comments in native Telugu script, Code-Mixed Telugu and Telugu-English Comments. More description can be found in my Github Repo. Enter a comment in the text box below and click on Analyze, then the model will give Prediction as Abusive or Not Abusive.')

@st.cache_data
def get_model():
    tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
    model = BertForSequenceClassification.from_pretrained("revanth-reddy-9/Abusive_Comment_Detector_mBERT")
    return tokenizer, model

tokenizer, model = get_model()

user_input = st.text_area('Enter Text to Analyze')
button = st.button("Analyze")

d = {
    0: 'Abusive',
    1: 'Not Abusive'
}

if user_input and button:
    test_sample = tokenizer([user_input], padding=True, truncation=True, max_length=512, return_tensors='pt')
    output = model(**test_sample)
    #st.write("Logits: ", output.logits)
    y_pred = np.argmax(output.logits.detach().numpy(), axis=1)
    prediction_text = f"Prediction: {d[y_pred[0]]}"
    st.markdown(f"<h2 style='{prediction_text_style}'>{prediction_text}</h2>", unsafe_allow_html=True)

icon_size = 24

st_button('linkedin', 'https://www.linkedin.com/in/revanth-reddy-pingala/', '   Connect with me on LinkedIn', icon_size)
st_button('github', 'https://github.com/Revanth-Reddy-Pingala', '   Check my Github Profile', icon_size)
st_button('medium', 'https://rrdatadiaries.blogspot.com/', '   Read my Blogs', icon_size)
st_button('instagram', 'https://www.instagram.com/revanth_reddy.1459/', '   Follow me on Instagram', icon_size)
