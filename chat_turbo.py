import streamlit as st 
import os 
import openai
from dotenv import load_dotenv

emoji_robo = "🤖"
emoji_user = "🙋"

#load_dotenv()  # carrega as variáveis de ambiente do arquivo .env

#openai.api_key = os.getenv('SENHA_OPEN_AI')

openai.api_key = st.secrets["chaveOpenAI"]

st.title(f'{emoji_robo} Pergunte ao Jarvis')
st.write('***')

if 'hst_conversa' not in st.session_state:
    st.session_state.hst_conversa = []

pergunta = st.text_input('Digite sua pergunta')

col1, col2 = st.columns(2)

with col1:
    btn_enviar = st.button("Enviar Pergunta")

with col2:
    btn_limpar = st.button("Limpar Conversa")

if btn_enviar: 
    st.session_state.hst_conversa.append({"role": "user", "content": pergunta})
    retorno_openai = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", 
        messages = st.session_state.hst_conversa,
        max_tokens = 500,
        n=1
    )
    st.session_state.hst_conversa.append(
        {"role": "assistant", 
         "content": retorno_openai['choices'][0]['message']['content']})
    
if btn_limpar: # se o botão "Limpar Conversa" for pressionado
    st.session_state.hst_conversa = [] # redefine a lista de histórico de conversa para vazia
    pergunta = '' # redefine o valor do input para uma string vazia

if len(st.session_state.hst_conversa) > 0:
    for i in range(len(st.session_state.hst_conversa)):
        if i % 2 == 0:
            with st.container():
                st.write(f"{emoji_user} Você: " + st.session_state.hst_conversa[i]['content'])
        else:
            with st.container():
                st.write(f"{emoji_robo} Resposta da IA: " + st.session_state.hst_conversa[i]['content'])

# Adiciona a barra lateral com informações do autor
st.sidebar.markdown("<h3 style='text-align: center; font-size: 20px; color: Red'>By Melo Jr &reg - 2023</h3>", unsafe_allow_html=True)
