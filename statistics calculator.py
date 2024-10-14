import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, tan, sqrt, log, exp

# Title of the app
st.title('Comprehensive Calculator for Arithmetic, Scientific, and Statistical Calculations')

# Basic Arithmetic Operations
def calculator():
    st.subheader("Basic Arithmetic Operations")

    num1 = st.number_input("Enter first number", step=1e-6, format="%.6f")
    num2 = st.number_input("Enter second number", step=1e-6, format="%.6f")
    operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
            st.write(f"Result: {num1} + {num2} = {result}")
        elif operation == "Subtract":
            result = num1 - num2
            st.write(f"Result: {num1} - {num2} = {result}")
        elif operation == "Multiply":
            result = num1 * num2
            st.write(f"Result: {num1} * {num2} = {result}")
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
                st.write(f"Result: {num1} / {num2} = {result}")
            else:
                st.error("Error! Division by zero.")

# Scientific Functions
def scientific_functions():
    st.subheader("Scientific Functions")

    num = st.number_input("Enter a number", step=1e-6, format="%.6f")
    func = st.selectbox("Choose a function", ("Sine", "Cosine", "Tangent", "Square Root", "Logarithm", "Exponential"))

    if st.button("Calculate Scientific Function"):
        try:
            if func == "Sine":
                result = sin(num)
                st.write(f"sin({num}) = {result}")
            elif func == "Cosine":
                result = cos(num)
                st.write(f"cos({num}) = {result}")
            elif func == "Tangent":
                result = tan(num)
                st.write(f"tan({num}) = {result}")
            elif func == "Square Root":
                if num >= 0:
                    result = sqrt(num)
                    st.write(f"sqrt({num}) = {result}")
                else:
                    st.error("Error! Square root of a negative number.")
            elif func == "Logarithm":
                if num > 0:
                    result = log(num)
                    st.write(f"log({num}) = {result}")
                else:
                    st.error("Error! Logarithm only defined for positive numbers.")
            elif func == "Exponential":
                result = exp(num)
                st.write(f"exp({num}) = {result}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Statistical Functions
def statistical_plots():
    st.subheader("Statistical Analysis")

    data_type = st.radio("Is your data grouped or ungrouped?", ("Ungrouped", "Grouped"))

    if data_type == "Ungrouped":
        ungrouped_data = st.text_area("Enter your ungrouped data (comma-separated)", "1, 2, 3, 4, 5, 6")
        try:
            data = np.array([float(i.strip()) for i in ungrouped_data.split(",")])
            plot_type = st.selectbox("Select plot type", ("Histogram", "Box Plot"))

            if st.button("Plot Ungrouped Data"):
                fig, ax = plt.subplots()
                if plot_type == "Histogram":
                    ax.hist(data, bins='auto', color='blue', alpha=0.7)
                    ax.set_title("Histogram of Ungrouped Data")
                elif plot_type == "Box Plot":
                    ax.boxplot(data)
                    ax.set_title("Box Plot of Ungrouped Data")
                st.pyplot(fig)

            # Displaying basic statistics for ungrouped data
            mean = np.mean(data)
            median = np.median(data)
            std_dev = np.std(data)
            st.write(f"Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}")
        except Exception as e:
            st.error(f"Error processing ungrouped data: {e}")

    elif data_type == "Grouped":
        intervals = st.text_area("Enter group intervals (comma-separated, e.g., 0-10, 11-20)", "0-10, 11-20")
        frequencies = st.text_area("Enter frequencies (comma-separated)", "5, 10")
        try:
            interval_ranges = intervals.split(",")
            freq_data = np.array([int(i) for i in frequencies.split(",")])

            if len(freq_data) != len(interval_ranges):
                st.error("Error: The number of frequencies must match the number of intervals.")
                return

            # Calculating midpoints of intervals
            midpoints = [(int(interval.split('-')[0]) + int(interval.split('-')[1])) / 2 for interval in interval_ranges]

            plot_type = st.selectbox("Select plot type for grouped data", ("Bar Chart", "Histogram"))

            if st.button("Plot Grouped Data"):
                fig, ax = plt.subplots()
                if plot_type == "Bar Chart":
                    ax.bar(midpoints, freq_data, color='purple', alpha=0.7)
                    ax.set_title("Bar Chart of Grouped Data")
                    ax.set_xlabel("Midpoints")
                    ax.set_ylabel("Frequency")
                elif plot_type == "Histogram":
                    ax.hist(midpoints, weights=freq_data, bins=len(midpoints), color='green', alpha=0.7)
                    ax.set_title("Histogram of Grouped Data")
                st.pyplot(fig)

            # Displaying basic statistics for grouped data
            mean = np.average(midpoints, weights=freq_data)
            st.write(f"Mean (Weighted): {mean}")
        except Exception as e:
            st.error(f"Error processing grouped data: {e}")

# Sidebar for feature selection
st.sidebar.title("Choose a Feature")
feature = st.sidebar.radio("Select a feature", ("Basic Calculator", "Scientific Functions", "Statistical Plots"))

# Display the selected feature
if feature == "Basic Calculator":
    calculator()
elif feature == "Scientific Functions":
    scientific_functions()
elif feature == "Statistical Plots":
    statistical_plots()
