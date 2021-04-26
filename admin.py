# -*- coding: utf-8 -*-
"""
Advent Of Code
ArcelorMittal FOS 2021
@author: Cédric LEBOCQ
"""
# %% Imports

import streamlit as st
import SessionState 
import pandas as pd
import base64

# %% Chargement des datasets

def app():
    
    # chargement du dataSet des participants
    ds_users = pd.read_csv("data/users.csv")
    # chargement du dataSet des solutions
    ds_solutions = pd.read_csv("data/solutions.csv")
    
    def get_table_download_link(df,filename,link_text):
        """Generates a link allowing the data in a given panda dataframe to be downloaded
        in:  dataframe
        out: href string
        """
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
        href = f'<a href="data:file/csv;base64,{b64}" Download="{filename}">{link_text}</a>'
        return href
    
    
    st.markdown("# Admin page")
    
    #########################   LOGIN   ###########################################
    state = SessionState.get()
    authenticated = False
    if hasattr(state,'authenticated'):
        authenticated = True
        
    if not authenticated:
        
        txt_input, btn_login = st.beta_columns(2)
        
        with txt_input:
            pwd = st.text_input(label='mot de passe',type='password')
            
        
        with btn_login:
            st.markdown('Entrez le mot de passe admin')
            if st.button('Login', help='Cliquez pour vous identifier'):
                if pwd == '#Aoc2021#':
                    state.authenticated = True
                    st.markdown("** Bienvenue Admin **")
                else:
                    st.markdown("** mot de passe incorrect **")
                    
    ###############################################################################                    
    if hasattr(state,'authenticated'):
        #Download fichier users               
        st.markdown("## Récupération du fichier des inscrits")
        st.markdown(get_table_download_link(ds_users,"users.csv","Download du fichier des inscrits (users.csv)"), unsafe_allow_html=True)
        
        # Upload fichier users
        st.markdown("## Remplacer le fichier des inscrits (users.csv)")
        uploaded_file = st.file_uploader("Séléctionner le fichier users.csv à uploader")
        if uploaded_file is not None:
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe)
            dataframe.to_csv("data/users.csv",index=False)
            st.markdown("**Fichier remplacé**")
            
        #Download fichier solutions               
        st.markdown("## Récupération du fichier des solutions")
        st.markdown(get_table_download_link(ds_solutions,"solutions.csv","Download du fichier des solutions (solutions.csv)"), unsafe_allow_html=True)
        
        # Upload fichier solutions
        st.markdown("## Remplacer le fichier des solutions (solutions.csv)")
        uploaded_file_s = st.file_uploader("Séléctionner le fichier solutions.csv à uploader")
        if uploaded_file_s is not None:
            dataframe = pd.read_csv(uploaded_file_s)
            st.write(dataframe)
            dataframe.to_csv("data/solutions.csv",index=False)
            st.markdown("**Fichier remplacé**")
            
            
