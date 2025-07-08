from ml_model import simulate_ml_risk_score

def score_issue(issue):
    ml_result = simulate_ml_risk_score(issue)
    issue["risk_score"] = ml_result["ml_score"]
    issue["likely_real"] = ml_result["likely_real"]
    return issue["risk_score"]

def prioritize_issues(issues):
    for issue in issues:
        score_issue(issue)
    return sorted(issues, key=lambda x: x["risk_score"], reverse=True)
