# NutrioBot - Assisting people with packed food items.
![Nutrio Bot](https://github.com/user-attachments/assets/a1e58598-4fec-4cea-9175-a7d7beb50094)


**NutrioBot** is an AI-powered web application designed to help users understand the ingredients in their food products. The app provides comprehensive information such as the benefits, side effects, allergens, dietary needs, and much more, empowering users to make informed decisions about their food consumption. NutrioBot utilizes advanced technologies like OCR for ingredient extraction, BERT-based NLP for attribute prediction, and integrates the Google Gemini AI API for chatbot functionality.

## Features

- **Ingredient Analysis**: Scan food product ingredients using OCR and get detailed reports on benefits, side effects, and allergens.
- **Interactive Chatbot**: Ask NutrioBot anything about food ingredients. The bot provides expert advice on food ingredients using Google Gemini AI API.
- **Comprehensive Reports**: NutrioBot generates detailed summaries including dietary needs, preferences, and potential health impacts for each ingredient.
- **AI-Powered**: Uses BERT-based NLP models to predict attributes related to food ingredients.
- **Streamlit UI**: A user-friendly interface for interaction with the bot and displaying ingredient information.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)


## Installation

### Prerequisites
- Python 3.8 or above
- NLTK
- PaddleOCR
- Google Gemini AI API key
- Streamlit

### Setting up the environment
1. Clone the repository:
    ```bash
    git clone https://github.com/Sudharsan72692/INTEL-AI
    cd nutriobot
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download NLTK resources:
    ```bash
    python nltk_script.py
    ```

4. Set up the Google Gemini AI API:
    - Replace the `api_key` in the code with your Google Gemini AI API key.

### Running the application
To start the NutrioBot application, run:
```bash
streamlit run streamlit_final.py
```

## Usage
Chatbot Interaction
Open the app in your browser and enter any questions related to food ingredients in the chatbot section.
NutrioBot will provide concise responses based on the input.
OCR and Ingredient Analysis
Upload an image of a food product label to extract ingredient names.
The app will generate a detailed analysis of the ingredients, including potential allergens, side effects, and health impacts.

## Project Structure
NutrioBot/
│
├── bert.py              # BERT model for ingredient analysis
├── nltk_script.py       # NLTK resource setup
├── main.py              # OCR functionality using PaddleOCR
├── streamlit_final.py   # Main Streamlit app with chatbot and OCR
├── requirements.txt     # Required Python libraries
├── README.md            # Project documentation
└── ...


## Technologies Used
Technologies Used
Streamlit: For building the user interface.
Google Gemini AI API: For generating chatbot responses.
PaddleOCR: For Optical Character Recognition (OCR) of ingredient labels.
BERT: For predicting attributes and providing information on food ingredients.
NLTK: For text processing and tokenization.


## Website UI:
![nutriobot home](https://github.com/user-attachments/assets/9db669ec-0084-4e3d-a1dd-0f79a1458fc9)


## Demo Video and Test Images
https://github.com/user-attachments/assets/0eb7bb97-3edb-477d-8748-66eaf9ce12d1




![chocolate-back](https://github.com/user-attachments/assets/4d04187f-0eb4-40cf-bb64-3217d53d49b0)

## ChatBot Output
![chatbot](https://github.com/user-attachments/assets/2a930544-8824-494c-ae8c-1ab358603fdd)
