from google import genai

def generate_brand_tone_content(api_key, brand_description, tone, language, model="gemini-2.0-flash"):
    client = genai.Client(api_key=api_key)

    prompt = (
        f"You are a professional brand copywriter.\n"
        f"Generate creative content in a {tone} tone "
        f"for a brand with the following description: {brand_description}.\n"
        f"Output must be in {language}."
    )

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    return response.text