import pandas as pd
import plotly
import plotly.express as px
import streamlit as st
import seaborn as sns
from PIL import  Image

# Image

im = Image.open(fp="C:\\Users\\admin\\Downloads\\Techno.jpeg")

st.set_page_config(page_title='OneKlick Techno',layout='wide',page_icon=im)

@st.cache_data
def data_excel():
    file_name = r"D:\Machine Learning\techno data\Calling.xlsx"
    dataframe = pd.read_excel(io=file_name,engine="openpyxl",
                              sheet_name="Calling data",nrows=674)
    return dataframe


dataframe = data_excel()

# Name Selection
st.sidebar.header("Please Filter Here")
Name = st.sidebar.multiselect(
    "Select the Person Name",
    options=dataframe['Name'].unique(),
    default=dataframe['Name'].unique()

)

dataframe = dataframe.query(
    "Name == @Name"
)
#header
st.subheader(":iphone: Jio Calling Data",)
st.markdown("###")

# KPI
highest_time = dataframe['Time In Min.'].max()
avg_time = dataframe['Time In Min.'].sum()/dataframe['Time In Min.'].count()
left_column, middle_column,right_column = st.columns(3)
with left_column:
    st.subheader("Highest Call Time")
    st.subheader(f"{highest_time}")
with middle_column:
    st.subheader("Average Time")
    st.subheader(f"{round(avg_time,2)}")
with right_column:
    st.subheader("Total Time In Min.")
    st.subheader(round(dataframe['Time In Min.'],0).sum())
st.markdown("---")
st.caption("Note: The dataset is regarding of only office time!")


# Plots
x = dataframe['Time In Min.']
y = dataframe['Calling Time hour']
fig = px.scatter(dataframe,x =y, y =x,color=dataframe["Name"],width=600,color_continuous_scale="reds")
fig.update_xaxes()
fig.update_layout(title ={
    'text' : "Hour Viz Calls",
    'y' : 0.9,
    'x' : 0.5,
    "xanchor" : "center",
    "yanchor" : 'top'},
font = dict(
    family = "Arial",
    color = "black",
    size = 9
))
st.plotly_chart(fig, theme="streamlit", use_container_width=True)


#Calling vix date

import seaborn as sns
ax = plt.figure(figsize=(18,5))
sns.set_style("white")
sns.lineplot(data= dataframe,x = "Date",y="Time In Min.",hue=dataframe.Name,ci=20).set_title("Calling Time by Date",fontsize=13)
plt.xticks(dataframe['Date'].unique(),rotation=70,fontsize=10)
sns.despine(right=True,top=True)
plt.xlabel(xlabel=" ")
st.pyplot(ax)


#Hist
first_column,second_column = st.columns(2)
with first_column:
    fig = plt.figure(figsize=(8,5))
    sns.histplot(dataframe["Time In Min."],kde=True,alpha=0.2,shrink=1.5).set_title('Time Duration Count',fontsize=12)
    plt.xticks(fontsize=10)
    sns.despine(right=True,top=True)
    st.pyplot(fig)
with second_column:
    ax =px.pie(dataframe,values="Time In Min.",names="Name",width=450,height=330,title="Value Count By Person")
    st.plotly_chart(ax)
    ax.update_layout(
        title={
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})


# dataframe

st.markdown("DataFrame")
dataframe['Date'] = dataframe['Date'].dt.date
st.dataframe(dataframe,use_container_width=False)


# Hide the lables
hide_streamlit_style= """
<style>
#Mainmenu {visibility:hidden;}
</style>
"""
st.markdown(hide_streamlit_style,unsafe_allow_html=True)
