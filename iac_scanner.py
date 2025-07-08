import subprocess
import json
import shutil
import os

def run_checkov_scan(directory):
    try:
        checkov_path = shutil.which("checkov")

        if not checkov_path:
            possible_paths = [
                os.path.expandvars(r"%APPDATA%\Python\Python311\Scripts\checkov.cmd"),
                os.path.expandvars(r"%APPDATA%\Python\Python312\Scripts\checkov.cmd"),
                os.path.expandvars(r"%APPDATA%\Python\Python313\Scripts\checkov.cmd"),
                os.path.expandvars(r"%LOCALAPPDATA%\Programs\Python\Python311\Scripts\checkov.cmd"),
                os.path.expandvars(r"%LOCALAPPDATA%\Programs\Python\Python312\Scripts\checkov.cmd"),
                os.path.expandvars(r"%LOCALAPPDATA%\Programs\Python\Python313\Scripts\checkov.cmd"),
            ]
            for path in possible_paths:
                if os.path.exists(path):
                    checkov_path = path
                    break

        if not checkov_path:
            print("Checkov executable not found. Please install it using: pip install checkov")
            return {}

        cmd = [checkov_path, "-d", directory, "-o", "json"]

        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        output = result.stdout.strip()

        if output.startswith("{") and "results" in output:
            return json.loads(output)
        else:
            print("Checkov returned no output.")
            print("STDERR:", result.stderr.strip())
            return {}

    except Exception as e:
        print("Error running Checkov:", e)
        return {}
