import streamlit as st
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

import seaborn as sns
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI NIDS Dashboard", layout="wide")

st.title("AI-Powered Network Intrusion Detection System")

st.markdown("""
### Project Overview
This system uses Machine Learning (**Random Forest Algorithm**) to analyze network traffic.
It classifies traffic into:
- **Benign** (Normal traffic)
- **Malicious** (DDoS attacks)
""")

# ---------------- 1. DATA LOADING (REAL DATA) ----------------
@st.cache_data
def load_data():
    # Load CIC-IDS2017 CSV
    df = pd.read_csv("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert labels to numeric
    df['Label'] = df['Label'].map({'BENIGN': 0, 'DDoS': 1})

    # Drop invalid rows
    df = df.dropna(subset=['Label'])

    # Select required features
    df = df[
        [
            'Destination Port',
            'Flow Duration',
            'Total Fwd Packets',
            'Packet Length Mean',
            'Active Mean',
            'Label'
        ]
    ]

    return df

df = load_data()

# ---------------- SIDEBAR CONTROLS ----------------
st.sidebar.header("Control Panel")
st.sidebar.info("Adjust model parameters")

split_size = st.sidebar.slider("Training Data Size (%)", 50, 90, 80)
n_estimators = st.sidebar.slider("Number of Trees", 10, 200, 100)

# ---------------- 2. PREPROCESSING ----------------
X = df.drop('Label', axis=1)
y = df['Label']

test_size = (100 - split_size) / 100

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=test_size,
    random_state=42
)

# ---------------- 3. MODEL TRAINING ----------------
st.divider()
col_train, col_metrics = st.columns([1, 2])

with col_train:
    st.subheader("1. Model Training")

    if st.button("Train Model Now"):
        with st.spinner("Training Random Forest..."):
            model = RandomForestClassifier(
                n_estimators=n_estimators,
                random_state=42
            )
            model.fit(X_train, y_train)
            st.session_state['model'] = model
            st.success("Model trained successfully!")

    if 'model' in st.session_state:
        st.success("Model ready for testing")

# ---------------- 4. EVALUATION ----------------
with col_metrics:
    st.subheader("2. Performance Metrics")

    if 'model' in st.session_state:
        model = st.session_state['model']
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)

        c1, c2, c3 = st.columns(3)
        c1.metric("Accuracy", f"{acc * 100:.2f}%")
        c2.metric("Total Records", len(df))
        c3.metric("Detected Attacks", int(np.sum(y_pred)))

        st.write("### Confusion Matrix")
        cm = confusion_matrix(y_test, y_pred)

        fig, ax = plt.subplots(figsize=(4, 3))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', ax=ax)
        ax.set_xlabel("Predicted")
        ax.set_ylabel("Actual")
        st.pyplot(fig)
    else:
        st.warning("Train the model first")

# ---------------- 5. LIVE ATTACK SIMULATOR ----------------
st.divider()
st.subheader("3. Live Traffic Simulator")

c1, c2, c3, c4, c5 = st.columns(5)

p_port = c1.number_input("Destination Port", 1, 65535, 80)
p_dur = c2.number_input("Flow Duration", 0, 100000, 200)
p_pkts = c3.number_input("Total Fwd Packets", 0, 5000, 100)
p_len = c4.number_input("Packet Length Mean", 0, 1500, 500)
p_active = c5.number_input("Active Mean", 0, 1000, 50)

if st.button("Analyze Packet"):
    if 'model' in st.session_state:
        model = st.session_state['model']

        input_data = np.array([
            [p_port, p_dur, p_pkts, p_len, p_active]
        ])

        # ML probability
        proba = model.predict_proba(input_data)[0][1]

        st.write(f"**Attack Probability:** {proba*100:.2f}%")

        # ---------------- DECISION LOGIC ----------------
        if p_pkts > 600 and p_dur < 300:
            st.error("🚨 MALICIOUS TRAFFIC DETECTED (Rule-Based DDoS Signature)")

        elif proba >= 0.30:
            st.warning("⚠️ SUSPICIOUS TRAFFIC (Possible DDoS)")

        else:
            st.success("✅ BENIGN TRAFFIC")

    else:
        st.error("Please train the model first")
