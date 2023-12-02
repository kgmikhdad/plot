import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set the title of the app
st.title("Plotting Graphs with Streamlit")

# Create a sidebar with a selectbox to choose the type of plot
plot_type = st.sidebar.selectbox("Choose the type of plot", ["Matplotlib", "Seaborn", "Plotly"])

# Create a file uploader to upload a CSV file
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type="csv")

# Check if a file is uploaded
if uploaded_file is not None:
    # Read the file as a data frame
    df = pd.read_csv(uploaded_file)

    # Display the data frame
    st.write("Here is your data:")
    st.dataframe(df)

    # Display the columns of the data frame
    st.write("Here are the columns of your data:")
    st.write(list(df.columns))

    # Create a sidebar with multiselect to choose the columns to plot
    columns = st.sidebar.multiselect("Choose the columns to plot", list(df.columns))

    # Check if at least two columns are selected
    if len(columns) >= 2:
        # Display the plot based on the type of plot chosen
        st.write(f"Here is your {plot_type} plot:")
        if plot_type == "Matplotlib":
            # Create a matplotlib figure
            fig, ax = plt.subplots()
            # Plot the columns as a scatter plot
            ax.scatter(df[columns[0]], df[columns[1]])
            # Set the labels of the axes
            ax.set_xlabel(columns[0])
            ax.set_ylabel(columns[1])
            # Display the plot
            st.pyplot(fig)
        elif plot_type == "Seaborn":
            # Create a seaborn figure
            fig = sns.relplot(x=columns[0], y=columns[1], data=df)
            # Display the plot
            st.seaborn(fig)
        elif plot_type == "Plotly":
            # Create a plotly figure
            fig = px.scatter(df, x=columns[0], y=columns[1])
            # Display the plot
            st.plotly_chart(fig)

        # Create a button to download the plot as a PNG or PDF file
        download = st.button("Download plot")
        # Check if the button is clicked
        if download:
            # Save the plot as a PNG file
            fig.savefig("plot.png")
            # Display a link to download the file
            st.markdown("[Download plot]")
    else:
        # Display a message if less than two columns are selected
        st.write("Please select at least two columns to plot.")
else:
    # Display a message if no file is uploaded
    st.write("Please upload a CSV file to plot.")
