import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd  # Add this import statement for pandas
import os
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Set page title
st.title("Interactive Plotting App")

# Sidebar for user input
st.sidebar.header("Settings")

# Choose plotting library
plotting_library = st.sidebar.selectbox("Select Plotting Library", ["Matplotlib", "Seaborn", "Plotly"])

# Upload file
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

# Function to plot using Matplotlib
def plot_matplotlib(data):
    st.subheader("Matplotlib Plot")
    # Your Matplotlib plotting code here
    plt.plot(data)
    st.pyplot()

    # Save as PNG
    if st.button("Save Matplotlib Plot as PNG"):
        plt.savefig("matplotlib_plot.png")
        st.success("Plot saved as matplotlib_plot.png")

# Function to plot using Seaborn
def plot_seaborn(data):
    st.subheader("Seaborn Plot")
    # Your Seaborn plotting code here
    sns.lineplot(data=data)
    st.pyplot()

    # Save as PNG
    if st.button("Save Seaborn Plot as PNG"):
        plt.savefig("seaborn_plot.png")
        st.success("Plot saved as seaborn_plot.png")

# Function to plot using Plotly
def plot_plotly(data):
    st.subheader("Plotly Plot")
    # Your Plotly plotting code here
    fig = px.line(data, x=data.index, y=data.columns)
    st.plotly_chart(fig)

    # Save as PNG
    if st.button("Save Plotly Plot as PNG"):
        fig.write_image("plotly_plot.png")
        st.success("Plot saved as plotly_plot.png")

# Main function
def main():
    if uploaded_file is not None:
        data = None
        try:
            # Read data from CSV
            data = pd.read_csv(uploaded_file)
        except Exception as e:
            st.error(f"Error: {e}")

        if data is not None:
            if plotting_library == "Matplotlib":
                plot_matplotlib(data)
            elif plotting_library == "Seaborn":
                plot_seaborn(data)
            elif plotting_library == "Plotly":
                plot_plotly(data)
    else:
        st.warning("Please upload a CSV file.")

# Run the app
if __name__ == "__main__":
    main()
