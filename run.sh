#!/bin/bash
# Smart Risk Profiler — Run Script
cd "$(dirname "$0")"
source venv/bin/activate
streamlit run app.py
