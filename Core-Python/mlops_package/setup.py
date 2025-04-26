from setuptools import setup, find_packages

setup(
    name="mlops_python",
    version="1.0",
    packages=find_packages(),
    description="MLOps Python Package",
    long_description="This package provides utilities for MLOps, including data loading, preprocessing, model training, and serialization.",
    author="Nachiketh",
    author_email="nachiketh@manifoldailearning.in",
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scikit-learn>=0.24.0",
        "joblib>=1.0.0",
        "pickle5>=0.0.11",
    ],
)