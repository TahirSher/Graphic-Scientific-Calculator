import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, tan, sqrt, log, exp

# Title of the app
st.title('Basic Calculator')

def calculator():
    st.subheader("Basic Operations")
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

# Sidebar feature selection
st.sidebar.title("Choose a Feature")
feature = st.sidebar.radio("Select a feature", ("Basic Calculator",))

# Display the corresponding feature
if feature == "Basic Calculator":
    calculator()
