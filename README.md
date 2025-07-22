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


## 🔑 About the `credentials` Folder & Google OAuth Setup

### Why Use Your Own Google OAuth API?

For secure, authorized access to your Gmail account, you **must create your own OAuth credentials via Google Cloud**. Never share your credentials files online, and always use your own for privacy.

### How to Obtain and Configure `credentials.json`

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).  
2. Create/Open a Project.  
3. Enable the Gmail API (APIs & Services > Enable APIs and Services > search "Gmail API" > Enable).  
4. Configure OAuth consent screen (choose External user type and complete minimal setup).  
5. Create OAuth Client ID (Credentials > Create > OAuth client ID > Desktop app).  
6. Download the `credentials.json` and place it in the `credentials/` folder in your project.  
7. On first script run, authenticate with Google in the browser; this will create `token.json` in `credentials/`.

*(continue with the rest of your README content similarly, with clear headings, bullet lists, code blocks, and blank lines)*

### Additional Tips

- Preview your README in GitHub or a Markdown viewer to check formatting before committing.  
- Use a Markdown editor (Typora, VS Code with Markdown Preview) for easier writing.  
- If pasting from somewhere that loses formatting, manually fix indentation and blank lines before saving.

If you want, I can also prepare a **Markdown (.md) file** formatted exactly for GitHub so you can copy-paste it directly without losing structure. Just let me know!
