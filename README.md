# Energy & Carbon-Aware AI Model Selection Framework

## Overview
This project implements a sustainability-aware machine learning model selection framework.  
It evaluates models using four key metrics:

- Accuracy  
- Energy Consumption  
- Carbon Emissions  
- Latency  

The system supports deployment-aware decision making for:

- Edge Devices  
- Cloud Servers  
- Enterprise Systems  

---

## Evaluated Models

- ResNet50  
- MobileNetV2  
- EfficientNet-B0  
- Quantized-MobileNet (8-bit)  

---

## Features

- CPU-based energy estimation  
- Carbon footprint calculation (country-adjustable)  
- Multi-objective sustainability scoring  
- AutoML-based recommendation  
- Pareto frontier visualization  
- Streamlit interactive dashboard  

---


## Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```


Run the Dashboard
```
streamlit run app.py
```
Dataset

This project uses the CIFAR-10 dataset.

The dataset is not included in this repository.
Download it from:

https://www.cs.toronto.edu/~kriz/cifar.html

Author
Ganesh Reddy
Vellore Institute of Technology



