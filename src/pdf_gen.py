import pandas as pd
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from email_sender import send_email
import os

def file_exists(path):
    return os.path.isfile(path)

def generator(primary_category=None, secondary_category=None, brand=None):
    print(f"Generating PDF catalogue for: {primary_category}, {secondary_category}, {brand}")

    # Load data from a local CSV file
    df = pd.read_csv("utils/data.csv")
    print(f"Debug - Available columns: {df.columns.tolist()}")

    # Filter rows based on the inputs
    filtered_df = df.copy()
    if primary_category:
        filtered_df = filtered_df[filtered_df["Primary Category"].str.lower() == primary_category.lower()]
    if secondary_category:
        filtered_df = filtered_df[filtered_df["Secondary Category"].str.lower() == secondary_category.lower()]
    if brand:
        filtered_df = filtered_df[filtered_df["Brand"].str.lower() == brand.lower()]

    print(f"Debug - Found {len(filtered_df)} matching rows")

    # Add serial number column
    filtered_df.reset_index(drop=True, inplace=True)
    filtered_df['sno'] = filtered_df.index + 1

    # Determine the template to use based on the primary category
    if primary_category:
        template_name = f"src/layouts/{primary_category.lower().replace(' ', '')}.html"
        if not file_exists(template_name):
            print(f"Debug - Template {template_name} not found. Reverting to default template.")
            template_name = "src/layouts/powertools.html"
    else:
        template_name = "src/layouts/powertools.html"

    # Load Jinja2 template
    env = Environment(loader=FileSystemLoader("."))
    env.filters['file_exists'] = file_exists  # Register the custom filter
    template = env.get_template(template_name)

    # Convert "Price" column to int
    if "Price" in filtered_df.columns:
        filtered_df["Price"] = filtered_df["Price"].astype(int)
    
    # Render template with filtered DataFrame data
    html_content = template.render(data=filtered_df.to_dict(orient="records"), sub_head=f"{primary_category or ''} {secondary_category or ''}  {brand or ''}")

    # Define the output PDF path
    primary_filename = primary_category.lower().strip().replace(" ", "-") if primary_category else "catalogue"
    filename = primary_filename
    if secondary_category:
        secondary_filename = secondary_category.lower().strip().replace(" ", "-")
        filename = f"{primary_filename}_{secondary_filename}"
    if brand:
        brand_filename = brand.lower().strip().replace(" ", "-")
        filename = f"{filename}_{brand_filename}"
    output_pdf_path = f"{filename}.pdf"

    # Convert to PDF
    HTML(string=html_content, base_url='.').write_pdf(output_pdf_path)
    print("PDF generated successfully!")

    # Send email
    send_email(subject=f"Catalogue for {primary_category or 'All'} - {secondary_category or 'All'} - {brand or 'All'}", attachment_path=output_pdf_path)
    print("Email sent successfully!")

if __name__ == '__main__':
    generator("Spare Parts", "ASM04-100A")