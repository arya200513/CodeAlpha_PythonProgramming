import re

def extract_emails():
    print("Email Extractor from Text File")
    input_path = input("Enter path to input .txt file: ")

    try:
        with open(input_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return
    except IOError:
        print("Error reading the file. Please try again.")
        return

    # Regex pattern for emails
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    unique_emails = sorted(set(emails))

    if not unique_emails:
        print("No email addresses found in the file.")
        return

    output_path = "extracted_emails.txt"
    with open(output_path, 'w') as f:
        for email in unique_emails:
            f.write(email + '\n')

    print(f"Extracted {len(unique_emails)} unique email(s).")
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    extract_emails()
