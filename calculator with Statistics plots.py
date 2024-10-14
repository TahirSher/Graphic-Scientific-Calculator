import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from math import sin, cos, tan, sqrt, log, exp

# Title of the app
st.title('Graphic, Scientific & Statistical Calculator')

# Calculator functionality
def calculator():
    st.subheader("Basic Operations")
    num1 = st.number_input("Enter first number", step=1e-6, format="%.6f", key="num1")
    num2 = st.number_input("Enter second number", step=1e-6, format="%.6f", key="num2")
    operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"), key="operation")

    if st.button("Calculate Basic Operation"):
        try:
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
        except Exception as e:
            st.error(f"Error during calculation: {e}")
        st.stop()  # For debugging

def scientific_functions():
    st.subheader("Scientific Functions")
    num = st.number_input("Enter a number for scientific calculation", step=1e-6, format="%.6f")
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
        except Exception as e:
            st.error(f"Error during scientific calculation: {e}")
        st.stop()  # For debugging

def plot_function():
    st.subheader("Plot a Function")
    func_choice = st.selectbox("Select a function to plot", ("Sine", "Cosine", "Tangent", "Exponential", "Square Root"))
    x_min = st.number_input("Enter the minimum x value", -100, 0, -10)
    x_max = st.number_input("Enter the maximum x value", 0, 100, 10)

    if st.button("Plot Function"):
        progress_bar = st.progress(0)  # Progress bar for user feedback
        try:
            x = np.linspace(x_min, x_max, 400)
            progress_bar.progress(30)

            if func_choice == "Sine":
                y = np.sin(x)
            elif func_choice == "Cosine":
                y = np.cos(x)
            elif func_choice == "Tangent":
                y = np.tan(x)
            elif func_choice == "Exponential":
                y = np.exp(x)
            elif func_choice == "Square Root":
                y = np.sqrt(np.clip(x, 0, None))
            progress_bar.progress(60)

            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.set_title(f'Plot of {func_choice}(x)')
            ax.grid(True)
            st.pyplot(fig)
            progress_bar.progress(100)
        except Exception as e:
            st.error(f"Error during plotting: {e}")
        st.stop()  # For debugging

def symbolic_operations():
    st.subheader("Symbolic Differentiation and Integration")
    x = sp.symbols('x')
    expr = st.text_input("Enter an expression in terms of x (e.g., x**2 + 2*x + 1)")

    if expr:
        try:
            expr = sp.sympify(expr)
            derivative = sp.diff(expr, x)
            integral = sp.integrate(expr, x)

            st.write(f"Expression: {expr}")
            st.write(f"Derivative: {derivative}")
            st.write(f"Indefinite integral: {integral}")
        except Exception as e:
            st.error(f"Error parsing expression: {e}")
        st.stop()  # For debugging

def statistical_plots():
    st.subheader("Statistical Plots")
    data_type = st.radio("Is your data grouped or ungrouped?", ("Ungrouped", "Grouped"))

    if data_type == "Ungrouped":
        ungrouped_data = st.text_area("Enter your ungrouped data (comma-separated)", "1, 2, 3, 4, 5, 6")
        try:
            data = np.array([float(i) for i in ungrouped_data.split(",") if i.strip() != ""])

            plot_type = st.selectbox("Select plot type", ("Histogram", "Box Plot"))

            if st.button("Plot Ungrouped Data"):
                fig, ax = plt.subplots()
                if plot_type == "Histogram":
                    ax.hist(data, bins='auto', color='blue', alpha=0.7, rwidth=0.85)
                elif plot_type == "Box Plot":
                    ax.boxplot(data)
                st.pyplot(fig)
        except Exception as e:
            st.error(f"Error processing ungrouped data: {e}")
        st.stop()  # For debugging

    elif data_type == "Grouped":
        intervals = st.text_area("Enter group intervals (comma-separated, e.g., 0-10, 11-20)", "0-10, 11-20")
        frequencies = st.text_area("Enter frequencies (comma-separated)", "5, 10")
        try:
            interval_ranges = intervals.split(",")
            freq_data = np.array([int(i) for i in frequencies.split(",") if i.strip() != ""])

            if len(freq_data) != len(interval_ranges):
