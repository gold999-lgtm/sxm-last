#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pandas as pd
import numpy as np
import sqlite3 as sql
import matplotlib.pyplot as plt
import plotly.express as px

# Function to visualize data
def visualize(m, n):
    st.write(f"Generating data for {m} users and {n} categories...")

    # Create a DataFrame
    df = pd.DataFrame()
    df["UserId"] = list(range(1, m + 1))
    for j in range(1, n + 1):
        df["Channel" + str(j)] = np.random.randint(-1, 2, df.shape[0])

    st.write(f"Data Shape: {df.shape}")
    st.write(f"Data Types: {type(df.iloc[:, 0])}, {type(df)}")

    st.write("Data Columns with Null Values:")
    st.write(df.isnull().any(axis=0))

    st.write("Rows with Null Values:")
    st.write(df.isnull().any(axis=1))

    st.write("Saving data to CSV...")
    df.to_csv("Voting Data.csv", index=False)

    st.write("Creating SQLite database and table...")
    conn = sql.connect("voting_data.db")
    df.to_sql("ChannelVotingTable53", conn, index=False)

    st.write("Reading data from SQLite database...")
    conn = sql.connect("voting_data.db")
    df = pd.read_sql_query("SELECT * from ChannelVotingTable53", conn)

    st.write("Visualizing data...")
    total_votes = []
    channels = []
    for j in range(1, n + 1):
        tvc = df['Channel' + str(j)].value_counts()[1]
        total_votes.append(tvc)
        channels.append(j)

    st.write("Line Plot")
    st.line_chart(pd.DataFrame({'Channels': channels, 'Total Votes': total_votes}).set_index('Channels'))

    #st.write("Scatter Plot")
    #st.scatter_chart(pd.DataFrame({'Channels': channels, 'Total Votes': total_votes}))

    st.write("Pie Chart")
    fig = px.pie(names=channels, values=total_votes, title="Total Votes for Each Channel")
    st.plotly_chart(fig)

    st.write("Bar Chart")
    fig = px.bar(x=channels, y=total_votes, title="Total Votes for Each Channel")
    st.plotly_chart(fig)

def main():
    st.title("Streamlit Voting Data Visualization")
    m = st.number_input("Enter the Number of Users", value=50)
    n = st.number_input("Enter the number of categories", value=5)
    visualize(m, n)

if __name__ == '__main__':
    main()


# In[ ]:




