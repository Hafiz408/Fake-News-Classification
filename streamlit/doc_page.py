import streamlit as st
# import webbrowser



# url = 'https://github.com/Hafiz408/My-Doctor'

def doc():
    st.balloons()
    st.title("Hello guys !!")
    st.write("")
    st.write("""
    #
    ##### " BogusText " is a web app created using streamlit library in python. It aims to detect fake news in articles with the help of the Natural Language ToolKit (NLTK) for preprocessing. 

    #
    ##### Further, it includes some insights and visuals about the articles.
    #
    """)

    cols=st.columns([3,2])
    cols[0].write("""
    Click the below link, for the Github repo.
    https://github.com/Hafiz408/Fake-News-Classification
    """)
    # github = cols[1].button("Here.")
    # if github:
    #     webbrowser.open_new_tab(url)
          
        