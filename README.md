# Brand Tone Generator

A lightweight AI-powered assistant that generates creative, tone-specific brand content in multiple languages using Google's Gemini model.

## Features

- Generate tailored brand content (headlines, captions, CTAs)  
- Choose from multiple tone presets (Luxury, Friendly, Professional, Bold, Minimal)  
- Multilingual support (English, Russian, Spanish, French)  
- Powered by Gemini 2.0 Flash API  
- Simple Streamlit UI for quick prototyping

## Project Structure

brand-tone-generator/
├── app.py                # Streamlit UI
├── generator.py          # Gemini content generation logic
├── prompts.py            # Tone prompt templates
├── LLM_Brand_Tone_Generator.ipynb  # Jupyter project demo
├── requirements.txt
└── README.md

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/brand-tone-generator.git

cd brand-tone-generator
```

2. Install dependecies

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application

```bash
streamlit run app.py
```