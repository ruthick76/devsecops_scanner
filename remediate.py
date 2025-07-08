def suggest_remediation(issue):
    issue_text = issue.get("issue", "").lower()

    if "eval" in issue_text:
        return "Avoid using 'eval'. Consider using 'ast.literal_eval' or a safer alternative."
    elif "assert" in issue_text:
        return "Avoid using 'assert' for security checks in production code."
    elif "hardcoded password" in issue_text:
        return "Store credentials in environment variables or a secrets manager."
    else:
        return "Review the code and apply secure coding best practices."
