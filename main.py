import random
import time
import os
import streamlit as st

def roll_dice():
    return random.randint(1, 6)

def show_dice_gif(result):
    gifs_path = os.path.join("src")
    gif_name = f"{result}.gif"
    gif_full_path = os.path.join(gifs_path, gif_name)
    if os.path.exists(gif_full_path):
        st.image(gif_full_path, use_container_width=True)
    else:
        st.error(f"GIF not found for {result}")

def main():
    st.title("🎲 Dice Simulator")
    
    if st.button("Throw the Dice"):
        with st.spinner("Spinning the Dice..."):
            time.sleep(1)
            result = roll_dice()
            show_dice_gif(result)
            st.success(f"You earned a {result}!")

if __name__ == "__main__":
    main()