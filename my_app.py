# %%
import streamlit as st # Handles User interface
import pandas as pd # Builds DF for model
import joblib # Loads saved model



# %%
model = joblib.load("Final_Model") # Loads exact model trained

# %%
st.title('Quantity Demand Forecast App') # Creates title for User Interface

st.write('Enter product details to get a prediction') # App instructions 

# %%
# User Input 


price = st.number_input("Product Price", min_value=0.0, step=0.1)
week = st.number_input('Week of', min_value = 1, max_value = 52, step =1)
is_weekend = st.selectbox("Is Weekend?", ['No', 'Yes'])
month = st.number_input("Month (1-12)", min_value=1, max_value=12, step=1)
year = st.number_input("Year", min_value=2020, max_value=2030, step=1)
day_of_week = st.selectbox("Day of Week", ['Monday', 'Tuesday', 'Wednesday', 
                                           'Thursday', 'Friday', 'Saturday', 'Sunday'])
category = st.selectbox('Category', ['Breakfast', 'Cleaning', 'Snacks', 'Frozen', 'drinks' ])


is_weekend_num = 1 if is_weekend == "Yes" else 0

# %%
# Create input dataframe 

input_df = pd.DataFrame([{
    'is_weekend': is_weekend, 
    'week': week,
    'day_of_week': day_of_week, 
    'month': month, 
    'year': year, 
    'price': price,
    'category': category}])

# %%
input_df

# %%
if st.button("Predicted Quantity"):
    prediction = model.predict(input_df)[0]
    st.success(f'Quantity Predicted{prediction: .2f}')



# %%


# %%



