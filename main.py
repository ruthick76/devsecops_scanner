from scanner import run_bandit_scan
from analyzer import extract_issues
from prioritizer import prioritize_issues
from remediate import suggest_remediation
from container_scanner import scan_docker_image
from iac_scanner import run_checkov_scan
import json

def main():
    target_directory = "./code_to_scan"
    iac_directory = "./iac_code"
    container_image = "python:3.8-slim"

    print("Running Bandit scan...")
    raw_results = run_bandit_scan(target_directory)

    print("Analyzing results...")
    issues = extract_issues(raw_results)
    prioritized = prioritize_issues(issues)

    print("\nVulnerability Report:")
    for issue in prioritized:
        print(f"\nFile: {issue['file']} (Line {issue['line']})")
        print(f"Issue: {issue['issue']}")
        print(f"Severity: {issue['severity']} | Confidence: {issue['confidence']} | Risk Score: {issue['risk_score']}")
        print(f"Prediction: {'Real issue' if issue['likely_real'] else 'Possible false positive'}")
        print("-" * 50)

    print("\nScanning Docker container...")
    container_results = scan_docker_image(container_image)

    if container_results and container_results.get("Results"):
        for target in container_results["Results"]:
            for vuln in target.get("Vulnerabilities", []):
                print(f"\nPackage: {vuln.get('PkgName')}")
                print(f"Vuln ID: {vuln.get('VulnerabilityID')}")
                print(f"Severity: {vuln.get('Severity')}")
                print(f"Fixed Version: {vuln.get('FixedVersion')}")
                print("-" * 40)
    else:
        print("No major container vulnerabilities found.")

    print("\nScanning Infrastructure-as-Code (Terraform/Kubernetes)...")
    iac_results = run_checkov_scan(iac_directory)

    if "results" in iac_results:
        failed_checks = iac_results["results"].get("failed_checks", [])
        if failed_checks:
            print(f"Found {len(failed_checks)} IaC security issues:")
            for check in failed_checks[:5]:
                print(f"\nFile: {check['file_path']}")
                print(f"Issue: {check['check_name']} | Severity: {check.get('severity', 'UNKNOWN')}")
                print(f"Resource: {check['resource']}")
                print(f"Fix Recommendation: {check.get('guideline', 'N/A')}")
                print("-" * 40)
        else:
            print("No major misconfigurations found.")
    else:
        print("No Checkov results.")

    combined_results = {
        "code_issues": prioritized,
        "container_results": container_results,
        "iac_results": iac_results
    }

    with open("data_store.json", "w") as f:
        json.dump(combined_results, f, indent=4)

    print("\nScan results saved to 'data_store.json'. Run 'streamlit run dashboard.py' to view them.")

if __name__ == "__main__":
    main()
