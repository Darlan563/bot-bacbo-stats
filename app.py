import streamlit as st
import pandas as pd
import telebot

# 1. ESTA LINHA TEM QUE SER A PRIMEIRA DE TODAS:
st.set_page_config(page_title="BacBo Pro", layout="centered")

# 2. DEPOIS VOCÊ COLOCA AS SUAS CONFIGURAÇÕES:
TOKEN = "8787083495:AAFlFbZ3VGk8zj-11vqxVdCKWFoxdyqHKPc"
CHAT_ID = 123456789 # <--- COLOQUE O SEU ID AQUI (SÓ NÚMEROS)

bot = telebot.TeleBot(TOKEN)

# O restante do código continua igual abaixo...
def enviar_telegram(msg):
    try:
        bot.send_message(CHAT_ID, msg)
    except Exception as e:
        st.error(f"Erro no Telegram: {e}")

st.title("🤖 Bac Bo: Analisador + Telegram")

if 'historico' not in st.session_state:
    st.session_state.historico = []

st.subheader("Registrar Resultado Manual")
c1, c2, c3 = st.columns(3)

if c1.button("🔵 Player"):
    st.session_state.historico.append('P')
    if len(st.session_state.historico) >= 3 and st.session_state.historico[-3:] == ['P','P','P']:
        enviar_telegram("🚨 SINAL: 3 Azuis! Entrar em BANKER 🔴")

if c2.button("🔴 Banker"):
    st.session_state.historico.append('B')
    if len(st.session_state.historico) >= 3 and st.session_state.historico[-3:] == ['B','B','B']:
        enviar_telegram("🚨 SINAL: 3 Vermelhos! Entrar em PLAYER 🔵")

if c3.button("⚪ Tie"):
    st.session_state.historico.append('T')

st.write(f"Últimos: {st.session_state.historico[-10:]}")
if st.session_state.historico:
    df = pd.DataFrame(st.session_state.historico, columns=['Res'])
    st.bar_chart(df['Res'].value_counts())
import telebot # Nova biblioteca para o Telegram

# COLOQUE SEUS DADOS AQUI
TOKEN = "8787083495:AAFlFbZ3VGk8zj-11vqxVdCKWFoxdyqHKPc"
CHAT_ID = 5274158834

bot = telebot.TeleBot(TOKEN)

def enviar_sinal(mensagem):
    try:
        bot.send_message(CHAT_ID, mensagem)
    except:
        pass

# --- INTERFACE DO DASHBOARD ---
st.set_page_config(page_title="BacBo Pro", layout="centered")
st.title("🤖 Bac Bo: Analisador + Telegram")

if 'historico' not in st.session_state:
    st.session_state.historico = []

st.subheader("Registrar Resultado Manual")
c1, c2, c3 = st.columns(3)

if c1.button("🔵 Player"):
    st.session_state.historico.append('P')
    # Verifica sinal após clicar
    if len(st.session_state.historico) >= 3 and st.session_state.historico[-3:] == ['P','P','P']:
        enviar_telegram("🚨 SINAL: 3 Azuis! Entrar em BANKER 🔴")

if c2.button("🔴 Banker"):
    st.session_state.historico.append('B')
    # Verifica sinal após clicar
    if len(st.session_state.historico) >= 3 and st.session_state.historico[-3:] == ['B','B','B']:
        enviar_telegram("🚨 SINAL: 3 Vermelhos! Entrar em PLAYER 🔵")

if c3.button("⚪ Tie"):
    st.session_state.historico.append('T')

# --- EXIBIÇÃO ---
st.write(f"Últimos: {st.session_state.historico[-10:]}")
if st.session_state.historico:
    df = pd.DataFrame(st.session_state.historico, columns=['Res'])
    st.bar_chart(df['Res'].value_counts())
    
