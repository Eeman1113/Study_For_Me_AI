import streamlit as st
import os 


# st.title('Ask Me Anything 📚')
st.markdown("<h1 style='text-align: center; color: white;'>Ask Me Anything 🎓</h1>", unsafe_allow_html=True)
st.markdown('')
st.markdown('')

st.session_state['new']=True
# if st.session_state.new==True:
#     os.system('!pip install torch==1.10.2+cu113 torchvision==0.11.3+cu113 torchaudio===0.10.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html')
#     os.system('!pip install transformers')
#     st.session_state.new=False 

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline


# creating the q/a pipeline
nlp = pipeline('question-answering', model='deepset/roberta-base-squad2', tokenizer='deepset/roberta-base-squad2')

text = st.text_area('Gimme Stuff To Study 📚')

st.markdown('---')
ques=st.text_input('Ask Me Anything From The Information You Have Given')

#forming a question directory 
ques_dict = {
                'question':ques, 
                'context':text
               }

butt = st.button('Ask 🤷🏻')

if butt==True:
    results = nlp(ques_dict)
    st.markdown('---')
    st.subheader('Here Is Your Answer')
    st.success(results['answer'])
    st.balloons()

