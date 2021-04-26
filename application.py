# -*- coding: utf-8 -*-
"""
Advent Of Code
ArcelorMittal FOS 2021
@author: Cédric LEBOCQ
"""

import adventOfCode
import admin
import streamlit as st
PAGES = {
    "Advent Of Code": adventOfCode,
    "Admin": admin
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Allez à", list(PAGES.keys()))
page = PAGES[selection]
page.app()