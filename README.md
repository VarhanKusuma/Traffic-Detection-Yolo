# 🚦 Traffic Detective: Real-Time Vehicle Detection (YOLOv8) via Telegram

[![Status](https://img.shields.io/badge/Status-Deployed-brightgreen.svg)]()
[![Model](https://img.shields.io/badge/Model-YOLOv8n-blue.svg)]()
[![API Hosting](https://img.shields.io/badge/API-HuggingFaceSpaces-orange.svg)]()
[![License](https://img-shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

This project implements an **end-to-end Machine Learning pipeline** for real-time vehicle detection and classification. It showcases the full lifecycle of an ML model: from training and deployment to its consumption via a user-friendly Telegram bot.

The core complexity lies in seamlessly integrating a public API hosted on Hugging Face with a self-hosted automation infrastructure running on Docker.

---

## 🚀 Live Demo

The model is deployed and fully operational. You can test the detection service directly:

| Component             | Detail                                         | Link                                                                               |
| :-------------------- | :--------------------------------------------- | :--------------------------------------------------------------------------------- |
| **Telegram Bot**      | Send any image containing vehicles to the bot. | **@TrafficDetection**                                                              |
| **Live API Endpoint** | FastAPI/Gradio documentation for the model.    | [https://vhnks-traffic-api.hf.space/docs](https://vhnks-traffic-api.hf.space/docs) |

---

## ⚙️ Technology Stack

| Category           | Technology                    | Purpose                                                                        |
| :----------------- | :---------------------------- | :----------------------------------------------------------------------------- |
| **Core ML**        | **YOLOv8n** (Ultralytics)     | Lightweight model for fast, accurate vehicle localization.                     |
| **Dataset**        | Roboflow Vehicle Detection    | Sourcing 3,300+ labeled images for specialization.                             |
| **Training**       | Google Colab (T4 GPU)         | Efficient training environment for 30 epochs.                                  |
| **Deployment**     | Hugging Face Spaces           | Publicly hosts the model as a scalable REST API.                               |
| **Automation**     | **n8n** (Workflow Automation) | The orchestration layer connecting Telegram to the API.                        |
| **Infrastructure** | **Docker & Ngrok/Caddy**      | Self-hosted environment management and secure HTTPS exposure for n8n webhooks. |

---

## 🔍 The End-to-End Workflow

This project is built around a complex, three-stage workflow ensuring zero-friction user experience.

### Phase 1: Model Training & Specialization

1.  **Data Curation:** Sourced and processed a specialized dataset for four vehicle classes: _Cars, Motorcycles, Buses, and Trucks_.
2.  **Model Selection:** Choosing the **YOLOv8n** model for its balance of size and performance.
3.  **Training:** The model was trained for **30 _epochs_** on a **Google Colab (GPU T4)** instance.

### Phase 2: Public API Deployment

1.  **Serving:** The custom weights (`best.pt`) are packaged and served as a scalable REST API on **Hugging Face Spaces**.
2.  **Functionality:** The API is configured to receive an image file via POST request and return the output image with detection bounding boxes applied.

### Phase 3: The Automation Layer (n8n & Docker)

This layer manages the flow from the user to the API and back:

1.  **Telegram Trigger:** Captures the image and the user's `Chat ID` upon receiving a photo.
2.  **Secure Connection:** The n8n instance, running in **Docker**, is exposed via **Ngrok Tunnel**, providing the necessary **HTTPS** webhook URL.
3.  **Processing:** The **HTTP Request** node forwards the image to the Hugging Face API.
4.  **Response:** The final detected image is sent back to the original sender's `Chat ID` using the **Send Photo** node.

---

## 💻 Self-Hosting & Development

To replicate or contribute to the n8n automation part of this project, you will need:

### Prerequisites

- Docker and Docker Compose.
- A verified Ngrok account (or a static domain and VPS for Caddy/Nginx).
- A Telegram Bot Token.

### Environment Setup (Key Docker Variables)

For the n8n instance to correctly handle Telegram webhooks, these **Environment Variables** must be set during Docker container creation:

```bash
N8N_HOST=your-ngrok-tunnel.ngrok-free.app  # The public URL provided by Ngrok
N8N_PROTOCOL=https
WEBHOOK_URL=[https://your-ngrok-tunnel.ngrok-free.app/](https://your-ngrok-tunnel.ngrok-free.app/)
```
