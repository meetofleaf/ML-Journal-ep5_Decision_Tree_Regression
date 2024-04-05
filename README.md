![Banner](.media/banner.png)
# ML Journal - Machine Learning Fundamentals Series
In this series of repositories, we'll explore various models, documenting the code and thought process behind each one.  The goal is to create a journal-like experience for both myself and anyone following along. By sharing the journey, we can:

- Break down complex concepts: We'll approach each model step-by-step, making the learning process manageable.
- Learn from mistakes: Documenting the process allows us to identify and learn from any errors along the way.
- Build a foundation: Each repository will build upon the knowledge from the previous one, creating a solid foundation in machine learning basics.
- We believe this approach can be particularly helpful for beginners struggling to find a starting point in the vast world of machine learning.


# Ep 05 - Decision Tree Regression
This is the fifth installment in the 'ML Journal' series. This specific repository focuses on Decision Tree Regression. It is a powerful tool for unraveling the relationships between features and continuous target variables.

Don't worry, the concept is explained here:
#### [Concept explanation](https://github.com/meetofleaf/ML-Journal-ep5_Decision_Tree_Regression/blob/main/dtr_explanation.md)


## Data
This repository includes the dataset containing Petrol Consumption data.
The dataset contains 5 variables and 48 instances. It was uploaded to [Kaggle](https://www.kaggle.com/) by [Arpit Kumar](https://www.kaggle.com/arpikr)

Dataset link: https://www.kaggle.com/datasets/arpikr/petrol-consumption

**Data dictionary**:
|Variable Name                |Data type |Variable type |Variable role |Sample  |
|:----------------------------|:---------|:-------------|:-------------|-------:|
|Petrol_tax                   |float     |Continuous    |Independent   |_9.00_  |
|Average_income               |int       |Discrete      |Independent   |_4958_  |
|Paved_Highways               |int       |Discrete      |              |_5800_  |
|Population_Driver_licence(%) |float     |Continuous    |              |_0.850_ |
|Petrol_Consumption           |int       |Discrete      |Dependent     |_458_   |


## Code
The Python code file (decision_tree_regression.py AND decision_tree_regression.ipynb) demonstrates how to implement decision tree regression using a popular machine learning library scikit-learn. You will find guiding comments in the code specifying purpose of each block of code in 1-2 lines.


## Requirements
Following is a list of the programs and libraries, with the versions, used in the code:

- `Python==3.12.1`
  - `numpy==1.26.3`
  - `pandas==2.2.0`
  - `matplotlib==3.8.3`
  - `scikit-learn==1.4.1`

## Getting Started
- Clone this repository.
- Make sure you have the required programs and libraries installed. You can install them using the requirements file with:
  - `pip install -r requirements.txt`
- Simply run the Python script either from your OS' command prompt or from your choice of IDE.
- Follow the comments and code execution to understand the process.
- I encourage you to experiment with the code, modify the data, and play around with the model!
- Lastly, feel free to share any suggestions, corrections, ideas or questions you might have.

Also feel free to reach out to me for any discussion or collaboration. I'd be glad to productively interact with you.

This is just the first step in our machine learning journey. Stay tuned for future repositories exploring other fundamental models!


## References & Guidance Links:
- Python: https://www.python.org/
  - Scikit-learn: https://scikit-learn.org/stable/install.html
  - Pandas: https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html
  - NumPy: https://numpy.org/install/
  - Matplotlib: https://matplotlib.org/stable/users/installing/index.html
- Pip (Python Package Manager): https://pip.pypa.io/en/stable/user_guide/
- Git: https://git-scm.com/
