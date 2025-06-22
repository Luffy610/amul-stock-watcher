# 🧀 AMUL Stock Watcher (with Email Alerts)

This Python project monitors the availability of selected AMUL products on the AMUL website and notifies you **via email** when a product is back in stock.

Perfect for when you're trying to buy a high-demand item like protein milk, buttermilk and whey protein and it's often marked **"Sold Out"**.

## ✨ Features

- ✅ Headless stock checker using Selenium
- ✅ Fully automated via GitHub Actions (runs every 4 hours)
- 📩 Sends **email notifications** when a product becomes available
- 🔁 Retries up to 3 times if the website fails to load properly
- 🔐 Uses GitHub Secrets for safe storage of credentials
- 📱 Supports **multiple email recipients**

## 📦 Project Structure
```markdown
amul-stock-watcher/
├── app/
│   ├── send_email.py        # Email notification logic
│   ├── stock_checker.py     # Stock checking logic
│   └── main.py              # Main checker script
├── requirements.txt         # Python dependencies
└── .github/
    └── workflows/
        └── stock-check.yml  # GitHub Actions workflow
```

## 🚀 How It Works

1. Selenium opens the AMUL product page.
2. Enters your pincode via the popup modal.
3. Waits for page update and checks for "Sold Out" alert.
4. If **not sold out**, it sends an email alert with the product URL.
5. GitHub Actions runs this script **every 4 hours**.

---

## 🧑‍💻 Local Setup

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/amul-stock-watcher.git
cd amul-stock-watcher
```
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
3. Add a .env file (for local testing)
Create a file named `.env` with the following content:
```bash
GMAIL_USER=yourgmail@gmail.com
GMAIL_PASS=your_16_char_app_password
EMAIL_TO=you@example.com,another@example.com
```
### 4. Run the Script

```bash
python app/main.py
```

You'll see the logs and recieve an email if the product is in stock.

## ☁️ GitHub Actions Setup (Automatic Checks Every 4 Hours)

### 1. Add Repository Secrets
Go to your **repo > Settings > Secrets and variables > Actions**, and add these:

| Secret Name  | Description                              |
|--------------|------------------------------------------|
| `GMAIL_USER` | Your Gmail address                       |
| `GMAIL_PASS` | Your Gmail app password (16 characters)  |
| `EMAIL_TO`   | Comma-separated list of recipient emails |


### 2. Push the Code
Ensure your repo contains:
```markdown
- app/
  - send_email.py
  - stock_checker.py
  - main.py
- requirements.txt
- .github/
  - workflows/
    - stock-check.yml
- .env (optional for local testing)
```

```bash
git add .
git commit -m "Setup AMUL Stock Watcher"
git push origin main
```

### 3. Run it manually (optional)
You can manually trigger the workflow from the GitHub Actions tab in your repo.

## ⏰ Scheduled Cron Timing
The script runs every 4 hours using the following cron expression:
```yaml
on:
  schedule:
    - cron: '0 */4 * * *'
```
This means it will check the stock at 00:00, 04:00, 08:00, 12:00, 16:00, and 20:00 UTC.

## 📧 Multiple Email Recipients
You can specify multiple email addresses in the `EMAIL_TO` variable, separated by commas. The script will send notifications to all listed recipients.

## 💻 Tech Stack
- Python 3.13
- Selenium for web automation
- Gmail for email notifications
- GitHub Actions for automation
- Tested headlessly on Ubuntu 22.04 via GitHub Actions

## ⚠️ Notes
- Make sure to use a **Gmail app password** for the `GMAIL_PASS` variable. Regular Gmail passwords won't work due to security restrictions. [Generate one here](https://myaccount.google.com/apppasswords).
- If you're using a different email provider, update the SMTP server accordingly
- This project scrapes AMUL’s publicly available product stock status; use respectfully

## 🙌 Contributing
Pull requests are welcome! Open an issue if you want to monitor multiple URLs, switch to Pushbullet/Telegram, or add logging features.