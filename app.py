
import sqlite3
import pandas as pd
import streamlit as st


conn = sqlite3.connect('test_data.db')
cursor = conn.cursor()


df = pd.read_sql_query("SELECT * FROM test_results", conn)

st.title("🔍 Mini Test Result Dashboard")


st.subheader("📊 Test Summary")
col1, col2, col3 = st.columns(3)
col1.metric("✅ Passed", df[df['status'] == 'PASS'].shape[0])
col2.metric("❌ Failed", df[df['status'] == 'FAIL'].shape[0])
col3.metric("⏱️ Avg Duration", f"{df['duration'].mean():.2f} sec")


st.sidebar.header("Filter Results")
status_filter = st.sidebar.selectbox("Status", options=["All", "PASS", "FAIL"])
module_filter = st.sidebar.selectbox("Module", options=["All"] + sorted(df['module'].unique().tolist()))

filtered_df = df.copy()
if status_filter != "All":
    filtered_df = filtered_df[filtered_df["status"] == status_filter]
if module_filter != "All":
    filtered_df = filtered_df[filtered_df["module"] == module_filter]


st.subheader("📋 Test Results")
st.dataframe(filtered_df)


st.download_button("⬇️ Download as CSV", filtered_df.to_csv(index=False), "test_results.csv")

conn.close()
