# NutrioBot

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
- [Contributing](#contributing)
- [License](#license)

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
