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

## Local Repository Operations

### Repository Initialization
- `.git` - Hidden directory that represents a Git repository
- `git init` - Initialize a new Git repository in the current directory

### File Tracking
- `git status` - Check the status of files in the repository
  - Shows untracked, modified, and staged files

### Staging Files
- `git add <filename>` - Stage a single file for commit
- `git add <filename1> <filename2> <filename3>` - Stage multiple files for commit
- `git add .` - Stage all files in the current directory for commit

### Committing Changes
- `git commit -m "<message>"` - Commit staged changes with a descriptive message
- `git log` - View commit history with details like author, date, and commit messages

Example workflow:
```bash
# Initialize a new repository
git init

# Check status of files
git status

# Stage files for commit
git add example.txt
# or
git add file1.txt file2.txt
# or
git add .

# Commit the changes
git commit -m "Initial commit with example files"

# View commit history
git log
```

## Branching Operations

### Branch Management
- `git branch` - List all branches in the repository
  - Current branch is marked with an asterisk (*)
- `git branch <branch-name>` - Create a new branch
  - Note: This command only creates the branch, it doesn't switch to it

### Switching Branches
- `git switch <branch-name>` - Switch to the specified branch (modern command)
- `git checkout <branch-name>` - Switch to the specified branch (traditional command)
  - Note: `git checkout` has multiple uses, while `git switch` is specifically for changing branches

Example workflow:
```bash
# List all branches
git branch

# Create a new feature branch
git branch feature/new-feature

# Switch to the new branch
git switch feature/new-feature
# or
git checkout feature/new-feature

# Make changes and commit them
git add .
git commit -m "Add new feature implementation"
```

## Merging and Rebasing

### Git Merge
Merging combines the changes from one branch into another, creating a merge commit.

#### Basic Merge Commands
- `git merge <branch-name>` - Merge specified branch into current branch
- `git merge --no-ff <branch-name>` - Create a merge commit even if fast-forward is possible
- `git merge --abort` - Abort the current merge operation

#### Merge Example Workflow
```bash
# Start from main branch
git checkout main

# Merge feature branch into main
git merge feature/new-feature

# If there are conflicts, resolve them and then:
git add .
git commit -m "Merge feature/new-feature into main"
```

### Git Rebase
Rebasing moves or combines a sequence of commits to a new base commit, creating a linear history.

#### Basic Rebase Commands
- `git rebase <branch-name>` - Rebase current branch onto specified branch
- `git rebase -i <commit-hash>` - Interactive rebase to modify commits
- `git rebase --continue` - Continue rebase after resolving conflicts
- `git rebase --abort` - Abort the current rebase operation

#### Rebase Example Workflow
```bash
# Start from feature branch
git checkout feature/new-feature

# Rebase feature branch onto main
git rebase main

# If there are conflicts, resolve them and then:
git add .
git rebase --continue
```

### Merge vs Rebase Comparison

#### When to Use Merge
- When you want to preserve the complete history
- When working on public branches (like main/master)
- When multiple developers are working on the same branch

#### When to Use Rebase
- When you want a clean, linear project history
- When working on local feature branches
- Before merging a feature branch into main

#### Example Scenarios

1. **Merge Scenario**:
```bash
# On main branch
git checkout main
git merge feature/new-feature
# Creates a merge commit preserving both histories
```

2. **Rebase Scenario**:
```bash
# On feature branch
git checkout feature/new-feature
git rebase main
# Creates a linear history by moving feature commits to the tip of main
```

#### Best Practices
- Never rebase commits that have been pushed to a shared repository
- Use merge for public branches
- Use rebase for local feature branches
- Always test your changes after rebasing
- Keep commits small and focused when planning to rebase