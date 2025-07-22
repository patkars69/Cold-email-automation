# Cold Email Automation Pipeline

Automate your job search and HR outreach with a robust, Python-powered workflow. This project lets you send engaging, personalized emails (with your resume attached) to hundreds of HR contacts in batches—while logging responses live in Excel and making every interaction count.

## 🚀 Features

- **Batch Sending:** Emails go out in batches (default 100 per run), keeping you safe from Gmail limits.  
- **Smart Reply Checks:** Detects previous replies before emailing and prevents duplicates.  
- **Live Excel Logging:** Updates `hr_contacts.xlsx` in real time, tracking who was sent and who has replied.  
- **Dynamic Personalization:** Every message features a real, custom line for the company.  
- **Resume Attachment:** Attaches your resume from a dedicated folder automatically.  
- **Idempotent:** Each run only contacts new HRs—never doubles up or misses status.  
- **Configurable & Open Source:** Set it up with your Google account for full privacy and control.

## 📂 Project Structure

cold_email_pipeline/

├── batched_email_pipeline.py # Main script to batch-send emails & log replies

├── hr_contacts.xlsx # Excel file with all HR contacts (and columns like Status/Reply)

├── resume/

│ └── Shashwat Patkar Resume.pdf # Your resume, attached automatically to each email

├── credentials/

│ ├── credentials.json # Your Gmail API OAuth credentials (see setup below)

│ └── token.json # Auto-generated token after first script run


---

## 🔧 Setup Instructions

### 1. 📄 Prepare Your Files

- Fill in your HR contact data in `hr_contacts.xlsx` with these columns:
Name | Email | Company Name | Personalized Line | Status | Reply


- Place your resume in the `resume/` folder.

- You’ll also need to set up **Google OAuth API** access to use Gmail services.

---

### 2. 🔐 Enable Gmail API & Create `credentials.json`

> **Follow these exact steps to enable Gmail API and get your personal `credentials.json` file:**

#### 🔁 One-Time OAuth Setup

1. Visit the [Google Cloud Console](https://console.cloud.google.com/).
2. Click **"Select a project"** → then **"New Project"** → name it something like `Cold Email Pipeline`.
3. After creating the project, search for **“Gmail API”** in the top search bar and **enable** it.
4. Go to **APIs & Services > Credentials**.
5. Click **"Create Credentials" → "OAuth client ID"**.
6. You’ll be prompted to configure the **OAuth Consent Screen**:
 - Choose **"External"** user type
 - Fill in **App name**, **email**, etc.
 - Add **Scopes**: `../auth/gmail.send`, `../auth/gmail.readonly`
 - Add **Test Users** (your Gmail account)
7. After saving, under **OAuth Client ID**:
 - Select **Application type: Desktop App**
 - Name it and click **Create**
8. Download the `credentials.json` file and place it in:

   cold_email_pipeline/credentials/credentials.json


> ⚠️ Keep this file secure — it contains your private API credentials.

---

### 3. 🛠️ Installation & First Run

From your project root, run:

Bash - 

# Activate virtual environment
.\venv\Scripts\Activate

# Install required libraries
pip install pandas openpyxl google-auth google-auth-oauthlib google-api-python-client

# Run the pipeline
python batched_email_pipeline.py

✅ On first run, a browser window will open asking you to log into your Gmail account and allow access. A token.json file will be generated and reused on future runs.

🧠 How It Works
Selects today's batch from hr_contacts.xlsx.

Checks for existing replies in your Gmail inbox.

Skips HRs who replied or were already sent an email.

Generates personalized content, attaches your resume, and sends the email.

Logs the result back to Excel (✅ for sent, replied, or skipped).

📈 Example: hr_contacts.xlsx
Name	Email	Company Name	Personalized Line	Status	Reply
Jane HR	jane@company.com	ABC Ltd	Impressed by ABC’s AI work	✅	✅

⚙️ Configuration Tips
Adjust BATCH_SIZE in batched_email_pipeline.py for pacing.

Update your resume easily in resume/ folder.

Re-run the script daily to continue processing pending HRs.

📌 Use Cases
Job Outreach

Client Acquisition

Conference Invitations

Lead Prospecting Campaigns

👨‍💻 Author
Shashwat Patkar
🔗 LinkedIn | ✉️ shashwat.patkar@gmail.com
Feel free to fork, contribute, and suggest improvements!



🤝 Contributions Welcome!
