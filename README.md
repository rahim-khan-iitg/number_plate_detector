# Number Plate Detector with YOLOv5 Model and Django

![Number Plate Detector](images/demo.png)

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [How it Works](#how-it-works)
- [Demo](#demo)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository contains a Number Plate Detector web application built using the YOLOv5 object detection model and Django framework. The application is designed to detect and extract number plates from images provided by the users. The YOLOv5 model is used for its high accuracy and efficiency in real-time object detection tasks.

## Installation

To run the Number Plate Detector locally, follow these steps:

1. Clone this GitHub repository to your local machine:

```bash
git clone https://github.com/rahim-khan-iitg/number_plate_detector.git
cd number_plate_detector
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To start the Django development server, run the following command:

```bash
python manage.py runserver
```

Once the server is running, open your web browser and navigate to `http://127.0.0.1:8000/`. You should see the Number Plate Detector web application. Upload an image containing a vehicle with a visible number plate, and the application will process the image using easyocr and display the detected number plate.
you can find kaggle notebook and training data set <a href="https://www.kaggle.com/code/rahimkhan76/number-plate-detection">here</a>

## How it Works

The Number Plate Detector is built upon the YOLOv5 object detection model. YOLOv5 is a state-of-the-art deep learning model that can detect and locate objects in images in real-time. The model has been trained on a large dataset of vehicle images to specifically recognize and extract number plates.

The Django framework is used to create the web application interface for the number plate detection. Users can upload images through the web interface, and the Django backend will process these images using the YOLOv5 model to detect number plates. The detected number plates are then displayed back to the user.


## Contributing

Contributions to this Number Plate Detector project are welcome. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
