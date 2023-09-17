

import streamlit as st
import pandas as pd
import numpy as np
import sqlite3 as sql
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import sqlite3 as sql
import matplotlib.pyplot as plt
import plotly.express as px

# Function to visualize data
def visualize():
  
    conn = sql.connect("voting_data.db")
    df = pd.read_sql_query("SELECT * from ChannelVotingTable62", conn)

    st.write("Visualizing data...")
    total_votes = []
    channels = []
    n=len(df.columns)
    for j in range(1, n ):
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
    st.title("Voting Data Visualization")
  
    visualize()

if __name__ == '__main__':
    main()