import torch
import streamlit as st
import cv2
import numpy as np
# from headshot import Headshot

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# model = Headshot()

def detect_faces(frame):
    # Implement your face detection logic here
    # For demonstration purposes, return a dummy bounding box
    return [(100, 100, 200, 200)]

def main():
    st.title("Headshot simulator")

    video_source = st.sidebar.radio("Select video source:", ("Webcam", "Upload", "Demo"))

    if video_source == "Webcam":
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            faces = detect_faces(frame)
            for face in faces:
                x, y, w, h = face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            st.image(frame, channels="RGB")

    elif video_source == "Demo":
        # prediction, image = sample()
        pass
    else:
        uploaded_file = st.sidebar.file_uploader("Choose a video file", type=["mp4", "avi"])
        if uploaded_file is not None:
            file_bytes = uploaded_file.read()
            cap = cv2.VideoCapture(uploaded_file.name)
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                faces = detect_faces(frame)
                for face in faces:
                    x, y, w, h = face
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                st.image(frame, channels="RGB")

if __name__ == "__main__":
    main()