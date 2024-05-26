import streamlit as st
import openai
import os

# Setup OpenAI API Key
openai.api_key = "sk-proj-zVeLpzlE7e8tq8FZDD7nT3BlbkFJMKVeAeIwRIPf5L2rtcsA"

# Function to generate text using GPT-3
def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Multi-Level Prompting Logic
def multi_level_prompting():
    st.title("Story Generator")
    
    # Level 1 Prompt
    genre = st.selectbox("Choose a genre:", ["Fantasy", "Science Fiction", "Mystery", "Romance"])
    
    # Level 2 Prompt based on Level 1
    if genre:
        style = st.selectbox(f"Choose a style for your {genre} story:", ["Narrative", "Dialogue", "Descriptive"])
        
        # Final Prompt
        if style:
            user_prompt = st.text_input(f"Provide a brief idea for your {style} {genre} story:")
            
            if user_prompt:
                full_prompt = f"Write a {style} {genre} story about: {user_prompt}"
                generated_text = generate_text(full_prompt)
                st.text_area("Generated Story", value=generated_text, height=300)

# Streamlit App Execution
if __name__ == "__main__":
    multi_level_prompting()

