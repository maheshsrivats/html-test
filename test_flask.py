# test_flask.py
import os
import subprocess


# Use GitHub CLI to create a directory and upload the file
repo = "html-test"
branch = "python-code"
file_path = "dist/index.html"
commit_message = "Add build output"

# Add the file to the repository
subprocess.run(["gh", "repo", "clone", repo])
os.chdir(repo)
subprocess.run(["git", "checkout", branch])
subprocess.run(["mkdir", "-p", "dist"])
subprocess.run(["cp", "../dist/index.html", "dist/index.html"])
subprocess.run(["git", "add", "dist/index.html"])
subprocess.run(["git", "commit", "-m", commit_message])
subprocess.run(["git", "push", "origin", branch])

# Create the 'dist' directory if it doesn't exist
os.makedirs('dist', exist_ok=True)

# Write the output to 'index.html'
with open('dist/index.html', 'w') as f:
    f.write("helllooooooooooooo")
