import pandas as pd
import os
import base64
import pickle
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# CONFIGURABLE SETTINGS
BATCH_SIZE = 100  # Number of emails to send per batch/run
CREDENTIALS_FILE = 'credentials/credentials.json'
TOKEN_FILE = 'credentials/token.json'
HR_CONTACTS_FILE = 'hr_contacts.xlsx'
RESUME_PATH = 'resume/Shashwat Patkar Resume.pdf'

SCOPES = ['https://www.googleapis.com/auth/gmail.modify', 'https://www.googleapis.com/auth/gmail.send']

def gmail_authenticate():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

def has_replied(service, hr_email):
    query = f'from:{hr_email} in:inbox'
    results = service.users().messages().list(userId='me', q=query).execute()
    return bool(results.get('messages'))

def create_message(to_email, subject, message_text, attachment_path):
    message = MIMEMultipart()
    message['to'] = to_email
    message['subject'] = subject
    message.attach(MIMEText(message_text, 'plain'))
    with open(attachment_path, 'rb') as file:
        attach_part = MIMEApplication(file.read(), Name=os.path.basename(attachment_path))
    attach_part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
    message.attach(attach_part)
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def generate_personalized_line(company_name):
    return f"I'm excited by {company_name}'s approach to test automation and innovation."

def main():
    # Load contacts and prepare next batch of unsent/unreplied HRs
    df = pd.read_excel(HR_CONTACTS_FILE, engine='openpyxl')
    unsent = df[(df["Status"] != "✅") & (df["Reply"] != "✅")]
    batch_contacts = unsent.iloc[:BATCH_SIZE]
    if batch_contacts.empty:
        print("No unsent HRs left in the file.")
        return

    # Connect to Gmail
    service = gmail_authenticate()
    for idx in batch_contacts.index:
        email = df.at[idx, 'Email']
        status = str(df.at[idx, 'Status']).strip() if 'Status' in df else ''
        reply = str(df.at[idx, 'Reply']).strip() if 'Reply' in df else ''

        # Check inbox for reply before sending
        if has_replied(service, email):
            df.at[idx, 'Reply'] = '✅'
            print(f'Reply found from {email}, logging in Excel and skipping email.')
            continue
        if status == '✅':
            print(f'Email already sent to {email}, skipping.')
            continue

        name = df.at[idx, 'Name']
        company = df.at[idx, 'Company Name']
        subject = f"Opportunities at {company}"
        personalized_line = generate_personalized_line(company)
        body = (f"Hi {name},\n\n"
        f"I’ve taken a close look at the way {company} approaches technology and quality—and I’m genuinely impressed. "
        "Your team's recent strides in innovative testing solutions inspired me to reach out.\n\n"
        f"As someone who thrives on bringing both automation and AI-driven insights into modern QA, I’d love to discuss where my 	experience might help accelerate your goals. "
        "If you're open to connecting, I’d be thrilled to share a few ideas or learn what challenges your team is tackling right now.\n\n"
        "I’ve attached my resume for your review, and hope we might chat soon!\n\n"
        "Warm regards,\n"
        "Shashwat Patkar")

        try:
            message = create_message(email, subject, body, RESUME_PATH)
            service.users().messages().send(userId='me', body=message).execute()
            df.at[idx, 'Status'] = '✅'
            print(f'Sent email to {email}')
        except Exception as e:
            print(f'Failed to send email to {email}: {e}')

    # Save all updates to the Excel file
    df.to_excel(HR_CONTACTS_FILE, index=False, engine='openpyxl')
    print(f'Batch complete. Status and replies have been logged in {HR_CONTACTS_FILE}.')

if __name__ == '__main__':
    main()
