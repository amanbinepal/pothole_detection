import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

import gradio as gr
from ultralytics import YOLO
from PIL import Image

model = YOLO('models/best.pt')

def detect(image):
    results = model.predict(image, conf=0.5)
    return Image.fromarray(results[0].plot())

gr.Interface(
    fn=detect,
    inputs=gr.Image(),
    outputs=gr.Image(),
    title="Pothole Detector",
    description="Upload a road image to detect potholes"
).launch()