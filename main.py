import pyshorteners
import streamlit as st

def urlShorter(url):
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        return short_url
    except Exception as e:
        return str(e)

st.set_page_config(page_title='Acorta tu URL', page_icon=':)', layout='centered')
st.image("img/www.png", use_column_width=True)
st.title('Acorta tu URL')

url_input = st.text_input('Ingresa la URL que deseas acortar:')
if st.button('Comprimir URL'):
    if url_input:
        short_url = urlShorter(url_input)
        if short_url:
            st.success('¡URL acortada exitosamente!')
            st.write('URL acortada:', short_url)
        else:
            st.error('Ha ocurrido un error al acortar la URL. Por favor, verifica la URL e intenta nuevamente.')
    else:
        st.warning('Por favor, ingresa una URL para acortar.')
