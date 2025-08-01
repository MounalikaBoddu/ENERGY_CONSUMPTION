'''import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data with error handling
try:
    df = pd.read_csv("energy_data_india.csv")
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Title
st.title("Indian Residential Energy Dashboard")

# Sidebar filter
region = st.sidebar.selectbox("Select Region", ["All"] + sorted(df["Region"].unique().tolist()))
if region != "All":
    df = df[df["Region"] == region]

# Overview
st.subheader("Household Energy Consumption Overview")
st.write(df.head())

# Metrics
avg_energy = df["Monthly_Energy_Consumption_kWh"].mean()
total_energy = df["Monthly_Energy_Consumption_kWh"].sum()

col1, col2 = st.columns(2)
col1.metric("Average Monthly Consumption (kWh)", f"{avg_energy:.2f}")
col2.metric("Total Energy Consumption (kWh)", f"{total_energy:.0f}")

# Scatter plot: Income vs Energy
st.subheader("Income vs Energy Consumption")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=df, x="Monthly_Income_INR", y="Monthly_Energy_Consumption_kWh", hue="Region", ax=ax1)
ax1.set_xlabel("Monthly Income (INR)")
ax1.set_ylabel("Energy Consumption (kWh)")
st.pyplot(fig1)

# Appliance-wise bar chart
st.subheader("Appliance-wise Count vs Energy Consumption")
appliances = ["Appliance_AC", "Appliance_Fan", "Appliance_Light", "Fridge", "Washing_Machine", "EV_Charging"]
selected_appliance = st.selectbox("Select Appliance", appliances)

fig2, ax2 = plt.subplots()
sns.barplot(
    data=df,
    x=selected_appliance,
    y="Monthly_Energy_Consumption_kWh",
    estimator='mean',
    ax=ax2
)
ax2.set_xlabel(f"No. of {selected_appliance.replace('_', ' ')}")
ax2.set_ylabel("Avg Energy Consumption (kWh)")
st.pyplot(fig2)

# Smart Recommendations
st.subheader("Smart Recommendations")

high_consumers = df[df["Monthly_Energy_Consumption_kWh"] > 250]
ev_households = df[df["EV_Charging"] == 1]

if not high_consumers.empty:
    st.warning("High Energy Consumption Households (>250 kWh):")
    for hid in high_consumers["Household_ID"]:
        st.text(f"• Household ID: {hid}")

if not ev_households.empty:
    st.info("Households Using EV Charging:")
    for hid in ev_households["Household_ID"]:
        st.text(f"• Household ID: {hid}")'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np  # ✅ Import NumPy for aggregation function

# Load data with error handling
try:
    df = pd.read_csv("energy_data_india.csv")
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Title
st.title("Indian Residential Energy Dashboard")

# Sidebar filter
region = st.sidebar.selectbox("Select Region", ["All"] + sorted(df["Region"].unique().tolist()))
if region != "All":
    df = df[df["Region"] == region]

# Overview
st.subheader("Household Energy Consumption Overview")
st.write(df.head())

# Metrics
avg_energy = df["Monthly_Energy_Consumption_kWh"].mean()
total_energy = df["Monthly_Energy_Consumption_kWh"].sum()

col1, col2 = st.columns(2)
col1.metric("Average Monthly Consumption (kWh)", f"{avg_energy:.2f}")
col2.metric("Total Energy Consumption (kWh)", f"{total_energy:.0f}")

# Scatter plot: Income vs Energy
st.subheader("Income vs Energy Consumption")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=df, x="Monthly_Income_INR", y="Monthly_Energy_Consumption_kWh", hue="Region", ax=ax1)
ax1.set_xlabel("Monthly Income (INR)")
ax1.set_ylabel("Energy Consumption (kWh)")
st.pyplot(fig1)

# Appliance-wise bar chart
st.subheader("Appliance-wise Count vs Energy Consumption")
appliances = ["Appliance_AC", "Appliance_Fan", "Appliance_Light", "Fridge", "Washing_Machine", "EV_Charging"]
selected_appliance = st.selectbox("Select Appliance", appliances)

fig2, ax2 = plt.subplots()
sns.barplot(
    data=df,
    x=selected_appliance,
    y="Monthly_Energy_Consumption_kWh",
    estimator=np.mean,  # ✅ Use function, not string
    ax=ax2
)
ax2.set_xlabel(f"No. of {selected_appliance.replace('_', ' ')}")
ax2.set_ylabel("Avg Energy Consumption (kWh)")
st.pyplot(fig2)

# Smart Recommendations
st.subheader("Smart Recommendations")

high_consumers = df[df["Monthly_Energy_Consumption_kWh"] > 250]
ev_households = df[df["EV_Charging"] == 1]

if not high_consumers.empty:
    st.warning("High Energy Consumption Households (>250 kWh):")
    for hid in high_consumers["Household_ID"]:
        st.text(f"• Household ID: {hid}")

if not ev_households.empty:
    st.info("Households Using EV Charging:")
    for hid in ev_households["Household_ID"]:
        st.text(f"• Household ID: {hid}")

