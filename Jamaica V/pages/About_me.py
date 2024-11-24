import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Overthinking Out Loud",
    page_icon='📝'
)

img = Image.open('./image/ad.png')

col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(img, width=230)

with col2:
    st.title('Jamaica Valdez')
    st.write('Currently Studying in SNSU main campus, a BSCpE Sudent')

st.write("\n")
st.subheader("Five Facts About Me", anchor=False)
"""
-Nature Lover 🌱: I adore hiking, camping, and just being surrounded by greenery—it’s where I feel most alive.

-Creative Soul 🎨: Painting and sketching are my favorite ways to express myself when words fall short.

-Coffee Enthusiast ☕: I can’t start my day without a good cup of cappuccino (bonus points if there’s latte art involved).

-Bookworm 📚: I’m always lost in a good novel, especially ones with strong female leads or epic fantasy worlds.

-Hopeless Romantic 💕: I love rom-coms, writing poetry, and those little moments that feel like they’re straight out of a movie.
"""

st.sidebar.success("Select pages above")
