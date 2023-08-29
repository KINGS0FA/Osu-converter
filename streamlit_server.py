import streamlit as st
import webbrowser

st.title('Osu Link Converter')

link = st.text_input('Enter Osu Link to convert',
                     help='Enter Link ex:[https://osu.ppy.sh/beatmapsets/xxxxxx#osu/xxxxxxx')

if st.button('Nerinyan'):
    start_marker = "beatmapsets/"
    end_marker = "#osu"
    start_index = link.find(start_marker) + len(start_marker)
    end_index = link.find(end_marker)
    extracted_string = link[start_index:end_index]

    if len(link) == 0:
        st.markdown('<span style="color: red;">Enter URL!</span>', unsafe_allow_html=True)
    elif 'beatmapsets/' not in link:
        st.markdown('<span style="color: red;">Invalid URL!</span>', unsafe_allow_html=True)
    else:
        webbrowser.open(f'https://nerinyan.moe/d/{extracted_string}')
        new_link = f'https://nerinyan.moe/d/{extracted_string}'
        st.markdown('<span style="color: green;">Link converted to Nerinyan!</span>', unsafe_allow_html=True)
        st.markdown(f'<span style="color: green;">{new_link}</span>', unsafe_allow_html=True)

if st.button('Chimu'):
    start_marker = "beatmapsets/"
    end_marker = "#osu"
    start_index = link.find(start_marker) + len(start_marker)
    end_index = link.find(end_marker)
    extracted_string = link[start_index:end_index]

    if len(link) == 0:
        st.markdown('<span style="color: red;">Enter URL!</span>', unsafe_allow_html=True)
    elif 'beatmapsets/' not in link:
        st.markdown('<span style="color: red;">Invalid URL!</span>', unsafe_allow_html=True)
    else:
        webbrowser.open(f'https://chimu.moe/d/{extracted_string}')
        new_link = f'https://chimu.moe/d/{extracted_string}'
        st.markdown('<span style="color: green;">Link converted to Chimu!</span>', unsafe_allow_html=True)
        st.markdown(f'<span style="color: green;">{new_link}</span>', unsafe_allow_html=True)

if st.button('BeatConnect'):
    start_marker = "beatmapsets/"
    end_marker = "#osu"
    start_index = link.find(start_marker) + len(start_marker)
    end_index = link.find(end_marker)
    extracted_string = link[start_index:end_index]

    if len(link) == 0:
        st.markdown('<span style="color: red;">Enter URL!</span>', unsafe_allow_html=True)
    elif 'beatmapsets/' not in link:
        st.markdown('<span style="color: red;">Invalid URL!</span>', unsafe_allow_html=True)
    else:
        webbrowser.open(f'https://beatconnect.io/b/{extracted_string}')
        new_link = f'https://beatconnect.io/b/{extracted_string}'
        st.markdown('<span style="color: green;">Link converted to BeatConnect!</span>', unsafe_allow_html=True)
        st.markdown(f'<span style="color: green;">{new_link}</span>', unsafe_allow_html=True)
