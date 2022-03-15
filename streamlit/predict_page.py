import streamlit as st
import pickle
import pandas as pd
import string
import nltk

def load_model():
    with open('fake_news_classifier.pkl', 'rb') as file:
         data = pickle.load(file)
    return data

data = load_model()

class Text:
    def punctuation_removal(self,text):
        all_list = [char for char in text if char not in string.punctuation]
        clean_str = ''.join(all_list)
        return clean_str
    
    def remove_numbers(self,text):
        numbers='0123456789'
        all_list = [char for char in text if char not in numbers]
        clean_str = ''.join(all_list)
        return clean_str
    
    def remove_stopwords(self,text):
        nltk.download('stopwords')
        from nltk.corpus import stopwords
        stop = stopwords.words('english')
        clean_str=''.join([word for word in text.split() if word not in (stop)])
        return clean_str

    def stemSentence(self,text):
        from nltk.stem.porter import PorterStemmer
        porter=PorterStemmer()
        clean_str=' '.join([porter.stem(word) for word in text.split()])
        return clean_str

    def preprocess(self,text):
        text=text.lower()
        text=self.punctuation_removal(text)
        text=self.remove_numbers(text)
        text=self.remove_stopwords(text)
        text=self.stemSentence(text)
        return text

def show_predict_page():

    cols=st.columns([2,4,2])
    cols[1].image("icon.png",width=250)
    cols=st.columns([2,8,2])
    cols[1].title("|....... Bogus Text  ......|")
    st.write("")

    st.subheader("Enter the news :")
    text=st.text_area("",placeholder="Type or paste the news to be verified...",height=250)

    st.write("")
    cols = st.columns([2,1,2])
    ok = cols[1].button("Detect")

    if ok:
        if len(text) !=0:
            obj=Text()
            processed_text=obj.preprocess(text)
            prediction=data['model'].predict([processed_text])[0]
            cols=st.columns([1,3,1])
            if prediction==0:
                cols[1].write('''# The news is fake !!''')
            else:
                cols[1].write('''# The news is true !!''')
        else:
            st.warning("No text found. Try again !!")

    