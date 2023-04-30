import av
import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

_type = st.radio("Select transform type", ("noop", "vision"))


def callback(frame: av.VideoFrame) -> av.VideoFrame:
    img = frame.to_ndarray(format="bgr24")

    if _type == "noop":
      pass
    elif _type == "vision":
      # Run YOLOv8 inference on the frame
      results = model(img)
      print(results[0].tojson())

      # Visualize the results on the frame
      img = results[0].plot()

    return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(
    key="opencv-filter",
    mode=WebRtcMode.SENDRECV,
    video_frame_callback=callback,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)
