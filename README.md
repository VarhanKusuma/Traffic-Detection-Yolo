# traffic-detection-yolo

Real-Time Vehicle Detection (Cars, Motorcycles, Buses) using YOLOv8 for Traffic Analysis.

# 🤖 Technology Used

- **Model:** YOLOv8n
- **Dataset:** [Vehicle Detection Dataset from Roboflow Universe](https://universe.roboflow.com/vaishak-shetty-sri7e/vehicle-detection-byizq)
- **Tools:** Google Colab (for GPU training), Roboflow (for dataset management), Python.

## 📝 Work Process

1.  **Dataset Preparation:** Using a dataset from Roboflow with more than 3,300 images.
2.  **Training:** Train the `yolov8n` model for 30 epochs on Google Colab using a T4 GPU.
3.  **Results:** A custom model (`best.pt`) specialized for detecting 4 vehicle classes.
