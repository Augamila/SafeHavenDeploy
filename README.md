# SafeHaven Dashboard (Python Streamlit)

A lightweight Streamlit admin dashboard for monitoring campaign data for the SafeHaven crowdfunding platform.

## 🔧 Setup

1. Clone this repo or unzip the archive
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Add your Firebase service credentials using Streamlit Secrets:
   - Go to Streamlit Cloud → Settings → Secrets and paste:
     ```toml
     [firebase]
     type = "service_account"
     ...
     ```
4. Run the app:
   ```
   streamlit run safehaven_dashboard.py
   ```

## 🔐 Firebase Required Collections

Ensure you have a Firestore collection at:
```
/artifacts/safehaven-app/public/data/campaigns
```

## ✅ Features

- Live campaign progress visualization
- Firebase Firestore integration
- Streamlit Secrets security
