# Git Basics Labs

## Lab 1: Git Installation and Configuration
1. **Install Git**:
2. **Verify Installation**:
   ```bash
   git --version
   ```
3. **Set Global Username and Email**:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```
4. **Check Configuration**:
   ```bash
   git config --list
   ```
---

## Lab 2: Initializing a Repository
1. **Create a New Directory**:
   ```bash
   mkdir git-lab
   cd git-lab
   ```
2. **Initialize Git**:
   ```bash
   git init
   ```
3. **Check Repository Status**:
   ```bash
   git status
   ```
4. **View the Hidden `.git` Directory**:
   ```bash
   ls -a
   ```
---

## Lab 3: Adding and Committing Files
1. **Create a File**:
   ```bash
   echo "Hello, Git!" > file.txt
   ```
2. **Check Status**:
   ```bash
   git status
   ```
3. **Stage the File**:
   ```bash
   git add file.txt
   ```
4. **Check Short Status**:
   ```bash
   git status -s
   ```
5. **Commit the Changes**:
   ```bash
   git commit -m "Initial commit"
   ```
6. **View Commit Log**:
   ```bash
   git log
   ```
---

## Lab 4: Removing Files from Git
1. **Create and Stage a File**:
   ```bash
   echo "Temporary file" > temp.txt
   git add temp.txt
   ```

2. **Commit the File**:
   ```bash
   git commit -m "Add temp.txt"
   ```

3. **Remove the File**:
   ```bash
   git rm temp.txt
   git commit -m "Remove temp.txt"
   ```
4. **Verify Removal**:
   ```bash
   git status
   ```
---

## Lab 5: Advanced Status Commands
1. Modify an Existing File:
   ```bash
   echo "New line" >> file.txt
   ```
2. View Status:
   ```bash
   git status
   ```
3. View Short Status:
   ```bash
   git status -s
   ```
   - `M file.txt`: Modified file
   - `A file.txt`: Added file
   - `D file.txt`: Deleted file

---

