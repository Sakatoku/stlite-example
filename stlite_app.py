import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit example')

rnd_data = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])
st.line_chart(rnd_data)
