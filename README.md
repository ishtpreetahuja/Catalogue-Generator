# Catalogue Generator

A Streamlit-based web application that generates PDF catalogues for products based on selected categories and brands. The application supports data synchronization with Google Sheets and automated email delivery of generated catalogues.

## Features

- Web-based GUI using Streamlit
- Generate PDF catalogues based on:
  - Primary Category
  - Secondary Category
  - Brand
- Sync product data from Google Sheets
- Automatic email delivery of generated catalogues
- Support for multiple categories and brands
- Image handling for products and brand logos

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/catalogue-generator.git
    cd catalogue-generator
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a [.env](http://_vscodecontentref_/1) file in the [utils](http://_vscodecontentref_/2) directory with the following content:
    ```plaintext
    RECEIVER-EMAIL=your-email@gmail.com
    RECEIVER-PASSWORD=your-app-password
    TO-EMAIL=recipient-email@gmail.com
    ```

5. **Add your data**:
    - Place your data in the [data.csv](http://_vscodecontentref_/3) file
    - Required columns: "SKU", "Brand", "Primary Category", "Secondary Category", "Price", "Technical Details"

6. **Add your Google Sheets credentials**:
    Place your Google Sheets credentials in the [credentials-gsheet.json](http://_vscodecontentref_/4) file.

7. **Add product and brand images**:
    - Product images: Place in [items](http://_vscodecontentref_/5) with SKU as filename (e.g., `GWS600.jpg`)
    - Brand logos: Place in [brands](http://_vscodecontentref_/6) with brand name as filename (e.g., `bosch.png`)

## Usage

1. **Start the application**:
    ```sh
    python main.py
    ```

2. **Using the web interface**:
    - Select Primary Category from dropdown
    - Select Secondary Category from dropdown
    - Select Brand from dropdown
    - Click "Generate PDF" to create and email the catalogue
    - Click "Sync Data" to update local data from Google Sheets
    - Click "Create New Entry" to reset selections

## Project Structure

- [input_gui.py](http://_vscodecontentref_/7): Streamlit web interface
- [pdf_gen.py](http://_vscodecontentref_/8): PDF generation logic
- [email_sender.py](http://_vscodecontentref_/9): Email functionality
- [sync_local.py](http://_vscodecontentref_/10): Google Sheets synchronization
- [layouts](http://_vscodecontentref_/11): HTML templates and assets

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License.