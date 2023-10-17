import torch
import streamlit as st
# from .detector import detect_faces
from headshot import Headshot

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = Headshot()

# model.load_pretrain('')

def main():
    st.title("Headshot simulator")

    video_source = st.sidebar.radio("Select video source:", ("Webcam", "Upload","Demo"))

    if video_source == "Webcam":
        pass

    elif video_source == "Demo":
        # prediction,image = sample()
        pass
    else:
        uploaded_file = st.sidebar.file_uploader("Choose a video file", type=["mp4", "avi"])
        if uploaded_file is not None:
            file_bytes = uploaded_file.read()



if __name__ == "__main__":
    main()
