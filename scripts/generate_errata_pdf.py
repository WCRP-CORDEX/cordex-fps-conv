import subprocess
import json
import re
import datetime
from weasyprint import HTML
from icecream import ic

# Step 1: Fetch issues with `gh` CLI
def fetch_issues_with_label(label):
    try:
        result = subprocess.run(
            ["gh", "issue", "list",
             "--label", label,
             "--state", "all",
             "--json", "number,title,createdAt,closedAt,body,state,url,labels"
            ],
            capture_output=True,
            text=True,
            check=True
        )
        issues = json.loads(result.stdout)
        return issues
    except subprocess.CalledProcessError as e:
        print(f"Error calling gh CLI: {e.stderr}")
        return []

# Step 2: Extract metadata from issue markdown
def extract_metadata(issue):
    body = issue['body']
    metadata = {
        "Date": datetime.datetime.fromisoformat(issue['createdAt'].replace("Z", "")).strftime('%Y-%m-%d'),  # Date only
        "Title": issue['title'],
        "Link": issue['url'], 
        "Status": issue['state'],
        "Variables": "",
        "Model": "",
        "Experiment": ""
    }
    headings = ["Variables", "Model", "Experiment"]
    for heading in headings:
        match = re.search(rf"#+ {heading}\s*(.+?)(?=\n#|$)", body, re.DOTALL)
        if match: 
            metadata[heading] = match.group(1).strip()
    return metadata

# Step 3: Generate styled HTML for the PDF
def generate_html(data):
    # Define table style
    style = """
    <style>
        body {
            font-family: Arial, sans-serif;
            font-size: 10pt;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ffffff;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f4f4f4;
            font-weight: bold;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr.status-wont-fix { background-color: #ffcccc; }
        tr.status-fixed { background-color: #ccffcc; }
        tr.status-open { background-color: #d1f2eb ; }
        a {color: DodgerBlue}
        a:link { text-decoration: none; }
        a:visited { text-decoration: none; }
        a:hover { text-decoration: underline; }
        a:active { text-decoration: underline;}
        @page {
          size: A4 landscape;
          margin: 5mm 5mm 5mm 5mm;
        }
    </style>
    """
    # Build HTML table
    rows = ""
    for row in data:
        status_class = f"status-{row['Status'].replace(' ', '-').lower()}"
        rows += f"""
        <tr class="{status_class}">
            <td>{row['Date']}</td>
            <td><a href="{row['Link']}" target="_blank">{row['Title']}</a></td>
            <td>{row['Variables']}</td>
            <td>{row['Model']}</td>
            <td>{row['Experiment']}</td>
            <td>{row['Status']}</td>
        </tr>
        """
    html = f"""
    <html>
    <head>{style}</head>
    <body>
        <h1>CORDEX-FPSCONV errata report</h1>
        This report was generated automatically on {datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M")} UTC from the "Errata"-labeled issues opened in the CORDEX-FPSCONV github repository, which can be found at <a href=\"https://github.com/WCRP-CORDEX/cordex-fps-conv/issues?q=is%3Aissue%20label%3AErrata\">https://github.com/WCRP-CORDEX/cordex-fps-conv/issues</a>. Please, check there for further detail on the issues and potential new known errors in the data.
        <table>
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Issue (with link to details)</th>
                    <th>Variables</th>
                    <th>Model</th>
                    <th>Experiment</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
    </body>
    </html>
    """
    return html

# Step 4: Convert HTML to PDF
def save_pdf(html_content, output_file):
    html = HTML(string=html_content)
    html.write_pdf(output_file, stylesheets=None, presentational_hints=True)

# Main script
if __name__ == "__main__":
    label = "Errata"
    issues = fetch_issues_with_label(label)
    #ic(issues) 
    parsed_data = [extract_metadata(issue) for issue in issues]
    parsed_data.sort(key=lambda x: x['Date'])  # Sort by date
    
    html_content = generate_html(parsed_data)
    pdf_file = f"CORDEX-FPSCONV_errata_v{datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d')}.pdf"
    save_pdf(html_content, pdf_file)
    print(f"PDF saved as {pdf_file}")

