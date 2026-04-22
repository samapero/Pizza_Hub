import streamlit as st

home_page = st.Page(
    page='pages/home.py',
    title='Home Page',
    icon='🏡',
    default=True
)

chatbot_page = st.Page(
    page='pages/chatbot.py',
    title='Chatbot',
    icon='🤖'
)

menu_page = st.Page(
    page='pages/menu.py',
    title='Menu Page',
    icon='🍔'
)

signin_page = st.Page(
    page='pages/signin.py',
    title='Signin Page',
      icon='🔑'
)

signup_page = st.Page(
    page='pages/signup.py',
    title='Signup Page',
    icon='📝'
)


pg= st.navigation([home_page, chatbot_page, menu_page, signin_page, signup_page],position='top')

pg.run()









