# Git Foundations

This README contains basic Git commands and configurations for reference.

## Command Line Basics

### File System Navigation
- `pwd` - Print Working Directory: Shows the current directory path
- `ls` - List: Shows visible files and directories in current directory
- `ls -a` - List All: Shows both hidden and visible files and directories
- `cd <path_to_directory>` - Change Directory: Navigate to specified directory
- `cd ..` - Change Directory Up: Navigate to parent directory
- `mkdir <directory_name>` - Make Directory: Create a new directory/folder

## Git Commands

### Basic Git Commands
- `git commit -m "message"` - Commit changes with a message
  - Note: Use single dash (-) or double dash (--) for command options

## Git Configuration

### View Configuration
- `git config --global --list` - List all global Git configurations

### Set User Configuration
- `git config --global user.name "your_name"` - Set global Git username
- `git config --global user.email "your_email"` - Set global Git email

Example:
```bash
git config --global user.name "nachiketh"
git config --global user.email "murthy@manifoldailearning.in"
```