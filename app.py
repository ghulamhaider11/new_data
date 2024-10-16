import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport

# Sidebar file uploader for both Excel and CSV
uploaded_file = st.sidebar.file_uploader("Upload your input file", type=["xlsx", "csv"])

if uploaded_file is not None:
    st.markdown('---')
    
    # Determine the file type
    file_extension = uploaded_file.name.split('.')[-1]
    
    # Load the file based on its extension
    if file_extension == 'xlsx':
        input_df = pd.read_excel(uploaded_file, engine="openpyxl")
    elif file_extension == 'csv':
        input_df = pd.read_csv(uploaded_file)

    # Display the file content
    st.write(input_df)
    
    # Generate and display the profile report
    profile = ProfileReport(input_df, title="New Data for Profiling")
    
    st.subheader("Detailed Report of the Data Used")
    
    # Embed the profiling report as HTML in Streamlit
    st.components.v1.html(profile.to_html(), height=1000, scrolling=True)

else:
    st.write("You did not upload a file.")
