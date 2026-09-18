# Pothole Detection

Object detection model that identifies potholes from images using YOLOv8.

## Dataset

Dataset from [Brad Dwyer on Roboflow](https://universe.roboflow.com/brad-dwyer/pothole-voxrl)

## Model

- Architecture: YOLOv8n
- Epochs: 50
- Image size: 640x640

## Results

| Metric    | Score |
| --------- | ----- |
| mAP50     | 0.773 |
| mAP50-95  | 0.506 |
| Precision | 0.786 |
| Recall    | 0.667 |

## Demo

The project includes a Gradio app for testing the model interactively. When you upload a road image, it draws bounding boxes around detected potholes.

[![Demo](assets/demo.png)](assets/demo.png)

## Setup

1. Clone the repo
2. Create the conda environment:

```
conda env create -f environment.yml
conda activate pothole-detection
```

3. (Optional: only needed if retraining) Download the dataset from Roboflow and place it in the `data/` folder. The trained weights (`models/best.pt`) are already included in the repo, so this step isn't required just to run the demo or make predictions.

## Usage

### Interactive demo

```
python app.py
```

This launches a local Gradio web app (default: `http://127.0.0.1:7860`) where you can upload a road image and see detected potholes drawn on the output.

### Python API

```
from ultralytics import YOLO

model = YOLO('models/best.pt')
results = model.predict(source='path/to/image.jpg', conf=0.5)
results[0].show()
```

## About

Personal Project for Pothole Detection using YOLO model
