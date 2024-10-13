import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from math import sin, cos, tan, sqrt, log, exp, pi

# Title of the app
st.title('Scientific Calculator with Plotting')

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
    num1 = st.number_input("Enter first number", step=1e-6, format="%.6f")
    num2 = st.number_input("Enter second number", step=1e-6, format="%.6f")
    operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

    # Add "Calculate" button
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

def scientific_functions():
    st.subheader("Scientific Functions")

    # Input number
    num = st.number_input("Enter a number for scientific calculation", step=1e-6, format="%.6f")
    func = st.selectbox("Choose a function", ("Sine", "Cosine", "Tangent", "Square Root", "Logarithm", "Exponential"))

    # Add "Calculate" button
    if st.button("Calculate"):
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
    func_choice = st.selectbox("Select a function to plot", ("Sine", "Cosine", "Tangent", "Exponential", "Square Root"))
    x_min = st.number_input("Enter the minimum x value", -100, 0, -10)
    x_max = st.number_input("Enter the maximum x value", 0, 100, 10)

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
    expr = st.text_input("Enter an expression in terms of x (e.g., x**2 + 2*x + 1
