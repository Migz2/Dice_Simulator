import random
import time
import os
import streamlit as st

def roll_dice():
    """Função que simula o lançamento do dado e retorna o resultado"""
    return random.randint(1, 6)

def show_dice_gif(result):
    """Função que mostra o GIF correspondente ao resultado do dado"""
    gifs_path = os.path.join("src")
    gif_name = f"{result}.gif"
    gif_full_path = os.path.join(gifs_path, gif_name)
    if os.path.exists(gif_full_path):
        st.image(gif_full_path, caption=f"Dado mostrando {result}", use_column_width=True)
    else:
        st.error(f"GIF não encontrado para o número {result}")

def main():
    st.title("🎲 Simulador de Dados")
    
    if st.button("Jogar Dado"):
        with st.spinner("Rolando o dado..."):
            time.sleep(1)  # Pequena pausa para efeito visual
            result = roll_dice()
            show_dice_gif(result)
            st.success(f"Você rolou um {result}!")

if __name__ == "__main__":
    main()