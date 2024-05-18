# Password Strength Evaluator

This project contains a machine learning model that evaluates the strength of passwords into three categories: strong, weak, and medium. The code and data used to develop this model are not originally mine and credit is given to the original authors.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)

## Introduction
Password security is an important aspect of digital security. This project uses a machine learning model to evaluate and categorize passwords based on their strength. 

## Features
- Classifies passwords into three categories: strong, medium, and weak.
- Utilizes a trained machine learning model.
- Easy to use and integrate into other applications.

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/tagoreji/Password-Strength-Evaluator.git
    cd your-repository
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Training the Model
To train the model, run the following script:
```sh
python scripts/train_model.py
```

To evaluate the model, run the following script:
```sh
python scripts/evaluate_password.py
```


## Credits

This project is built upon the code and data developed by the original authors:

- **Code**: Original code by [amankharwal](https://thecleverprogrammer.com/2022/08/22/password-strength-checker-with-machine-learning/).
- **Data**: Dataset provided by [BHAVIK BANSAL](https://www.kaggle.com/datasets/bhavikbb/password-strength-classifier-dataset).

Their contributions are greatly acknowledged and appreciated.

