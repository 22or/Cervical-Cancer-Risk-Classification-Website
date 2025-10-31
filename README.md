# Cervical Cancer Risk Classification Website

A web-based application that predicts cervical cancer risk using machine learning. Built with Django and MLServer, this project implements an XGBoost binary classification model trained on the [Cervical Cancer Risk Classification dataset](https://www.kaggle.com/datasets/loveall/cervical-cancer-risk-classification/data) from Kaggle.

## Overview

This application provides a user-friendly interface for assessing cervical cancer risk based on various demographic, behavioral, and medical history factors. The XGBoost model has been pre-trained and deployed using MLServer for efficient inference.

## Features

- **Risk Assessment Form**: Interactive web form for inputting patient data
- **Real-time Predictions**: Instant risk classification using a trained XGBoost model
- **RESTful API**: MLServer integration for model serving
- **User-friendly Interface**: Clean Django-based web interface

## Technology Stack

- **Backend Framework**: Django
- **Model Serving**: MLServer
- **Machine Learning**: XGBoost (binary classification)
- **Language**: Python 3.x

## Project Structure
```
Cervical-Cancer-Risk-Classification-Website/
├── model/                  # Trained XGBoost model with MLServer config
└── website/                # Django application
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**
```bash
   git clone https://github.com/22or/Cervical-Cancer-Risk-Classification-Website.git
   cd Cervical-Cancer-Risk-Classification-Website
```

2. **Create and activate a virtual environment**
```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Apply Django migrations**
```bash
   python manage.py migrate
```

## Running the Application

### Start MLServer (Model Server)

In a terminal window, start the MLServer instance:
```bash
mlserver start .
```

The model server will start on `http://localhost:8080` by default.

### Start Django Development Server

In a separate terminal window, start the Django application:
```bash
python manage.py runserver
```

The web application will be available at `http://localhost:8000`.

## Model Information

- **Algorithm**: XGBoost (Extreme Gradient Boosting)
- **Task**: Binary Classification
- **Dataset**: Cervical Cancer Risk Classification from Kaggle
- **Features**: Demographics, sexual history, contraceptive use, STDs, and other medical factors
- **Target**: Biopsy result (positive/negative for cervical cancer risk)

The model has been pre-trained and saved in the `model/` directory. No additional training is required to run the application.

## Usage

1. Navigate to `http://localhost:8000` in your web browser
2. Fill out the risk assessment form with the required information:
   - Age
   - Number of sexual partners
   - First sexual intercourse age
   - Number of pregnancies
   - Smoking habits
   - Hormonal contraceptive use
   - STD history
   - Other relevant medical factors
3. Submit the form to receive a risk prediction
4. The model will classify the risk as positive or negative for cervical cancer

## API Endpoints

### MLServer Model Endpoint
```
POST http://localhost:8080/v2/models/cervical-cancer-model/infer
```

Request body format:
```json
{
  "inputs": [
    {
      "name": "input",
      "shape": [1, n_features],
      "datatype": "FP32",
      "data": [...]
    }
  ]
}
```

### Django Application Endpoints
- `/` - Home page with risk assessment form
- `/predict` - Form submission endpoint for predictions

## Dependencies

Key dependencies include:
- Django
- MLServer
- XGBoost
- NumPy
- Pandas
- Scikit-learn

See `requirements.txt` for the complete list of dependencies.

## Disclaimer

This application is for educational and research purposes only. It should **not** be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers regarding medical conditions and treatment options.

## Dataset Attribution

The dataset used in this project is provided by Kaggle:
- **Source**: [Cervical Cancer Risk Classification Dataset](https://www.kaggle.com/datasets/loveall/cervical-cancer-risk-classification/data)
- **Original Collection**: Hospital Universitario de Caracas, Venezuela
- **Samples**: 858 patients
- **Features**: 32 attributes including demographics, habits, and medical records

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact

For questions or suggestions, please open an issue on GitHub.

## Acknowledgments

- Kaggle for providing the dataset
- Hospital Universitario de Caracas for the original data collection
- The open-source community for Django, MLServer, and XGBoost

---

**Note**: Ensure both MLServer and Django development server are running simultaneously for the application to function properly.
