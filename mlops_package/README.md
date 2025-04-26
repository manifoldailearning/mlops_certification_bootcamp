# MLOps Python Package

A modular Python package for implementing linear regression on advertising data. This package demonstrates best practices in MLOps, including data handling, model implementation, and preprocessing utilities.

## Package Structure

```
mlops_package/
├── mlops_python/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── data_loader.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── linear_regression.py
│   └── utils/
│       ├── __init__.py
│       └── preprocessor.py
├── example.py
└── requirements.txt
```

## Detailed Implementation Explanation

### 1. Data Module (`data_loader.py`)

The data module is responsible for loading and preparing the advertising dataset. It consists of two main methods:

- `load_data()`: Reads the CSV file using pandas and returns a DataFrame
- `prepare_data()`: Extracts features (TV, radio, newspaper) and target (sales) variables, converting them to numpy arrays

Key features:
- Type hints for better code readability and IDE support
- Error handling for file operations
- Clean separation of data loading and preparation

### 2. Models Module (`linear_regression.py`)

The models module implements a linear regression model using gradient descent. Key components:

- **Initialization**:
  - Learning rate and number of iterations are configurable
  - Weights and bias are initialized as None and set during training

- **Training Process**:
  - Implements batch gradient descent
  - Updates parameters using the mean squared error loss function
  - Supports multiple features through vectorized operations

- **Prediction and Evaluation**:
  - `predict()`: Makes predictions using the trained model
  - `score()`: Calculates R-squared score for model evaluation

### 3. Utils Module (`preprocessor.py`)

The utils module provides essential preprocessing functions:

- **Train-Test Split**:
  - Implements a custom train-test split function
  - Supports configurable test size and random state
  - Ensures reproducible splits

- **Feature Normalization**:
  - Implements min-max scaling
  - Handles multiple features simultaneously
  - Preserves the relative relationships between features

## Usage Example

The package can be used as shown in `example.py`:

```python
from mlops_python.data.data_loader import DataLoader
from mlops_python.models.linear_regression import LinearRegression
from mlops_python.utils.preprocessor import Preprocessor

# Initialize data loader
data_loader = DataLoader('mlops_python/Advertising.csv')

# Load and prepare data
X, y = data_loader.prepare_data()

# Split data into train and test sets
X_train, X_test, y_train, y_test = Preprocessor.train_test_split(X, y)

# Normalize features
X_train = Preprocessor.normalize(X_train)
X_test = Preprocessor.normalize(X_test)

# Initialize and train the model
model = LinearRegression(learning_rate=0.01, n_iterations=1000)
model.fit(X_train, y_train)

# Evaluate the model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
```

## Key Features

1. **Modularity**: Each component (data, model, preprocessing) is isolated in its own module
2. **Type Safety**: Extensive use of type hints for better code reliability
3. **Documentation**: Comprehensive docstrings for all classes and methods
4. **Flexibility**: Configurable parameters for model training and data preprocessing
5. **Reproducibility**: Random state control for consistent results

## Dependencies

- numpy>=1.21.0
- pandas>=1.3.0

## Installation

### Option 1: Install from PyPI (when published)
```bash
pip install mlops-python
```

### Option 2: Install from local source
```bash
# Clone the repository
git clone <repository-url>
cd mlops_package

# Install the package
pip install -e .
```

### Option 3: Install with development dependencies
```bash
pip install -e ".[dev]"
```

### Development Installation
For development, you might want to install additional tools:
```bash
pip install -e ".[dev]"
```

This will install:
- pytest: For running tests
- black: For code formatting
- flake8: For linting
- mypy: For type checking

## Best Practices Implemented

1. **Code Organization**:
   - Clear separation of concerns
   - Modular package structure
   - Proper use of Python packages with `__init__.py` files

2. **Data Handling**:
   - Clean data loading interface
   - Proper type conversion
   - Feature-target separation

3. **Model Implementation**:
   - Vectorized operations for efficiency
   - Configurable hyperparameters
   - Proper initialization of model parameters

4. **Preprocessing**:
   - Consistent normalization
   - Reproducible data splitting
   - Stateless preprocessing methods

5. **Documentation**:
   - Comprehensive docstrings
   - Clear README
   - Type hints for better code understanding 

## Running the Project

### Prerequisites
1. Python 3.7 or higher
2. pip (Python package installer)

### Step-by-Step Guide

1. **Clone the Repository**
```bash
git clone <repository-url>
cd mlops_package
```

2. **Create a Virtual Environment (Recommended)**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Example Script**
```bash
python example.py
```

### Expected Output
When you run the example script, you should see output similar to:
```
Training R-squared score: 0.XXXX
Testing R-squared score: 0.XXXX

Prediction for sample input: XX.XX
```

### Running Custom Experiments

You can create your own script to experiment with the package. Here's a template:

```python
from mlops_python.data.data_loader import DataLoader
from mlops_python.models.linear_regression import LinearRegression
from mlops_python.utils.preprocessor import Preprocessor

# Initialize components
data_loader = DataLoader('mlops_python/Advertising.csv')
model = LinearRegression(learning_rate=0.01, n_iterations=1000)

# Load and prepare data
X, y = data_loader.prepare_data()

# Split and normalize data
X_train, X_test, y_train, y_test = Preprocessor.train_test_split(X, y)
X_train = Preprocessor.normalize(X_train)
X_test = Preprocessor.normalize(X_test)

# Train and evaluate
model.fit(X_train, y_train)
print(f"Training score: {model.score(X_train, y_train):.4f}")
print(f"Testing score: {model.score(X_test, y_test):.4f}")
```

### Troubleshooting

1. **ImportError: No module named 'mlops_python'**
   - Make sure you're in the correct directory (mlops_package)
   - Verify that the virtual environment is activated
   - Check that all dependencies are installed

2. **FileNotFoundError: Advertising.csv**
   - Ensure the CSV file is in the correct location (mlops_package/mlops_python/Advertising.csv)
   - Verify the file path in your code

3. **ValueError: shapes not aligned**
   - Check that the input data dimensions match the expected format
   - Verify that the data preprocessing steps are applied correctly

### Additional Tips

1. **Experiment with Hyperparameters**
   - Try different learning rates (e.g., 0.001, 0.01, 0.1)
   - Adjust the number of iterations
   - Modify the test size in train-test split

2. **Visualize Results**
   - You can add visualization code using matplotlib or seaborn
   - Plot training curves or feature importance

3. **Save Model**
   - Add code to save the trained model using pickle or joblib
   - Save preprocessing parameters for future use 

### Serialization Features

The package includes model serialization capabilities through the `ModelSerializer` class:

1. **Model Saving and Loading**
   ```python
   from mlops_python.utils.serializer import ModelSerializer
   
   # Save model
   ModelSerializer.save_model(model, 'models/linear_regression_model.pkl')
   
   # Load model
   loaded_model = ModelSerializer.load_model('models/linear_regression_model.pkl')
   ```

2. **Metrics Saving**
   ```python
   metrics = {
       'train_score': train_score,
       'test_score': test_score
   }
   ModelSerializer.save_metrics(metrics, 'metrics/model_metrics.json')
   ```

3. **Directory Structure for Saved Files**
   ```
   mlops_package/
   ├── models/
   │   └── linear_regression_model.pkl
   └── metrics/
       └── model_metrics.json
   ```

### Expected Output with Serialization
When you run the example script, you'll see additional output:
```
Training R-squared score: 0.XXXX
Testing R-squared score: 0.XXXX

Model saved to 'models/linear_regression_model.pkl'
Metrics saved to 'metrics/model_metrics.json'

Prediction for sample input: XX.XX

Loading saved model...
Prediction using loaded model: XX.XX
Loaded model verified - predictions match original model
``` 