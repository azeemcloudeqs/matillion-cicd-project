import os
import shutil
import json
from datetime import datetime

# 🔹 Get GitHub environment variables
commit_id = os.getenv("GITHUB_SHA", "local_commit")
author = os.getenv("GITHUB_ACTOR", "unknown_user")
branch = os.getenv("GITHUB_REF_NAME", "local")

# 🔹 Artifact naming
artifact_name = f"v_{commit_id}"
artifact_dir = os.path.join("artifacts", artifact_name)

# 🔹 Create artifact directory
os.makedirs(artifact_dir, exist_ok=True)


folders_to_include = [
    "matillion",   # your pipelines (IMPORTANT)
    "scripts"      # optional (only if needed for deploy)
]

for folder in folders_to_include:
    if os.path.exists(folder):
        shutil.copytree(
            folder,
            os.path.join(artifact_dir, folder),
            dirs_exist_ok=True
        )
    else:
        print(f" Folder not found, skipping: {folder}")



files_to_include = [
    "README.md"
]

for file in files_to_include:
    if os.path.exists(file):
        shutil.copy(file, artifact_dir)



metadata = {
    "artifact_name": artifact_name,
    "commit_id": commit_id,
    "author": author,
    "branch": branch,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "description": "Matillion CI/CD Artifact"
}

with open(os.path.join(artifact_dir, "metadata.json"), "w") as f:
    json.dump(metadata, f, indent=4)


print(f" Artifact created successfully")
print(f" Location: {artifact_dir}")
print(f" Version: {artifact_name}")
