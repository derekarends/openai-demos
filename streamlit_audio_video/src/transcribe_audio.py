""" Streamlit app for audio processing """
import os
import tempfile
import logging
import queue
import pydub
import openai
import streamlit as st

from streamlit_webrtc import WebRtcMode, webrtc_streamer
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

logger = logging.getLogger(__name__)

webrtc_ctx = webrtc_streamer(
    key="sendonly-audio",
    mode=WebRtcMode.SENDONLY,
    audio_receiver_size=256,
    media_stream_constraints={"audio": True},
)

sound_window_len = 5000  # 5s
sound_window_buffer = None

while True:
  if not webrtc_ctx.audio_receiver:
    logger.warning("AudioReceiver is not set. Abort.")
    break

  try:
    audio_frames = webrtc_ctx.audio_receiver.get_frames(timeout=1)
  except queue.Empty:
    logger.warning("Queue is empty. Abort.")
    break

  sound_chunk = pydub.AudioSegment.empty()
  for audio_frame in audio_frames:
    sound = pydub.AudioSegment(
      data=audio_frame.to_ndarray().tobytes(),
      sample_width=audio_frame.format.bytes,
      frame_rate=audio_frame.sample_rate,
      channels=len(audio_frame.layout.channels),
    )
    sound_chunk += sound

  if len(sound_chunk) > 0:
    if sound_window_buffer is None:
      sound_window_buffer = pydub.AudioSegment.empty()

    sound_window_buffer += sound_chunk

  if len(sound_window_buffer) > sound_window_len:
    sound_window_buffer = sound_window_buffer.set_channels(1) 
   
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=True) as tmp:
      sound_window_buffer.export(tmp.name, format="wav")
      sound_window_buffer = None

      response = openai.Audio.transcribe("whisper-1", tmp)
      st.write(response["text"])
      