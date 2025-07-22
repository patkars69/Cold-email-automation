Cold Email Automation Pipeline


Automate your job search and HR outreach with a robust, Python-powered workflow. This project lets you send engaging, personalized emails (with your resume attached) to hundreds of HR contacts in batches—while logging responses live in Excel and making every interaction count.

🚀 Features
Batch Sending: Emails go out in batches (default 100 per run), keeping you safe from Gmail limits.

Smart Reply Checks: Detects previous replies before emailing and prevents duplicates.

Live Excel Logging: Updates hr_contacts.xlsx in real time, tracking who was sent and who has replied.

Dynamic Personalization: Every message features a real, custom line for the company.

Resume Attachment: Attaches your resume from a dedicated folder automatically.

Idempotent: Each run only contacts new HRs—never doubles up or misses status.

Configurable & Open Source: Set it up with your Google account for full privacy and control.

📂 Project Structure
text
cold_email_pipeline/
├── batched_email_pipeline.py        # Main batch sending & reply-check script
├── hr_contacts.xlsx                 # Contact tracker: all HRs & statuses
├── resume/
│   └── Shashwat Patkar Resume.pdf   # Your resume for attachment
├── credentials/
│   ├── credentials.json             # Your own Google OAuth API file (instructions below)
│   └── token.json                   # Generated automatically on first run
├── venv/                            # Python virtual environment (not version controlled)
🔑 About the credentials Folder & Google OAuth Setup
Why Use Your Own Google OAuth API?
For secure, authorized access to your Gmail account, you must create your own OAuth credentials via Google Cloud.

Never share your credentials files online, and always use your own for privacy.

How to Obtain and Configure credentials.json:
Go to the Google Cloud Console

Create/Open a Project:

Click the project drop-down, then "New Project" (or use existing).

Enable Gmail API:

From "APIs & Services", select "Enable APIs and Services" and find "Gmail API".

Click "Enable".

Configure OAuth Consent Screen:

Under "APIs & Services" > "OAuth consent screen", set up an External user type and complete the minimal config.

Create OAuth Client ID:

Go to "APIs & Services" > "Credentials" > "Create Credentials" > "OAuth client ID".

Choose "Desktop app" as application type.

Name it (e.g., "cold-email-pipeline").

Download the credentials.json file when prompted.

Place credentials.json in your project's credentials/ folder.

First Run:

When you first run the script, you'll be prompted to log in with your Google account in a browser.

This will generate a token.json in the credentials folder for future runs.

🛠️ Setup Instructions
1. Clone and Prepare
bash
git clone https://github.com/yourusername/cold-email-automation.git
cd cold-email-automation
2. Create & Activate Virtual Environment
bash
python -m venv venv
# Command Prompt
venv\Scripts\activate
# PowerShell
.\venv\Scripts\Activate
3. Install Dependencies
bash
pip install pandas openpyxl google-auth google-auth-oauthlib google-api-python-client
4. Insert Your Data and Credentials
Place your resume PDF in the resume/ folder.

Add your credentials.json file as described above to the credentials/ folder.

Prepare and confirm your hr_contacts.xlsx (see format below).

📊 Excel File Format
Name	Email	Company Name	Personalized Line	Status	Reply
Jane HR	jane@company.com	ABC Ltd			
Hari Singh	hari@xyz.org	XYZ Inc			
Status: ✅ when your email is sent.

Reply: ✅ if a reply is detected from this contact.

✉️ How Sending Works
Script finds all HR contacts not yet emailed to or replied.

Processes the next batch (default 100), for each HR:

Checks for replies—if present, logs and skips.

If not sent before, generates a dynamic, personal line.

Mails the HR with your resume attached.

Logs result in Excel.

Re-run anytime to progress through the list—never duplicates.

💬 Example Email Body
text
Hi [HR Name],

I’ve taken a close look at the way [Company] approaches technology and quality—and I’m genuinely impressed. Your team's recent strides in innovative testing solutions inspired me to reach out.

As someone who thrives on bringing both automation and AI-driven insights into modern QA, I’d love to discuss where my experience might help accelerate your goals. If you're open to connecting, I’d be thrilled to share a few ideas or learn what challenges your team is tackling right now.

I’ve attached my resume for your review, and hope we might chat soon!

Warm regards,
Shashwat Patkar
🏁 How to Run
bash
python batched_email_pipeline.py
Each run processes the next eligible group of HR contacts, always updating your log and never sending twice.

🔧 Customization
Batch Size: Change BATCH_SIZE in batched_email_pipeline.py.

Personalization: Edit generate_personalized_line() in the script.

📋 License
MIT License

🤝 Credits & Contact
Created by Shashwat Patkar
[Add your GitHub/LinkedIn here]

Suggestions and contributions welcome!
