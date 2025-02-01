# Catalogue Generator

This project is an automated email-based catalogue generator. It listens for specific email subjects, generates a PDF catalogue based on the email content, and sends the generated PDF as an email attachment.

## Features

- Detects emails with specific subjects
- Generates PDF catalogues based on email content
- Sends the generated PDF as an email attachment
- Supports multiple categories and brands


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
    Create a `.env` file in the [utils](http://_vscodecontentref_/3) directory with the following content:
    ```plaintext
    RECEIVER-EMAIL=your-email@gmail.com
    RECEIVER-PASSWORD=your-app-password
    ```

5. **Add your data**:
    Place your data in the [data.csv](http://_vscodecontentref_/4) file. Ensure it has columns like "Brand", "Primary Category", "Secondary Category", etc.

6. **Add your Google Sheets credentials**:
    Place your Google Sheets credentials in the [credentials-gsheet.json](http://_vscodecontentref_/5) file.

## Usage

1. **Run the main script**:
    ```sh
    python main.py
    ```

2. **Send an email**:
    - To generate a catalogue, send an email with the subject "Send catalogue" and the body containing the category or brand.
    - To sync data, send an email with the subject "sync".

## Example

- **Email Subject**: Send catalogue
- **Email Body**: Power Tools

The script will generate a PDF catalogue for "Power Tools" and send it as an email attachment.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License.