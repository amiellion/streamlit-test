import streamlit as st
from page_components.pages_intro import intro
from page_components.pages_mapping_demo import mapping_demo
from page_components.pages_plotting import plotting_demo
from page_components.pages_dataframe import data_frame_demo
from page_components.pages_aggrid import aggrid_component
from page_components.pages_aggrid_react import aggrid_react

page_names_to_funcs = {
    "—": intro,
    "Plotting Demo": plotting_demo,
    "Mapping Demo": mapping_demo,
    "DataFrame Demo": data_frame_demo,
    "AgGrid(Streamlit) Demo": aggrid_component,
    "AgGrid(React) Demo": aggrid_react
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name](page_names_to_funcs)