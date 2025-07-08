def simulate_ml_risk_score(issue):
    score = 0

    # Assign base score based on severity
    severity = issue.get("severity", "").upper()
    if severity == "HIGH":
        score += 3
    elif severity == "MEDIUM":
        score += 2
    else:
        score += 1

    # Adjust score based on confidence
    confidence = issue.get("confidence", "").upper()
    if confidence == "HIGH":
        score += 1.5
    elif confidence == "MEDIUM":
        score += 1

    # Add bonus if CWE is a known high-risk category
    high_risk_cwes = {"79", "89", "119", "200", "287", "352"}
    cwe = str(issue.get("cwe", ""))
    if cwe in high_risk_cwes:
        score += 1

    # Classify as likely real if score is high enough
    likely_real = score >= 4.5

    return {
        "ml_score": round(score, 2),
        "likely_real": likely_real
    }
