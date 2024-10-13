import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from math import sin, cos, tan, sqrt, log, exp, pi

# Title of the app
st.title('Graphic, Scientific & Statistical Calculator')

# Inject CSS for hover color change on button
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50; /* Default button color */
        color: white;
    }
    div.stButton > button:first-child:hover {
        background-color: #45a049; /* Hover color */
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Calculator functionality
def calculator():
    st.subheader("Basic Operations")

    # Input numbers and operation
    num1 = st.number_input("Enter first number", step=1e-6, format="%.6f", key="basic_num1")
    num2 = st.number_input("Enter second number", step=1e-6, format="%.6f", key="basic_num2")
    operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"), key="basic_operation")

    # Add "Calculate" button
    if st.button("Calculate Basic Operation", key="calc_button"):
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

def scientific_functions():
    st.subheader("Scientific Functions")

    # Input number
    num = st.number_input("Enter a number for scientific calculation", step=1e-6, format="%.6f", key="sci_num")
    func = st.selectbox("Choose a function", ("Sine", "Cosine", "Tangent", "Square Root", "Logarithm", "Exponential"), key="sci_func")

    # Add "Calculate" button
    if st.button("Calculate Scientific Function", key="sci_calc_button"):
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
                st.error("Error! Cannot compute square root of a negative number.")
        elif func == "Logarithm":
            if num > 0:
                result = log(num)
                st.write(f"log({num}) = {result}")
            else:
                st.error("Error! Logarithm only defined for positive numbers.")
        elif func == "Exponential":
            result = exp(num)
            st.write(f"exp({num}) = {result}")

def plot_function():
    st.subheader("Plot a Function")

    # Choose a function to plot
    func_choice = st.selectbox("Select a function to plot", ("Sine", "Cosine", "Tangent", "Exponential", "Square Root"), key="plot_func")
    x_min = st.number_input("Enter the minimum x value", -100, 0, -10, key="plot_xmin")
    x_max = st.number_input("Enter the maximum x value", 0, 100, 10, key="plot_xmax")

    if st.button("Plot Function", key="plot_button"):
        x = np.linspace(x_min, x_max, 400)
        
        if func_choice == "Sine":
            y = np.sin(x)
            st.write("Plot of sin(x)")
        elif func_choice == "Cosine":
            y = np.cos(x)
            st.write("Plot of cos(x)")
        elif func_choice == "Tangent":
            y = np.tan(x)
            st.write("Plot of tan(x)")
        elif func_choice == "Exponential":
            y = np.exp(x)
            st.write("Plot of exp(x)")
        elif func_choice == "Square Root":
            y = np.sqrt(np.clip(x, 0, None))  # Clip to avoid negative values for sqrt
            st.write("Plot of sqrt(x)")

        # Plot the graph
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.grid(True)
        st.pyplot(fig)

def symbolic_operations():
    st.subheader("Symbolic Differentiation and Integration")

    x = sp.symbols('x')
    expr = st.text_input("Enter an expression in terms of x (e.g., x**2 + 2*x + 1)", key="symbolic_expr")
    if st.button("Calculate Symbolic Operation", key="symbolic_button") and expr:
        expr = sp.sympify(expr)
        derivative = sp.diff(expr, x)
        integral = sp.integrate(expr, x)

        st.write(f"Expression: {expr}")
        st.write(f"Derivative of the expression: {derivative}")
        st.write(f"Indefinite integral of the expression: {integral}")

# New function: Statistical Plots
def statistical_plots():
    st.subheader("Statistical Plots")

    # Input data for statistical analysis
    data_type = st.radio("Is your data grouped or ungrouped?", ("Ungrouped", "Grouped"))

    if data_type == "Ungrouped":
        ungrouped_data = st.text_area("Enter your ungrouped data (comma-separated)", "1, 2, 3, 4, 5, 6", key="ungrouped_data")
        data = np.array([float(i) for i in ungrouped_data.split(",")])
        
        plot_type = st.selectbox("Select plot type", ("Histogram", "Box Plot"), key="ungrouped_plot")

        if st.button("Plot Ungrouped Data", key="ungrouped_plot_button"):
            if plot_type == "Histogram":
                st.write("Histogram of Ungrouped Data")
                fig, ax = plt.subplots()
                ax.hist(data, bins='auto', color='blue', alpha=0.7, rwidth=0.85)
                st.pyplot(fig)
            elif plot_type == "Box Plot":
                st.write("Box Plot of Ungrouped Data")
                fig, ax = plt.subplots()
                ax.boxplot(data)
                st.pyplot(fig)
                
    elif data_type == "Grouped":
        st.write("For grouped data, input values in two columns: Group Intervals and Frequencies.")
        intervals = st.text_area("Enter group intervals (comma-separated, e.g., 0-10, 11-20, etc.)", "0-10, 11-20, 21-30", key="group_intervals")
        frequencies = st.text_area("Enter frequencies (comma-separated)", "5, 10, 8", key="group_freqs")
        
        interval_ranges = intervals.split(",")
        freq_data = np.array([int(i) for i in frequencies.split(",")])
        midpoints = [(int(interval.split('-')[0]) + int(interval.split('-')[1])) / 2 for interval in interval_ranges]

        plot_type = st.selectbox("Select plot type for grouped data", ("Bar Chart", "Histogram"), key="grouped_plot")

        if st.button("Plot Grouped Data", key="grouped_plot_button"):
            if plot_type == "Bar Chart":
                st.write("Bar Chart of Grouped Data")
                fig, ax = plt.subplots()
                ax.bar(midpoints, freq_data, color='purple', alpha=0.7)
                st.pyplot(fig)
            elif plot_type == "Histogram":
                st.write("Histogram of Grouped Data")
                fig, ax = plt.subplots()
                ax.hist(midpoints, weights=freq_data, bins=len(midpoints), color='green', alpha=0.7)
                st.pyplot(fig)

# Sidebar feature selection
st.sidebar.title("Choose a Feature")
feature = st.sidebar.radio("Select a feature", ("Basic Calculator", "Scientific Functions", "Plot Functions", "Symbolic Calculations", "Statistical Plots"))

# Display the corresponding feature
if feature == "Basic Calculator":
    calculator()
elif feature == "Scientific Functions":
    scientific_functions()
elif feature == "Plot Functions":
    plot_function()
elif feature == "Symbolic Calculations":
    symbolic_operations()
elif feature == "Statistical Plots":
    statistical_plots()
