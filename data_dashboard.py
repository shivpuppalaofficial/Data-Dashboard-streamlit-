
## 🔹 Project 4: Data Dashboard (Streamlit)
```python
# data_dashboard.py
import pandas as pd
import streamlit as st

# Sample dataset
data = {
    "Year": [2018, 2019, 2020, 2021, 2022],
    "Sales": [100, 150, 200, 250, 300],
    "Profit": [20, 50, 70, 90, 120]
}
df = pd.DataFrame(data)

st.title("📊 Data Dashboard")
st.write("Sample Sales Data")

st.line_chart(df.set_index("Year"))
st.bar_chart(df.set_index("Year"))
