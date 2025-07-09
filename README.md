 
 
# 🛡️ DevSecOps Vulnerability Scanner

A lightweight Python-based scanner that integrates static code analysis, container scanning, and infrastructure-as-code checks into a unified dashboard. Ideal for DevSecOps pipelines and secure development workflows.

 

## 📂 Project Structure

 

 
devsecops_scanner\
├── code_to_scan\
│   └── app.py\
├── workflow\
│   └── devsecops.yml\
├── iac_code\
│   └── main.tf\
├── dashboard.py\
├── main.py\
├── data_store.json\
├── scanner.py\
├── analyzer.py\
├── container_scanner.py\
├── iac_scanner.py\
├── ml\_model.py                   
├── prioritizer.py    
├── remediaite.py 

 



## 🚀 Features

- Bandit – scans Python code for security issues.
- Trivy– scans Docker images for vulnerabilities.
- Checkov – scans Terraform/Kubernetes for misconfigurations.
- ML Simulation – scores issues to help prioritize remediation.
- Streamlit UI – interactive dashboard with severity filters.

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/devsecops_scanner.git
cd devsecops_scanner
````

### 2. Install dependencies

You may need to install Trivy and Checkov manually:

```bash
pip install bandit checkov streamlit
 ```

Ensure Trivy is installed:

```bash
choco install trivy  # On Windows (with Chocolatey)
 ```

Or download from [https://github.com/aquasecurity/trivy](https://github.com/aquasecurity/trivy)


## ✅ Usage

### Run all scans and save results

```bash
python main.py
 ```

This scans:

* Python code in `your_code_to_scan/`
* Docker image in `your_container/`
* Terraform/Kubernetes files in `iac_code/`

### Launch the dashboard

```bash
streamlit run dashboard.py
 
```
---

## 📊 Dashboard Features

* Filter vulnerabilities by severity (`LOW`, `MEDIUM`, `HIGH`)
* View results grouped by:

  * Code vulnerabilities (Bandit)
  * Container vulnerabilities (Trivy)
  * IaC issues (Checkov)
* Includes ML-predicted risk scores

---
 
 
