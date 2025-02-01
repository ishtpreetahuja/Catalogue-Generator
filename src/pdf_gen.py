import pandas as pd
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from src.email_sender import send_email

def generator(body, to_email=None, subject=None):
    print(f"Generating PDF catalogue for input: {body}")
    
    # Clean the input string
    body = body.strip()
    print(f"Debug - Cleaned input: '{body}'")

    # Load data from a local CSV file
    df = pd.read_csv("utils/data.csv")
    print(f"Debug - Available columns: {df.columns.tolist()}")
    print(f"Debug - Sample values in Primary Category: {df['Primary Category'].unique()}")

    # Detect the column based on the input (case insensitive)
    column = None
    for col in df.columns:
        if body.lower() in df[col].str.lower().values:
            column = col
            break

    if column is None:
        print(f"No matching column found for input: '{body}'")
        return False

    # Filter rows based on the detected column (case insensitive)
    filtered_df = df[df[column].str.lower() == body.lower()]
    print(f"Debug - Found {len(filtered_df)} matching rows")

    # Determine the template to use
    if column == "Primary Category":
        template_name = f"src/layouts/{body.lower().replace(' ', '')}.html"
    else:
        template_name = "src/layouts/defaultlayout.html"

    # Load Jinja2 template
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(template_name)

    # Render template with filtered DataFrame data
    html_content = template.render(data=filtered_df.to_dict(orient="records"), sub_head=body)

    # Define the output PDF path
    output_pdf_path = f"output_{body.lower().replace(' ', '_')}.pdf"

    # Convert to PDF
    HTML(string=html_content).write_pdf(output_pdf_path)
    print("PDF generated successfully!")

    # Send email if recipient details are provided
    if to_email and subject:
        try:
            send_email(to_email, f"REPLY TO {body}", 
                       "Please find the requested catalogue attached.", 
                       output_pdf_path)
            print("Email sent successfully!")
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

    return output_pdf_path