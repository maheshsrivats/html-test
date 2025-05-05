# test_flask.py
print("helllooooooooooooo")
import streamlit as st
from datetime import date
import pandas as pd
from PIL import Image
from ydata_profiling import ProfileReport
from pydantic_settings import BaseSettings

import seaborn as sns
import matplotlib.pyplot as plt

import os
import pandas
from pandasai import Agent

from pandasai.llm import OpenAI

from langchain_openai import AzureChatOpenAI
from pandasai import SmartDataframe

os.environ["AZURE_OPENAI_API_KEY"] = "8045853e65304ea98db831bb95d830f6"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://sci-gpt.openai.azure.com/"

llm = AzureChatOpenAI(openai_api_version="2023-09-15-preview", deployment_name="SCI_GPT")

# st.set_option('deprecation.showPyplotGlobalUse', False)
# Define functions for each page
def data_view(data):
    st.dataframe(data.reset_index(drop=True))

    # profile = ProfileReport(filtered_data, title='Data Analysis Report', explorative=True)
    # st.write(profile.to_widgets())
    # st.components.v1.html(profile.to_html(), height=4000)

def insights_gpt_view(df):
    smart_df = SmartDataframe(
        df,
        config={
            "llm": llm,
            "verbose": True,
            "open_charts": False,
        }
    )
    user_query = st.text_input('QnA on the Data', 'Type here...')
    if st.button("Send Query"):
        response = smart_df.chat(user_query)
        try:
            img = Image.open(response)
            st.image(img, use_column_width=True)
        except Exception as e:
            st.write(response)

@st.cache_data  # Use caching to avoid loading the data multiple times
def load_data():
    ikea_products = [
        {
            'SKU': '72041247',
            'SKU Name': 'Charming Bowl (Umbrellas)',
            'Category': 'Outdoor',
            'Sub-Category': 'Umbrellas',
            'Vendor': 'Vendor 75',
            'Unit Price': '493.66',
            'Lead Time (Weeks)': '14',
            'MOQ': '205',
            'Payment Terms': 'Prepaid',
            'Price Basis': 'Ex-Showroom',
            'Delivery Terms': 'Ex-Showroom Hyderabad',
            'Quality Inspection Terms': 'During production inspection',
            'Supplier Code of Conduct Compliance': 'In Progress',
            'Environmental Impact': 'No',
            'Social Responsibility': 'No',
            'Sustainability Certifications': 'PEFC',
            'Packaging Requirements': 'Standard',
            'Product Specifications': 'See product details',
            'Warranty Terms': 'Limited Lifetime',
            'Return Policy': '90 days',
            'Compliance with IKEA Standards': 'In Progress',
            'Inspection and Testing Requirements': 'Yes',
            'Supplier Performance Metrics': 'Quality'
        },
        {
            'SKU': '76766049',
            'SKU Name': 'Simple Fork (Boxes)',
            'Category': 'Organization',
            'Sub-Category': 'Boxes',
            'Vendor': 'Vendor 46',
            'Unit Price': '33.26',
            'Lead Time (Weeks)': '20',
            'MOQ': '139',
            'Payment Terms': 'Net 30',
            'Price Basis': 'FOB Origin',
            'Delivery Terms': 'FOB Origin Delhi',
            'Quality Inspection Terms': 'Third-party inspection',
            'Supplier Code of Conduct Compliance': 'In Progress',
            'Environmental Impact': 'No',
            'Social Responsibility': 'In Progress',
            'Sustainability Certifications': 'None',
            'Packaging Requirements': 'Sustainable',
            'Product Specifications': 'See product details',
            'Warranty Terms': '1 year',
            'Return Policy': '30 days',
            'Compliance with IKEA Standards': 'No',
            'Inspection and Testing Requirements': 'In Progress',
            'Supplier Performance Metrics': 'Cost'
        },
        # Add more entries as needed
    ]
    
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(ikea_products)
    return df

def main():
    st.set_page_config(page_title="Gen AI asset", page_icon="👀")
    df = load_data()
    st.title("Analysis")
    # st.image('logo.png', width=30)

    page = st.sidebar.selectbox("Choose a view", ["Data", "Insights"])

    # st.sidebar.subheader("Data Range")
    # Use date_input to take 'from' and 'to' dates

    if page == "Data":
        data_view(df)
    elif page == "Insights":
        insights_gpt_view(df)

if __name__ == "__main__":
    main()
