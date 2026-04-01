import os
import shutil
import json
from datetime import datetime

commit_id = os.getenv("GITHUB_SHA", "local_commit")
author = os.getenv("GITHUB_ACTOR", "unknown_user")

artifact_name = f"v_{commit_id}"
artifact_dir = os.path.join("artifacts", artifact_name)


os.makedirs(artifact_dir, exist_ok=True)

shutil.copytree(".", artifact_dir, dirs_exist_ok=True)


metadata = {
    "artifact_name": artifact_name,
    "commit_id": commit_id,
    "author": author,
    "timestamp": str(datetime.now())
}

with open(os.path.join(artifact_dir, "metadata.json"), "w") as f:
    json.dump(metadata, f, indent=4)

print(f" Full repo artifact created: {artifact_dir}")