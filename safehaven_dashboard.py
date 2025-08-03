import streamlit as st
import json
import firebase_admin
from firebase_admin import credentials, firestore

# Securely load Firebase credentials from Streamlit secrets
firebase_creds = json.loads(st.secrets["firebase"])
cred = credentials.Certificate(firebase_creds)
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

def get_campaigns():
    docs = db.collection('artifacts/safehaven-app/public/data/campaigns').stream()
    return [doc.to_dict() for doc in docs]

st.set_page_config(page_title="SafeHaven Admin Dashboard", layout="wide")
st.title("📊 SafeHaven Campaign Analytics")

campaigns = get_campaigns()
if not campaigns:
    st.warning("No campaigns found.")
else:
    for c in campaigns:
        st.subheader(c.get('title', 'Untitled Campaign'))
        st.markdown(f"**Goal:** ${c.get('goalAmount', 0)} | **Raised:** ${c.get('currentAmount', 0)}")
        progress = c.get('currentAmount', 0) / max(c.get('goalAmount', 1), 1)
        st.progress(min(progress, 1.0))
