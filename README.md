# CCS parameter Prediction System

## Overview

This project focuses on analyzing pellet properties to identify and address factors impacting Cold Crushing Strength (CSS), a critical parameter in the quality control of iron ore pellets. During the internship at Jindal, a systematic approach was adopted using Python, Excel, and data visualization tools to uncover patterns and support decision-making. A predictio model was also developed to find out parameters and visualize CSS trends effectively.

## Project Objective

- Analyze historical production data to understand variations in CSS.
- Identify key parameters influencing pellet strength.
- Develop visual tools for continuous monitoring and performance evaluation.
- Suggest process improvements based on data-driven insights.

## Setup

### Prerequisites

- Python 3.8
- Flask
- Pandas
- NumPy
- Scikit-Learn
- PyMongo
- MongoDB

## Installation
1. **Clone the repository**:
    
sh
    git clone https://github.com/dhruvg13/CSS-Parameters.git
    cd CSS-Parameters


2. **Create and activate a virtual environment**:
    
sh
    python3.8 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`


3. **Install the dependencies**:
    
sh
    pip install -r requirements.txt


## Run the application

1. **Start the Flask Application**:
    
sh
    python app.py


2. **Access the Application**:
    - Open a web browser and navigate to http://localhost:5000 to access the application.

## How It Works
1. **Data Preparation**:
    - The dataset data.csv is loaded and preprocessed. Missing values are replaced with the mean of the respective columns. duplicate records are deleted.


2. **Model Training**:
    - The data is split into training and testing sets.
    - Features are standardized using StandardScaler.
    - A Logistic Regression model is trained on the standardized training data.
    - The trained model and scaler are saved using pickle.

3. **Web Application**:
   - The Flask application serves a web form where users can input their health parameters.
   - The input data is standardized using the pre-trained scaler.
   - The standardized data is fed into the Logistic Regression model to make predictions.
   - The results and user data are stored in a MongoDB database.

##  Project Outcomes
- Enabled root cause identification for weak pellet batches.
- Provided a scalable system for ongoing quality monitoring.
- Built confidence in data-driven decision-making for process control.
