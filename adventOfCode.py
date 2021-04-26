# -*- coding: utf-8 -*-
"""
Advent Of Code
ArcelorMittal FOS 2021
@author: Cédric LEBOCQ
"""

# %% Imports

import os.path
import pandas as pd  
import matplotlib.pyplot as plt
import streamlit as st


def app():

    # %% Chargement des datasets
    
    # chargement du dataSet des participants
    ds_users = pd.read_csv("data/users.csv")
    ds_users = ds_users.set_index('Trigramme')
    # chargement du dataset des solutions
    ds_solutions = pd.read_csv("data/solutions.csv")
    ds_solutions = ds_solutions.set_index('Puzzle')
    
    # %% Fonction pour afficher le graphe d'avancement
    def plotUsers(ds):
        fig, ax = plt.subplots()
        ds.sort_values(by=['PuzzleEnCours']).plot.barh(y='PuzzleEnCours', ax=ax, width=0.7)
        plt.xticks(ds['PuzzleEnCours'], ds['PuzzleEnCours']) # location, labels
        #ax.legend(['Avancement par personne'], loc = 'lower left')
        st.pyplot(fig)
    
    # %%
    st.title("Bienvenue dans Advent Of Code !")
    
    
    html_counter = 'Vous êtes le visiteur <a href="https://www.freecounterstat.com" title="website view counter"><img src="https://counter2.stat.ovh/private/freecounterstat.php?c=fude952d8kt6jhabdmdyhxf792ujx8b7" border="0" title="website view counter" alt="website view counter"></a>'
    st.markdown(html_counter,unsafe_allow_html=True)
    
    st.markdown("""
    Sur ce site, vous trouverez régulièrement de nouveau "puzzles" à résoudre. Une seule contrainte,  pour passer au puzzle suivant, il faut résoudre le puzzle en cours. C'est le même principe que pour le **calendrier de l'avent**. 
    
    Chaque puzzle n'a qu'**une seule solution**. Libre à vous de choisir quel moyen vous allez utiliser pour la trouver. L'idéal est de faire un court programme (*quel que soit votre langage favori*),  mais encore fois, seul le résultat compte pour déverrouiller l'étape suivante. 
    
    L'objectif est de **s'amuser et d'apprendre** en même temps. Profitez en pour apprendre un nouveau langage, Python, Java, Powershell, C# , VB.net,  Javascript, C++, ce n'est pas le choix qui manque ! Vous n'êtes même pas obligé d'installer quoi que ce soit sur votre machine, il y a de nombreux compilateurs / éditeurs en ligne :
    
     - [Python avec repl.it](https://replit.com/)
     - [VB.net et C# avec Netfiddle](https://dotnetfiddle.net/)
     - [Javascript avec Playcode.io](https://playcode.io)
     - [C et C++ avec Onlinegdb](https://www.onlinegdb.com/online_c++_compiler)
    """)
    
    # Récupére les paramétres sur l'URL
    app_state = st.experimental_get_query_params()
    if not "con_trigram" in app_state:
         
        st.markdown("""
        # Pour participer, identifiez vous
        Si vous n'êtes pas inscrit, contactez moi : [cedric.lebocq@arcelormittal.com](mailto:cedric.lebocq@arcelormittal.com)
                    """)
        
        ###############################################################################
        #Crée deux zones en colonne pour l'affichage du login #########################
        ###############################################################################
        txt_input, btn_login = st.beta_columns(2)
        
        with txt_input:
            trigram = st.text_input(label='Utilisez votre trigramme',max_chars=3,key="trigram")
            trigram = trigram.upper()
            
            with st.beta_expander("Comment est constitué votre trigramme ?"):
                st.write("Votre **trigramme**, c'est la première lettre de votre prénom, suivie des deux premières de votre nom. Par exemple, **L**uke **Sk**ywalker donne **LSK**")
        
        login_ok = False
        message = ''
        
        with btn_login:
            st.markdown('Cliquez le bouton *login* pour vous identifier')
            if st.button('Login', help='Cliquez pour vous identifier'):
                if len(trigram) == 3 :
                    if trigram in ds_users.index:
                        login_ok = True
                    else:
                        message = "Ce trigramme **n'existe pas**..."
                else:
                    message = "Le trigramme doit faire **3 caractères** de long..."
        ###############################################################################
                   
        if login_ok:
            # Save trigram in session
            st.experimental_set_query_params(con_trigram=trigram)  
    
        else:
            st.markdown(message)
            st.stop()
    else:
        #on récupére le paramétre de la ligne de commande
        trigram = app_state["con_trigram"][0]
    
    
    # %%
    st.markdown("## Graphique Avancement par personne")
    with st.beta_expander("Ouvrir le graphique"):
        plotUsers(ds_users)
    
    # %%
    
    message = f"## **Bienvenue** {ds_users.loc[trigram]['Prenom']} {ds_users.loc[trigram]['Nom']}"    
    st.markdown(message)    
    
    # %%
    
    # Puzzle en cours de la personne connectée
    puzzle = ds_users.loc[trigram]['PuzzleEnCours']
    # nom du fichier associé
    fname = f'data/puzzle{puzzle:03d}.md'
    # nom de la solution
    sname = f'data/solution{puzzle:03d}.md'
    
    
    #Affichage du puzzle
    if os.path.isfile(fname):
        with open(fname,'r',encoding='utf8') as f:
            lines = f.readlines()
        
        lines = ''.join(lines)
        st.markdown(f'## Votre puzzle en cours est le numéro {puzzle} :')    
        st.markdown(lines)
    else:
        st.markdown(f"**le puzzle numéro {puzzle} n'existe pas encore, merci de repasser un peu plus tard...**")
        st.stop()
    
    #Chargement de la solution
    if os.path.isfile(sname):
        with open(sname,'r',encoding='utf8') as f:
            sol_lines = f.readlines()
        
        sol_lines = ''.join(sol_lines)
    else:
        sol_lines = ''
    
    
    
    # %%
    
    ###############################################################################
    # Crée deux zones en colonne pour la saisie de la solution ####################
    ###############################################################################
    
    txt_solution_input, btn_submit_solution = st.beta_columns(2)
    
    with txt_solution_input:
        solution = st.text_input(label='Entrez la solution',key="solution")
    
    solution_found=False
    with btn_submit_solution:
        st.markdown('Cliquez le bouton *Soumettre* pour vérifier')
        if st.button('Soumettre', help='Soumettre votre solution'):
            #solution attendue
            good_solution = str(ds_solutions.loc[puzzle]['Solution'])
            if solution == good_solution:
                solution_found=True
        else:
            st.stop()
    ###############################################################################
    
    if solution_found:
        st.markdown("**Bravo, Bien joué !** c’est la bonne solution. Vous avez déverrouillé le puzzle suivant.")
        st.markdown(sol_lines)
        # update du dataset users.csv
        ds_users.at[trigram,'PuzzleEnCours']= ds_users.loc[trigram]['PuzzleEnCours']+1
        ds_users.to_csv("data/users.csv")
    else:
        st.markdown("Désolé, **ce n'est pas la bonne solution...**")
