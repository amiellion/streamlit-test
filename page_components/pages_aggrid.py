from st_aggrid import AgGrid
import streamlit as st
import pandas as pd

def aggrid_component(page_names_to_funcs): 
    
    st.markdown(f"# {list(page_names_to_funcs.keys())[4]}")
    st.write(
        """
        This demo shows how to use `AgGrid` component to visualize csv data.
        
        [Github: streamlit-aggrid](https://github.com/PablocFonseca/streamlit-aggrid)
        
        (Data courtesy of the [fivethirtyeight](https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv).)
        """
    )
    
    df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
    AgGrid(df)