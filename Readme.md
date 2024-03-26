## Blockchain Code Security Audit Using ChatGPT

This Python script automates the generation of security audit reports for blockchain code using OpenAI's ChatGPT. By providing the blockchain source code, the script generates a detailed report following industry-standard practices. The report includes an executive summary, vulnerability analysis, best practices and considerations, and testing and audit methodology sections.

### How it Works

The script operates in the following steps:

1. Reads the blockchain source code from specified files (Solidity files in this example).
2. Constructs a prompt template for the ChatGPT model, outlining the structure of the audit report and incorporating the code content.
3. Utilizes OpenAI's ChatGPT model to generate a detailed security audit report based on the provided code.
4. Saves the generated audit report to a text file.

### Requirements

To run this script, ensure you have the following:

- Python installed on your system (version 3.x recommended).
- OpenAI API key for accessing the ChatGPT model.
- Necessary Python packages installed (specified in `requirements.txt`).

### Changes You Can Make

- Adjust the `prompt_template` variable to customize the structure and content of the audit report as per your requirements.
- Modify the code to support different programming languages or file formats for blockchain code.
- Enhance the script to handle multiple blockchain code files simultaneously for batch processing.

### How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/mominalix/Blockchain-Code-Security-Audit-Using-ChatGPT.git
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Replace `"API KEY"` in the script with your actual OpenAI API key.

4. Place your blockchain source code files (Solidity files in this example) in the `test_files` directory.

5. Run the script:

   ```bash
   python Auditor.py
   ```

6. The generated audit reports will be saved as text files with the suffix "_audit_report.txt" in the same directory as the source code files.
