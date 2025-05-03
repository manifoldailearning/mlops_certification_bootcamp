# DVC Demo Project

This project demonstrates the use of Data Version Control (DVC) for managing data and machine learning workflows. The project uses a simple advertising dataset to showcase DVC's core features.

## Project Structure

```
.
├── Advertising.csv        # Raw dataset
├── Advertising.csv.dvc    # DVC metadata file for the dataset
├── example.py            # Example Python script
├── .dvc/                 # DVC configuration directory
├── .git/                 # Git configuration directory
├── .dvcignore           # DVC ignore patterns
└── .gitignore           # Git ignore patterns
```

## Prerequisites

- Python 3.x
- Git
- DVC
- pip (Python package manager)

## Setup Instructions

1. **Install DVC**
   ```bash
   pip install dvc
   ```

2. **Initialize DVC**
   ```bash
   dvc init
   ```

3. **Add Remote Storage**
   ```bash
   dvc remote add -d myremote /path/to/remote/storage
   ```

## Demo Steps

### 1. Adding Data to DVC

```bash
# Add the dataset to DVC
dvc add Advertising.csv

# Commit the changes to Git
git add Advertising.csv.dvc .gitignore
git commit -m "Add dataset to DVC"
```

### 2. Pushing Data to Remote Storage

```bash
# Push the data to remote storage
dvc push
```

### 3. Pulling Data

```bash
# Pull the data from remote storage
dvc pull
```

### 4. Version Control Workflow

1. Make changes to your data or code
2. Track changes with DVC:
   ```bash
   dvc add Advertising.csv
   ```
3. Commit changes to Git:
   ```bash
   git add Advertising.csv.dvc
   git commit -m "Update dataset"
   ```
4. Push changes to remote:
   ```bash
   dvc push
   ```

## Best Practices

- Always commit DVC metadata files (`.dvc` files) to Git
- Use `.dvcignore` to exclude unnecessary files from DVC tracking
- Keep your remote storage credentials secure
- Regularly push your data to remote storage

## Troubleshooting

If you encounter any issues:

1. Check DVC status:
   ```bash
   dvc status
   ```

2. Verify remote configuration:
   ```bash
   dvc remote list
   ```

3. Check for data corruption:
   ```bash
   dvc check-ignore
   ```

## Additional Resources

- [DVC Documentation](https://dvc.org/doc)
- [DVC GitHub Repository](https://github.com/iterative/dvc)
- [DVC Tutorials](https://dvc.org/doc/tutorials)

## License

This project is open source and available under the MIT License. 