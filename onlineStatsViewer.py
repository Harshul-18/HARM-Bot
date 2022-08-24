import streamlit as st
from pytube import YouTube
import base64
from io import BytesIO
import pandas as pd
from videoProcessor import processingTheVid
from youtubeVideoStats import createDataset
import webbrowser
import chime

# if st.theme() == 'Dark':
#     file_ = open("/Users/harshulnanda/Documents/HARM-ML_challenge/harmLogoDark.gif", "rb")
# else:
#     file_ = open("/Users/harshulnanda/Documents/HARM-ML_challenge/harmLogo.gif", "rb")

hideStreamlitStyle = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hideStreamlitStyle, unsafe_allow_html=True)

with st.sidebar:

    st.markdown('''
        <p>By <b>HARM</b>, an intern team, aims to expand the world of AI by providing an useful feature.</p>
    ''', True)

    st.markdown("### Team Members ")

    if st.button("Harshul Nanda"):
        webbrowser.open_new_tab("https://www.linkedin.com/in/harshulnanda/")
    if st.button("Abhijeet Saroha"):
        webbrowser.open_new_tab("https://www.linkedin.com/in/abhijeet-saroha-a19031229/")
    if st.button("Rishabh Sagar"):
        webbrowser.open_new_tab("https://www.linkedin.com/in/rishabh-sagar-1b0b74229/")
    if st.button("Mayank Arora"):
        webbrowser.open_new_tab("https://www.linkedin.com/in/mayank-arora-24713322a/")


    st.markdown("### Contact us ")

    if st.button("GitHub"):
        webbrowser.open_new_tab("https://github.com/Harshul-18")
    if st.button("Linked In"):
        webbrowser.open_new_tab("https://www.linkedin.com/company/82157293/admin/")


file_ = open("harmLogo.gif", "rb")
    
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
st.markdown(
    f'<center><img src="data:image/gif;base64,{data_url}" alt="harmLogo" width=300 height=125></center>',
    unsafe_allow_html=True,
)

st.title("Hello, I am a YouTube API Bot!")
st.text("I am a simple tool, just enter the URL and I will give the video statistics.")

youtubeVideoUrl = st.text_input("Enter the URL of the Youtube Video", value="", type="default")

option = st.selectbox(
    'Select type of format of the video to download',
    ('Audio', 'Highest Resolution', 'Lowest Resolution')
)

if youtubeVideoUrl:
    with st.expander("Download"): 

        if (youtubeVideoUrl is None or len(youtubeVideoUrl) == 0):
            chime.error()
        
        videoObject = YouTube(youtubeVideoUrl)

        try:
            st.markdown("**Author of this video:** " + str(videoObject.author))
            st.markdown("**Title of video:** " + str(videoObject.title))
            st.markdown("**Number of views:** " + str(videoObject.views))
            st.markdown("**Video description:** " + str(videoObject.description))
            st.markdown("**Channel ID:** " + str(videoObject.channel_id))
            chime.success()
        except Exception as e:
            chime.error()
        
        if option=='Audio':
            a = videoObject.streams.get_audio_only().download()
        elif option=='Highest Resolution':
            a = videoObject.streams.get_highest_resolution().download()
        elif option=='Lowest Resolution':
            a = videoObject.streams.get_lowest_resolution().download()

        video = videoObject.streams
        if len(video) > 0:
            downloaded = False
            download_video = st.download_button(label="Download Video", data=a, file_name="video.mp4")
            download_audio = st.download_button(label="Download Audio Only", data=a, file_name="audio.mp3")
            if download_video:
                downloaded = True
            if download_audio:
                downloaded = True
            if downloaded:
                st.subheader("Download Complete")
        else:
            st.subheader("Sorry, this video can not be downloaded")

    


    with st.expander("View Video"):

        if (youtubeVideoUrl is None or len(youtubeVideoUrl) == 0):
            chime.error()

        videoObject = YouTube(youtubeVideoUrl)
        
        st.video(youtubeVideoUrl) 
        
        try:
            st.markdown("**Author of this video:** " + str(videoObject.author))
            st.markdown("**Title of video:** " + str(videoObject.title))
            st.markdown("**Number of views:** " + str(videoObject.views))
            st.markdown("**Video description:** " + str(videoObject.description))
            st.markdown("**Channel ID:** " + str(videoObject.channel_id))
            chime.success()
        except Exception as e:
            chime.error()

    with st.expander("View Channel Statistics"):

        if (youtubeVideoUrl is None or len(youtubeVideoUrl) == 0):
            chime.error()

        videoObject = YouTube(youtubeVideoUrl)

        processingTheVid(videoObject.channel_id)

        data = createDataset().astype(str)

        st.dataframe(data)

        # dataHist = data.plot.bar(x="title", y="views", figsize=(12, 8), fontsize=14)
        # st.pyplot(fig=dataHist)

footer="""<style>
a:link , a:visited{
color: black;
font-weight: bold;
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: none;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}

</style>
<div class="footer">
<p>Copyright © <a href="https://www.linkedin.com/company/82157293/admin/">HARM</a>, Designed by <a href="https://github.com/Harshul-18">Harshul</a>.</p>
</div>
"""

st.markdown(footer, True)
