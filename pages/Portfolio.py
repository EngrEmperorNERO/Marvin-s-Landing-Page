import streamlit as st
import base64


st.set_page_config(
    page_title="Portfolio",
    page_icon="💼",
    layout="wide"
)
# Function to get the background image as a base64 string
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    return b64_string

# Get the path to the image
image_path = "images/background3.jpg"

# Get the base64 string of the image
base64_image = get_base64_image(image_path)

st.markdown(f"""
    <style>
    /* Main page background image and text styling */
    .main {{
        background-image: url("data:image/jpg;base64,{base64_image}");
        background-size: cover;
        background-position: center;
        color: #00000; /* Set text color to white */
    }}

    /* Set text color for all Streamlit elements */
    .stText, .stTitle, .stHeader, .stMarkdown, .stCaption, .stSubheader, .stRadio, .stCheckbox, .stSelectbox, .stTextInput, .stButton, .stWidget {{
        color: #00000; /* Set text color to white */
    }}

    /* Hide Streamlit header and footer */
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    </style>
    """, unsafe_allow_html=True)



st.markdown("<h1 style='color: black;'>Portfolios</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

st.markdown("<h1 style='color: black;'>Real Estate NZ Property Listings Dashboard</h1>", unsafe_allow_html=True)
st.markdown("*Graphical Illustration of Property Listings*")  # Italicized text
col1, col2 = st.columns([2, 1], gap="large")  # Adjust column width ratio

with col1:
    st.markdown("""
    - The data comes from scraping automatically using a python script, gathering details of every property listings.
    - Graphical Data of Average Days on Market by Region
    - Line Graph of Listing Volume per Year
    - Dropdown option for filtering property listings Date Range
    - Data Source comes from https://www.realestate.co.nz/residential/sale
    - A python script will scrape the posting on the website and then will load on the dashboard.
    """)
    st.write("***Link: https://realestatenzdash-fgutiz3x7zjxkxkxefjcte.streamlit.app/***")

with col2:
    # Specify the path to the image in the images folder
    st.image("images/image1.png", width=400)

st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

st.markdown("<h1 style='color: black;'>TradeME NZ Property Listings Dashboard</h1>", unsafe_allow_html=True)
col1, col2 = st.columns([2, 1], gap="large")  # Adjust column width ratio


with col1:
    st.markdown("""
    - The script creates a Streamlit dashboard that allows users to filter property data by region, suburb, number of bedrooms, number of bathrooms, and listing date range. The filters are implemented as multi-select dropdowns and a date range selector in the sidebar.
    - The dashboard visualizes key metrics using Plotly, including bar charts for average rent and average days on market by region, and a line chart for property listing volume over time. The charts are styled with customized colors, fonts, and layouts.
    - The app includes custom CSS for consistent styling, such as setting background colors, adjusting sidebar colors, and customizing the appearance of chart elements. The main background is light gray, with sidebar and chart colors aligned to the user’s theme preferences.
    - Key statistics, such as the number of properties scraped and the average rent, are prominently displayed using styled information cards. The cards are color-coordinated to match the theme, with white text on colored backgrounds.
    - The Source of data is from scraped from https://www.trademe.co.nz/a/ After scraping, Additional python script will clean the data and then will be loaded on the dashboard.
                """)
    st.write("***Link: https://trademenzdash-e8tptjqt8dfpxu9vfpzob4.streamlit.app/***")

with col2:
    # Specify the path to the image in the images folder
    st.image("images/trademedash.png", width=400)

st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

st.markdown("<h1 style='color: black;'>Customer Lifetime Value Dashboard</h1>", unsafe_allow_html=True)
col1, col2 = st.columns([2, 1], gap="large")  # Adjust column width ratio

with col1:
    st.markdown("""
    - This four Dashboard  offers insights into customer value by tracking how long they remain customers, their total refunds, how many times they orders, and their total orders. It also highlights the average order value and frequency, and how these metrics relate to the company's marketing campaigns.
    - This dashboard also provides insights on identifying patterns and trends in customer retention, helping to improve strategies that increase customer loyalty and reduce churn rates.
    - With insights from the CLTV Dashboard, businesses can allocate marketing budgets more efficiently by focusing on acquiring and retaining high-value customers, leading to better ROI.
    - This dashboard was created using Power BI. The source of data comes from Mysql and most of the transformation happens upstream which is Mysql.
                """)

with col2:
    # Specify the path to the image in the images folder
    st.image("images/clv.png", width=400)

st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

st.markdown("<h1 style='color: black;'>E-Commerce Dashboard.</h1>", unsafe_allow_html=True)
st.markdown("*This e-commerce dashboard provides valuable insights into the store's performance.*")
col1, col2 = st.columns([2, 1], gap="large")  # Adjust column width ratio

with col1:
    st.markdown("""
    - Profit Tracking: It monitors profit over time, offering detailed breakdowns by year and quarter to help identify seasonal trends and growth patterns.
    - Geographical Analysis: The State slicer enables in-depth analysis by region, supporting informed decisions based on state-level performance.
    - Category Insights: Profit by sub-category reveals which product categories are most profitable, guiding inventory management and marketing strategies.
    - Customizable Views: The dashboard's filters and slicers allow users to tailor the data display, making it easy to find the information they need.
    - Holistic Performance View: By combining profit analysis, regional data, and product category performance, the dashboard provides a comprehensive overview of the e-commerce business.
    """)

with col2:
    # Specify the path to the image in the images folder
    st.image("images/image3.png", width=400)

st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

st.markdown("<h1 style='color: black;'>Automated Item Update.</h1>", unsafe_allow_html=True)
st.markdown("*The Automated Item Update script uses python to automate the process of item checking on the current inventory..*")
col1, col2 = st.columns([2, 1], gap="large")  # Adjust column width ratio

with col1:
    st.markdown("""
    - It uses 2 files; 1 from the manufacturer and one from the database of the company itself.
    - It clean the files and remove unwanted data.
    - The main algorithm is to loop through file and check if the item on the manufacturers is on the current inventory file. If not, then it will save it.
    - Finally, It will map the Product Category based on the dictionary data type in the code.
    """)
    st.write("***Link: https://github.com/EngrEmperorNERO/PHxxxx-Automated-Item-Update***")

with col2:
    # Specify the path to the image in the images folder
    st.image("images/automated-item-update.png", width=500)

st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

st.markdown("<h1 style='color: black;'>Data Transformation SQL Script: Orders LTV Schema.</h1>", unsafe_allow_html=True)
#st.markdown("*The Automated Item Update script uses python to automate the process of item checking on the current inventory..*")
col1, col2 = st.columns([2, 1], gap="large")  # Adjust column width ratio

with col1:
    st.markdown("""
    - This SQL script combines the necessary data such as order and order_items for the orders_ltv table. The process starts with cleaning the data, getting the column from each table(Orders and order_items) and joining it together.
    - The goal of the script is to have a summarized version of the orders table wherein we can see their 1st ever orders, which campaign they got 1st and the date of their original purchase.
    """)
    st.write("***Link: https://github.com/EngrEmperorNERO/Orders-LTV-Sample-schema-using-MySQL***")

with col2:
    # Specify the path to the image in the images folder
    st.image("images/orders-ltv.png", width=500)

st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

st.markdown("<h1 style='color: black;'>Automated Email Sender using Python.</h1>", unsafe_allow_html=True)
#st.markdown("*The Automated Item Update script uses python to automate the process of item checking on the current inventory..*")
col1, col2 = st.columns([2, 1], gap="large")  # Adjust column width ratio

with col1:
    st.markdown("""
    - The use of this python script is to automate sending the report. It connects with the user personal google account and give us a functionality to add an attachment that can be sent together with a hard coded message. It allows us to free our time sending recurring email everyday.
    """)
    st.write("***Link: https://github.com/EngrEmperorNERO/Sending-Report-with-Attachment-Python***")

with col2:
    # Specify the path to the image in the images folder
    st.image("images/send-email.png", width=500)

st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

st.markdown("<h1 style='color: black;'>UPS Cost Analysis Dashboard</h1>", unsafe_allow_html=True)
st.markdown("*The script provides an interactive dashboard for analyzing and visualizing UPS cost data.*")

col1, col2 = st.columns([2, 1], gap="large")  # Adjust column width ratio

with col1:
    st.markdown("""
    - The script allows users to filter and view UPS cost analysis data based on various criteria (service type, identifier, zone, DIM) using Streamlit’s interactive widgets. The filtered data is displayed in a table for detailed inspection.
    - It generates bar charts to visualize the count of different service types and DIM OUT shipments. This helps in understanding the distribution of service types and dimensional attributes across the dataset.
    - The script creates a sunburst chart and donut charts to provide a detailed breakdown of charges by service type. It also includes charts for visualizing the distribution of base rates and overall charge breakdowns.
    - The script generates individual heatmaps for specific charges (e.g., AHS Weight, DAS Comm) against the client’s cost, allowing users to examine the correlation between individual charge categories and overall cost.
    """)
    st.write("***Link: https://ups-dashboard-bf-cijesfjz8vsdznrg9uzldn.streamlit.app/***")

with col2:
    # Specify the path to the image in the images folder
    st.image("images/ups-dashboard.png", width=400)

st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

st.markdown("<h1 style='color: black;'>Cost Analysis Tools</h1>", unsafe_allow_html=True)
st.markdown("*A Multi Page App for Analyzing shipments cost and apply Discounts effectively.*")

col1, col2 = st.columns([2, 1], gap="large")  # Adjust column width ratio

with col1:
    st.markdown("""
    - Presents a list of tools with interactive buttons that allow users to navigate to different sections of the app, such as 'Airbill to Data Tab,' 'Analysis Tool,' and 'Discount Tool.
    - Airbill to Data Tab: Uploads your Shipment Invoices and process it into proper table like format.
    - Analysis Tool: The analysis tool to applies various cost analysis pivots and summary.
    - Discount Tool: Discount Tool helps you apply discounts on various shipments.
    """)
    st.write("***Link: https://costanalysismultipageapp.streamlit.app/***")

with col2:
    # Specify the path to the image in the images folder
    st.image("images/multipage.png", width=400)

st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

st.markdown("<h1 style='color: black;'>Consignment Fee Dashboard</h1>", unsafe_allow_html=True)
col1, col2 = st.columns([2, 1], gap="large")  # Adjust column width ratio

with col1:
    st.markdown("""
    - This dashboard was created using Tableau.
    - The source of data comes from Salesforce directly.
    - Transformation is happening on premise meaning on the Tableau itself.
    - This Dashboard shows insights about the Consignment fee trend. The company set a 2% rule meaning the over all consignment fee must not be greater than 2% of the overall Bill Only Sales of the company.
    - Other component of the dashboard shows the Year to date consignment fee of every warehouses as well as ratio of Bill Only Sales for every warehouses.
    - The Dashboard further breaks down the Consignment fee by 2 main types of Product; Sterile and Non Sterile.
    """)

with col2:
    # Specify the path to the image in the images folder
    st.image("images/consignment-dashboard.png", width=400)

st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

st.markdown("<h1 style='color: black;'>Freight Logistics Dashboard</h1>", unsafe_allow_html=True)
col1, col2 = st.columns([2, 1], gap="large")  # Adjust column width ratio

with col1:
    st.markdown("""
    - This dashboard was created using Tableau.
    - The source of data comes from Salesforce directly.
    - Transformation is happening on premise meaning on the Tableau itself.
    - This dashboard shows the Monthly Spend on Shipment as well as the breakdown of Total Shipment expenses for every warehouses. Additionally, The graph also shows the breakdown of Shipment for every category for the current Month as well as the trend of Shipment expenses for every category.
    """)

with col2:
    # Specify the path to the image in the images folder
    st.image("images/freight-logistics.png", width=400)

st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)
