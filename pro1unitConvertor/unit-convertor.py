# import streamlit as st
 
# st.title("🌎Unit Convertor App")
# st.markdown("### Convert Lenght, Weight And Time Instentlly")
# st.write("Welcome! Select a category, enter a value and get the converted value instenltlly.")

# category= st.selectbox("Choose Category", ["Lenght", "Weight","Time"])

# def convert_units(category, value, unit):
#     if category == "Lenght":
#         if unit == "Kilometers to Miles":
#             return value * 0.621371
#         elif unit == "Miles to Kilometer":
#             return value / 0.621371
        
#         elif category == "Weight":
#             if unit == "Kilograms to Pounds":
#                 return value * 2.20462 
#             elif unit == "Pounds to Kilograms":
#                 return value / 2.20462
            
#         elif category == "Time":
#             if unit == "Seconds to Minutes":
#                 return value * 60
#             elif unit == "Minutes to Seconds":
#                 return value / 60
#             elif unit == "Minutes to Hours":
#                 return value / 60
#             elif unit == "Hours to Minutes":
#                 return value * 60
#             elif  unit == "Hours to Days":
#                 return value / 24
#             elif unit == "Days to Hours":
#                 return value * 24
        
#         if category == "Lenght":
#             unit = st.selectbox("📏 Select Unit", ["Kilometers to Miles", "Miles to Kilometer"])
#         elif category == "Weight":
#             unit = st.selectbox("🏋️‍♀️ Select Unit", ["Kilograms to Pounds", "Pounds to Kilograms"])
#         elif category == "Time":
#             unit = st.selectbox("⏰ Select Unit", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"]) 
        
#         value = st.number_input ("Enter Value to convert")

#         if st.button("Convert"):
#             result = convert_units( category , value, unit)
#             st.success(f"The result is {result:.0.2f}")

import streamlit as st

st.title("🌎 Unit Convertor App")
st.markdown("### Convert Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter a value and get the converted value instantly.")

category = st.selectbox("Choose Category", ["Length", "Weight", "Time"])

# Move selectbox and number_input outside the function
if category == "Length":
    unit = st.selectbox("📏 Select Unit", ["Kilometers to Miles", "Miles to Kilometer"])
elif category == "Weight":
    unit = st.selectbox("🏋️‍♀️ Select Unit", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏰ Select Unit", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

value = st.number_input("Enter Value to convert")

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometer":
            return value / 0.621371
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value * 60
        elif unit == "Minutes to Seconds":
            return value / 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
