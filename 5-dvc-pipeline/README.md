
### DVC Pipeline Management

#### Creating Pipelines
```bash
# Create a pipeline stage
dvc run -n prepare \
        -d src/prepare.py -d data/raw/ \
        -o data/prepared/ \
        python src/prepare.py data/raw/ data/prepared/

# Create a training stage
dvc run -n train \
        -d src/train.py -d data/prepared/ \
        -o model/model.pkl \
        python src/train.py data/prepared/ model/model.pkl
```

#### Pipeline Operations
```bash
# Reproduce the entire pipeline
dvc repro

# Reproduce a specific stage
dvc repro prepare

# Show pipeline graph
dvc dag

# List all pipeline stages
dvc stage list
```

### Data Management

#### Removing Data
```bash
# Remove tracked data (keeps DVC metadata)
dvc remove data/raw/dataset.csv

# Remove data and its DVC metadata
dvc remove --force data/raw/dataset.csv

# Remove all tracked data
dvc gc --workspace
```

#### Moving/Renaming Data
```bash
# Move tracked data
dvc move data/old_location/ data/new_location/

# Rename tracked file
dvc move data/old_name.csv data/new_name.csv
```

### DVC Configuration

#### Remote Storage Configuration
```bash
# Add S3 remote
dvc remote add myremote s3://mybucket/path
dvc remote modify myremote endpointurl https://s3.amazonaws.com

# Add Google Cloud Storage remote
dvc remote add myremote gs://mybucket/path

# Add Azure Blob Storage remote
dvc remote add myremote azure://mycontainer/path
```

#### Cache Configuration
```bash
# Set cache directory
dvc cache dir /path/to/cache

# Configure cache type
dvc cache type reflink,symlink,copy

# Set cache size limit
dvc cache size 10GB
```

### DVC Best Practices

#### Workflow Guidelines
1. **Data Organization**:
   - Keep raw data immutable
   - Use clear directory structure
   - Separate code and data
   - Use meaningful file names

2. **Version Control**:
   - Commit DVC files with Git
   - Use descriptive commit messages
   - Tag important versions
   - Keep .gitignore updated

3. **Pipeline Management**:
   - Make stages atomic
   - Document dependencies
   - Use parameters for configuration
   - Test pipelines regularly

4. **Storage Management**:
   - Use appropriate remote storage
   - Monitor storage usage
   - Clean up unused data
   - Backup important versions

#### Common DVC Commands Cheat Sheet
```bash
# Initialize
dvc init

# Track data
dvc add <file/dir>

# Version control
dvc commit
dvc push
dvc pull

# Pipeline
dvc run
dvc repro
dvc dag

# Data management
dvc remove
dvc move
dvc gc

# Configuration
dvc remote
dvc cache
dvc config

# Status and information
dvc status
dvc list
dvc metrics
```

### Troubleshooting DVC

#### Common Issues and Solutions
1. **Cache Issues**:
   ```bash
   # Reset cache
   dvc cache clear
   
   # Fix cache corruption
   dvc cache verify
   ```

2. **Remote Storage Issues**:
   ```bash
   # Check remote connection
   dvc remote list
   
   # Verify remote configuration
   dvc remote default myremote
   ```

3. **Pipeline Issues**:
   ```bash
   # Check pipeline status
   dvc status
   
   # Force pipeline reproduction
   dvc repro --force
   ```

4. **Data Tracking Issues**:
   ```bash
   # Check tracked files
   dvc list .
   
   # Update tracking
   dvc update
   ```


# Push to Repo:

```
dvc remote add -d registry s3://dvcdemo-nachiketh/
dvc push -r registry

git tag best_model_v1
git push origin best_model_v1
```

# New System
# Pull model from Registry

```
git clone https://github.com/your-user/your-repo.git
cd dvc_model_registry_demo

# Checkout the best model tag
git checkout best_model_v1

# Pull model from registry
dvc pull -r registry models/model.pkl
```