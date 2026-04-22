
#importing extensions
import streamlit as st

#creating app title
st.title('Welcome to PizzaHub🍕',text_alignment='center')

#app slogan
st.subheader('The best italian in town! Now serving pizza, pasta and cold drinks')
st.image("D:\code camp\day\images\hero.jpg")
st.divider()


st.set_page_config(layout="wide")
st.title("Restaurant Dashboard")


col1, col2 = st.columns(2,border=True)
with col1:
   
        st.subheader("🍽️ Hungry?")
        st.write("Browse our delicious selection of pizzas, pastas, and drinks.")
        
        if st.button("Explore Menu", use_container_width=True):
            st.switch_page('pages/menu.py')
            

with col2:
    
        st.subheader("✨ Need help?")
        st.write("Talk to our AI assistant to get nutritional facts and recommendations.")
        
        if st.button("Chat with AI", use_container_width=True):
           
            st.switch_page('pages/chatbot.py')

col3, col4 = st.columns(2)

with col3:
    if st.button("Sign In 🔐", use_container_width=True):
        st.switch_page("pages/signin.py")

with col4:
    if st.button("Sign Up ✍️", use_container_width=True):
        st.switch_page("pages/signup.py")
