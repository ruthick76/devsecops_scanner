import subprocess
import json

def run_bandit_scan(target_dir):
    result = subprocess.run(
        ["bandit", "-r", target_dir, "-f", "json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        print("Error parsing Bandit output.")
        return {"results": []}
