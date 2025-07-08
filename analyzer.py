def extract_issues(scan_results):
    issues = []
    for item in scan_results.get("results", []):
        issue = {
            "file": item["filename"],
            "line": item["line_number"],
            "issue": item["issue_text"],
            "severity": item["issue_severity"],
            "confidence": item["issue_confidence"],
            "cwe": item.get("cwe", {}).get("id", "N/A")
        }
        issues.append(issue)
    return issues
