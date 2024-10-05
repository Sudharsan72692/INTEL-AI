import nltk
import os
import streamlit as st
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from main import read_image
from bert import data_summary
import google.generativeai as genai

# Specify the path to your nltk_data directory
nltk.data.path.append("C:/Users/sudha/nltk_data")  # Change this to your actual path

# Download the necessary resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Set up Google Generative AI API credentials
genai.configure(api_key='Your_API_Key')

# Function to get response from Google Gemini AI
def get_gemini_response(user_input, history=[]):
    generation_config = {
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 1000,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        system_instruction="You are an expert in food ingredients, providing clear and concise advice to users.And you are not supposed to answer questions like following I understand you're asking about salt intake for people over 80, but I'm unable to provide specific medical advice, and that includes dietary recommendations. Individual Needs Vary: Salt intake recommendations depend on many factors like overall health, medications, and existing health conditions, all of which are unique to each person, especially in their 80s and beyond. You should only reply in 10 sentence not more than that."
    )
    
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(user_input)
    return response.text

# Main function to handle Streamlit UI and chatbot logic
def main():
    st.sidebar.image('https://th.bing.com/th/id/OIP.B4mhnzvK_a7ltCfTxx5iKQHaE8?rs=1&pid=ImgDetMain', use_column_width=False)
    st.sidebar.markdown("> Made by [*Beta*]( )")
    
    user_color = '#000000'
    title_webapp = "NutrioBot"
    image_link = "https://th.bing.com/th/id/OIP.w9gXyd2xzaca3OyruTqhrgHaEJ?rs=1&pid=ImgDetMain"
    
    html_temp = f"""
                <div style="background-color:{user_color};padding:12px">
                <h1 style="color:white;text-align:center;">{title_webapp}
                <img src = "{image_link}" align="right" width=300px ></h1>
                </div>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    st.sidebar.header("About")
    st.sidebar.info("Our application combines the power of artificial intelligence and nutrition science to provide users with comprehensive information about the ingredients in their food products.By generating detailed reports on each ingredient, including their benefits, side effects, and overall impact, our application empowers users to make informed decisions about the foods they consume. Whether it's understanding the nutritional value of a snack or uncovering potential allergens, our platform equips users with the knowledge they need to prioritize their health and well-being.")
    st.sidebar.info("By bridging the gap between complex ingredient labels and consumer understanding, our application revolutionizes the way people engage with packaged foods, promoting transparency, health-consciousness, and informed decision-making. With our platform, users can navigate the modern food landscape with confidence, knowing they have access to accurate, personalized information about the products they consume.")
    
    st.title("Chat with Bot")
    
    execute_program = st.sidebar.checkbox("Execute program")

    # Show the chatbot regardless of whether the program is executed
    st.write("Bot: Hello! I'm your chatbot. Ask me anything about food ingredients.")
    
    user_input = st.text_input("You: ")

    if user_input.lower() == 'exit':
        st.write("Bot: Goodbye! Have a great day.")
    else:
        if user_input:
            history = []
            response = get_gemini_response(user_input, history)
            st.write("Bot:", response)

    # OCR and file upload section always visible
    st.markdown("<h2 style='text-align: center; color: blue;'> OCR Extraction</h2>", unsafe_allow_html=True)
    
    inp = st.file_uploader("UPLOAD THE FILE:")

    if inp is not None:
        a = read_image(inp.name)
        predicted_attributes_list = data_summary(a)
        menu = [item['Ingredient'] for item in predicted_attributes_list]
        selected_ingredient = st.sidebar.selectbox("Select Ingredient", menu)
        selected_ingredient_dict = next((item for item in predicted_attributes_list if item['Ingredient'] == selected_ingredient), None)
        
        if selected_ingredient_dict is not None:
            # Only display the table, no plain text output
            st.markdown("<br>", unsafe_allow_html=True)

            # Display the details in a table-like structure using HTML
            st.markdown(f"<span style='font-weight: bold;'>Details for:</span> {selected_ingredient_dict['Ingredient']}", unsafe_allow_html=True)
            st.markdown("<table>", unsafe_allow_html=True)
            for key, value in selected_ingredient_dict.items():
                st.markdown(f"<tr><td><span style='font-weight: bold;'>{key}:</span></td><td>{value}</td></tr>", unsafe_allow_html=True)
            st.markdown("</table>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
