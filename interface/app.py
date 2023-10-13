import cv2
import streamlit as st
from PIL import Image
def detect_faces(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    return image

def main():
    st.title("Headshot simulator")

    video_source = st.sidebar.radio("Select video source:", ("Webcam", "Upload"))

    if video_source == "Webcam":
        cap = cv2.VideoCapture(0)
    else:
        uploaded_file = st.sidebar.file_uploader("Choose a video file", type=["mp4", "avi"])
        if uploaded_file is not None:
            file_bytes = uploaded_file.read()
            cap = cv2.VideoCapture(file_bytes)

    if "cap" in locals():
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            frame_with_faces = detect_faces(frame)

            st.image(frame_with_faces, channels="BGR", use_column_width=True)

        cap.release()

if __name__ == "__main__":
    main()
