#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Hamzah Zaman",
    author_email='hamzahzaman21@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This notebook contains the code I used to get a score of 0.79186 (TOP 5%) on the Titanic-Machine Learning from Disaster Kaggle Competition. Sources I used are outlined below.  Steps:  1.) Performed Exploratory Data Analysis(EDA) to understand the data set more. 2.) After EDA was complete, preprocessed the data to make it easier to train on 3.) Perfomed classification using Random Forest Classifier, Logistic Regression, SVM, XGBoost, and LightGBM 4.) Performed hypertuning using Bayes Search CV 5.) Perfomed additional hypertuning to find optimum probability threashold 6.) Performed preprocessing steps on the test data and made predictions 7.) Created the submitted file  Sources: https://www.kaggle.com/code/anandhuh/titanic-simple-solution-top-12 https://github.com/ahmedbesbes/How-to-score-0.8134-in-Titanic-Kaggle-Challenge/blob/master/article_1.ipynb https://www.kaggle.com/code/sathyanarayanrao89/factor-analysis-and-svm-predictions",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='titanic___machine_learning_from_disaster___kaggle_project',
    name='titanic___machine_learning_from_disaster___kaggle_project',
    packages=find_packages(include=['titanic___machine_learning_from_disaster___kaggle_project', 'titanic___machine_learning_from_disaster___kaggle_project.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/HamzahZaman21/titanic___machine_learning_from_disaster___kaggle_project',
    version='0.1.0',
    zip_safe=False,
)
