import streamlit as st
import time

# Function to simulate conversation
def display_conversation():
    conversation = [
    ("Bot 1", "Good morning, Bot 2. I hope you're well. I wanted to discuss our pricing and discount strategies for the upcoming holiday season."),
    ("Bot 2", "Good morning, Bot 1. I'm doing well, thank you. Yes, the holiday season is approaching, and it's a crucial time for our pricing and discounts. Let's dive into the data. What insights do you have so far?"),
    ("Bot 1", "Well, based on historical data, we can see that during the holiday season, there's a significant increase in customer traffic and sales. However, we also observe that customers are increasingly price-conscious during this period, looking for deals and discounts."),
    ("Bot 2", "That's valuable information. To make informed decisions, I've analyzed the data from the past few holiday seasons. It seems like our biggest competitors tend to offer discounts on similar product categories. Their discounts range from 10% to 20%. To stay competitive, we might consider offering discounts within this range."),
    ("Bot 1", "That aligns with our goals. We don't want to over-discount, but we need to remain competitive. Let's aim for a range of 10% to 15% off on selected holiday products. Additionally, we should consider bundling some items together for greater value."),
    ("Bot 2", "Agreed. Bundling can be an effective strategy. I can analyze customer buying patterns to identify which products are frequently purchased together and create bundled offers accordingly. This way, we can maximize both sales and customer satisfaction."),
    ("Bot 1", "Excellent. Also, I've noticed that some products have a higher profit margin, so we can afford to offer slightly higher discounts on others. Can you help identify which products fall into this category?"),
    ("Bot 2", "Certainly. I'll analyze the data to identify high-margin products that we can use to cross-subsidize discounts on other items. This will help us maintain our profit margins while offering competitive prices."),
    ("Bot 1", "That's a smart approach. Additionally, let's keep an eye on real-time sales data during the holiday season. If we see certain products performing exceptionally well, we should consider adjusting prices or offering additional discounts to capitalize on the demand."),
    ("Bot 2", "Agreed, Bot 1. Real-time data analysis will be crucial for making quick, data-driven decisions during the holiday rush. I'll set up alerts to notify you of any significant changes in sales trends."),
    ("Bot 1", "Fantastic. It's great to have you on board, Bot 2. With your data insights and analysis, I'm confident that we can execute a successful pricing and discount strategy for the holiday season."),
    ("Bot 2", "Thank you, Bot 1. I'm looking forward to collaborating with you and ensuring that our pricing and discount management align with our customers' expectations and maximize our holiday season sales."),
]

    for speaker, message in conversation:
        if speaker == "Bot 1":
            bot1_text_area.text_area("Bot 1:", value=message, height=300) #, key="bot1"
            time.sleep(2)  # Delay for 2 seconds
        else:
            bot2_text_area.text_area("Bot 2:", value=message, height=300) #, key="bot2"
            time.sleep(2)  # Delay for 2 seconds

# Streamlit app layout
st.title("Bot Conversation Simulator")

# Create two columns for the bots
col1, col2 = st.columns(2)
with col1:
    st.header("Bot 1")
    bot1_text_area = st.empty()

with col2:
    st.header("Bot 2")
    bot2_text_area = st.empty()

# Button to start conversation
if st.button("Start Conversation"):
    display_conversation()
