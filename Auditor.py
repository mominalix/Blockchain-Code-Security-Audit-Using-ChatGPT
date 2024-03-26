import os
import openai
from openai import OpenAI

# Replace with your actual OpenAI API key
client = OpenAI(
    # This is the default and can be omitted
    api_key="API-KEY",
)


# Customize this prompt as needed (from the previous response)
prompt_template = """
Subject: Blockchain Security Audit Report Generation

Task:  You will be provided with blockchain source code (e.g., smart contracts in Solidity). Analyze the code and generate a detailed security audit report adhering to industry-standard practices. The report should have the following structure:

1. Executive Summary

Brief overview of the audited code's functionality and purpose.
High-level summary of critical findings and potential risks.
Overall severity assessment of vulnerabilities (Critical, High, Medium, Low).
Version of compilers, libraries, or frameworks.

2. Vulnerability Analysis

For each discovered vulnerability:
Description: Clear and concise explanation of the vulnerability's nature.
Impact: Potential consequences if exploited.
Code Snippet: Highlight relevant lines of code demonstrating the flaw.
Remediation: Specific recommendations on how to fix the issue.
References: Link to any relevant external resources, CVEs (Common Vulnerabilities and Exposures), or similar reports if applicable.

3.Best Practices and Considerations

* Highlight whether the code adheres to established blockchain security guidelines and standards.
* Recommendations for improvements even if not strictly classified as vulnerabilities (e.g., optimization, gas efficiency, code clarity).

4.Testing and Audit Methodology

* Describe the testing strategies employed (e.g., unit tests, integration tests, fuzzing).
* Mention any automated tools used in the auditing process.

Code Submission:
"""

def generate_audit_report(code_content):
    prompt = prompt_template + "\n" + code_content 
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4", # Adjust as needed
        max_tokens=1024,  # Adjust as needed
        temperature=0.1,  # Adjust as needed
    )
    print ('\n\n\n',response.choices[0].message.content,'\n\n\n')
    return response.choices[0].message.content

def process_code_file(file_path):
    with open(file_path, "r") as file:
        code_content = file.read()
    audit_report = generate_audit_report(code_content)

    # Save the report
    report_file_name = os.path.splitext(file_path)[0] + "_audit_report.txt"
    with open(report_file_name, "w") as report_file:
        report_file.write(audit_report)

if __name__ == "__main__":
    test_folder = "test_files"  # Replace with your folder's path
    for filename in os.listdir(test_folder):
        if filename.endswith(".sol"):  # Example for Solidity, adjust for your language
            file_path = os.path.join(test_folder, filename)
            process_code_file(file_path)
            print(f"Audit report generated for {filename}")
