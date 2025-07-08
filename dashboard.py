import streamlit as st
import json

# Load scan results from file
with open("data_store.json", "r") as f:
    data = json.load(f)

st.title("DevSecOps Vulnerability Dashboard")


severity_filter = st.multiselect(
    "Select Severities to Display", ["LOW", "MEDIUM", "HIGH"],
    default=["LOW", "MEDIUM", "HIGH"]
)

# Display Code Vulnerabilities (Bandit)
st.header("Code Vulnerabilities (Bandit)")
code_issues = data.get("code_issues", [])

if code_issues:
    for issue in code_issues:
        if issue["severity"] in severity_filter:
            st.markdown(f"**File:** {issue['file']} (Line {issue['line']})")
            st.markdown(f"- **Issue:** {issue['issue']}")
            st.markdown(f"- **Severity:** {issue['severity']} | Score: {issue['risk_score']}")
            st.markdown(f"- **Prediction:** {'Real' if issue['likely_real'] else 'Possibly False Positive'}")
            st.markdown(f"- **Remediation:** {issue.get('remediation', 'See secure coding docs')}")
            st.markdown("---")
else:
    st.success("No code vulnerabilities found.")

# Display Container Vulnerabilities (Trivy)
st.header("Container Vulnerabilities (Trivy)")
container_results = data.get("container_results", {}).get("Results", [])

if container_results:
    for result in container_results:
        st.subheader(result.get("Target", ""))
        for vuln in result.get("Vulnerabilities", []):
            if vuln["Severity"] in severity_filter:
                st.markdown(f"- **Package:** {vuln['PkgName']}")
                st.markdown(f"- **Vuln ID:** {vuln['VulnerabilityID']} | Severity: {vuln['Severity']}")
                st.markdown(f"- **Fix Version:** {vuln.get('FixedVersion', 'N/A')}")
                st.markdown("---")
else:
    st.success("No container vulnerabilities found.")

# IaC Vulnerabilities
# Infrastructure-as-Code Issues (Checkov)
st.header("Infrastructure-as-Code Issues (Checkov)")

iac_issues = data.get("iac_results", {}).get("results", {}).get("failed_checks", [])

# ✅ Add this: map known check IDs to severity
severity_map = {
    "CKV_AWS_23": "LOW",
    "CKV_AWS_24": "HIGH",
    "CKV2_AWS_5": "MEDIUM"
}

if iac_issues:
    for check in iac_issues:
        # ✅ Use mapped severity if Checkov didn't provide one
        severity = check.get("severity") or severity_map.get(check["check_id"], "MEDIUM")

        if severity in severity_filter:
            st.markdown(f"**File:** {check['file_path']}")
            st.markdown(f"- **Issue:** {check['check_name']}")
            st.markdown(f"- **Check ID:** {check['check_id']}")
            st.markdown(f"- **Resource:** {check['resource']}")
            st.markdown(f"- **Guideline:** {check.get('guideline', 'N/A')}")
            st.markdown(f"- **Severity:** {severity}")
            st.markdown("---")
else:
    st.success("No IaC issues detected.")



