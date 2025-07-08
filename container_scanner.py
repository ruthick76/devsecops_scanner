import subprocess
import json

def scan_docker_image(image_name):
    try:
        result = subprocess.run(
            ["trivy", "image", "--format", "json", image_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        if result.stdout:
            return json.loads(result.stdout)
        else:
            print("Trivy did not return any output.")
            return {}

    except Exception as e:
        print("Error scanning container:", e)
        return {}
