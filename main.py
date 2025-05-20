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
        st.error(f"GIF não encontrado para o número {result}")

def main():
    st.title("🎲 Simulador de Dados")
    
    if st.button("Jogar Dado"):
        with st.spinner("Rolando o dado..."):
            time.sleep(1)
            result = roll_dice()
            show_dice_gif(result)
            st.success(f"Você rolou um {result}!")

if __name__ == "__main__":
    main()