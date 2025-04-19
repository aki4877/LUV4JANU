import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(page_title="Dear Jani 💗", layout="wide")

# Function to convert image to base64
def get_image_base64(file_path):
    try:
        with open(file_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    except Exception as e:
        print(f"Error loading image {file_path}: {e}")
        return ""

# List of image paths and captions (assuming images are in root directory)
slides = [
    {"caption": "The day it all began — your smile changed everything.", "filename": "1.jpg"},
    {"caption": "Our first photo together — I knew we were something special.", "filename": "2.jpg"},
    {"caption": "Laughing like kids, loving like soulmates.", "filename": "3.jpg"},
    {"caption": "Late night talks, sleepy eyes, full hearts.", "filename": "4.jpg"},
    {"caption": "You looked at me like I was home.", "filename": "5.jpg"},
    {"caption": "A stolen kiss, forever etched in my mind.", "filename": "6.jpg"},
    {"caption": "Holding your hand felt like holding the universe.", "filename": "7.jpg"},
    {"caption": "Every second with you is a favorite memory.", "filename": "8.jpg"},
    {"caption": "You make ordinary moments feel magical.", "filename": "9.jpg"},
    {"caption": "From “I like you” to “I love you” — my favorite journey.", "filename": "10.jpg"},
    {"caption": "The way you look at me when I talk — I never felt so heard.", "filename": "11.jpg"},
    {"caption": "A thousand lifetimes wouldn’t be enough with you.", "filename": "12.jpg"},
    {"caption": "Even silence feels like love when I’m with you.", "filename": "13.jpg"},
    {"caption": "We’re not perfect, but we’re perfect for each other.", "filename": "14.jpg"},
    {"caption": "5 months down, forever to go — I love you, Janu.", "filename": "15.jpg"},
]

# Convert images to base64
for slide in slides:
    file_path = slide["filename"]  # Use filename directly from root
    if os.path.exists(file_path):
        slide["src"] = f"data:image/jpeg;base64,{get_image_base64(file_path)}"
    else:
        slide["src"] = "https://via.placeholder.com/300"  # Fallback image
        print(f"Image not found: {file_path}")

# Read and modify HTML content
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Inject slides data into HTML
slides_js = f"const slides = {str(slides).replace('src', 'src')};"
html_content = html_content.replace("const slides = [", f"{slides_js}\n// Original slides array replaced")

components.html(html_content, height=900)
