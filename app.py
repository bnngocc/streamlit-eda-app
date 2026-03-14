import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple EDA App")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file, encoding="latin1")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

    if len(numeric_columns) >= 2:
        x_col = st.selectbox("Choose X column", numeric_columns)
        y_col = st.selectbox("Choose Y column", numeric_columns)

        st.subheader("Scatter Plot")
        fig, ax = plt.subplots()
        ax.scatter(df[x_col], df[y_col])
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        st.pyplot(fig)

        st.subheader("Correlation Output")
        corr = df[x_col].corr(df[y_col])
        st.write(f"Correlation between {x_col} and {y_col}: {corr:.2f}")
    else:
        st.write("Dataset must have at least two numeric columns.")