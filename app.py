import streamlit as st
import requests

# Make 웹훅 URL
MAKE_WEBHOOK_URL = "https://hook.us1.make.com/y29icqye4b1nm9mjhwlp4qdodhbixpp4"

st.title("Webhook Test")

# OpenAI API Key, Google Calendar API Key 입력 폼
openai_api_key = st.text_input("OpenAI API Key")
google_calendar_api_key = st.text_input("Google Calendar API Key")

# 테스트 데이터를 입력받기 위한 필드
event_text = st.text_input("Event Description")
event_date = st.date_input("Event Date")
event_time = st.time_input("Event Time")

if st.button("Send to Webhook"):
    # 이벤트 데이터를 Make 웹훅으로 전송
    payload = {
        "openai_api_key": openai_api_key,
        "google_calendar_api_key": google_calendar_api_key,
        "event_text": event_text,
        "event_date": event_date.strftime("%Y-%m-%d"),
        "event_time": event_time.strftime("%H:%M:%S")
    }
    response = requests.post(MAKE_WEBHOOK_URL, json=payload)
    
    if response.status_code == 200:
        st.success("Data sent successfully!")
    else:
        st.error("Failed to send data.")

if st.button("Receive from Webhook"):
    response = requests.get(MAKE_WEBHOOK_URL)
    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error("Failed to receive data.")
