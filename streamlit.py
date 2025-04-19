import streamlit as st
import os

# Set page configuration
st.set_page_config(page_title="Image Test", layout="wide")

# Title
st.title("Image Loading Test (Updated: 04-19-2025 05:50 AM PDT)")

# List of image files
image_files = [f"{i}.jpg" for i in range(1, 16)]

# Check and display each image with a smaller size
for img_file in image_files:
    try:
        # Check if file exists in the root directory
        if os.path.exists(img_file):
            st.image(img_file, caption=f"Image {img_file}", width=300)
        else:
            st.error(f"File {img_file} not found in the root directory.")
    except Exception as e:
        st.error(f"Failed to load {img_file}: {str(e)}")
        st.write("Please check the file or reupload it.")

# Add a note for debugging
st.write("If images are not loading, verify files in the repository root and clear browser cache. Test raw URLs (e.g., https://raw.githubusercontent.com/yourusername/yourrepo/main/1.jpg).")
