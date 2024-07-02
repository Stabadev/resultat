vote_wauquiez = 27013
vote_heuzey = 25091
vote_gaccon = 13694
vote_gallien = 6932
vote_dracos = 668

# chiffres obtenus sur le site https://www.resultats-elections.interieur.gouv.fr/legislatives2024/ensemble_geographique/84/43/4301/index.html

def resultat(prc_abs_gaccon, prc_abs_gallien, prc_abs_dracos, prc_repo_gaccon_wau, prc_repo_gallien_wau, prc_repo_dracos_wau):
	tot_repo_gaccon = (1-prc_abs_gaccon)*vote_gaccon
	tot_repo_gallien = (1-prc_abs_gallien)*vote_gallien
	tot_repo_dracos = (1-prc_abs_dracos)*vote_dracos

	repo_gaccon_wau = prc_repo_gaccon_wau*tot_repo_gaccon
	repo_gallien_wau = prc_repo_gallien_wau*tot_repo_gallien
	repo_dracos_wau = prc_repo_dracos_wau*tot_repo_dracos

	repo_gaccon_heu = tot_repo_gaccon-repo_gaccon_wau
	repo_gallien_heu = tot_repo_gallien-repo_gallien_wau
	repo_dracos_heu = tot_repo_dracos-repo_dracos_wau

	total_vote = vote_wauquiez + vote_heuzey + tot_repo_gaccon + tot_repo_gallien + tot_repo_dracos
	total_wau = vote_wauquiez + repo_gaccon_wau + repo_gallien_wau + repo_dracos_wau
	total_heu = vote_heuzey + repo_gaccon_heu + repo_gallien_heu + repo_dracos_heu

	res_wau = total_wau/total_vote
	res_heu = total_heu/total_vote


	return(res_wau, res_heu)
	
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


# Configuration de la page pour une mise en page large
st.set_page_config(layout="wide")

# Interface utilisateur avec Streamlit
st.title("Simulateur résultat élection législatives")
st.markdown("*2nd tour - 1ère circonscription Haute-Loire*")

st.sidebar.header("Pourcentage d'absentation des électeurs au 1er tour du candidat")
p1 = st.sidebar.slider('Celline GACON', 0.0, 100.0, 50.0, step = 1.0)/100
p2 = st.sidebar.slider('Cécile GALLIEN', 0.0, 100.0, 50.0, step = 1.0)/100
p3 = st.sidebar.slider('Electre DRACOS', 0.0, 100.0, 50.0, step = 1.0)/100

st.sidebar.header("Pourcentage de report des voix des électeurs en faveur du candidat Laurent WAUQUIEZ (et donc le reste en faveur du candidat Alexandre HEUZEY)")
r1 = st.sidebar.slider('r1', 0.0, 100.0, 50.0, step = 1.0)/100
r2 = st.sidebar.slider('r2', 0.0, 100.0, 50.0, step = 1.0)/100
r3 = st.sidebar.slider('r3', 0.0, 100.0, 50.0, step = 1.0)/100

res_wau, res_heu = resultat(p1, p2, p3, r1, r2, r3)

# Affichage du texte explicatif
st.markdown("""
En supposant que :
- Tous les électeurs du candidat Laurent WAUQUIEZ au 1er tour revotent pour Laurent WAUQUIEZ au 2nd tour
- Tous les électeurs du candidat Alexandre HEUZEY au 1er tour revotent pour Alexandre HEUZEY au 2nd tour
""")
# Affichage du texte dynamique en fonction des valeurs des sliders
st.markdown(f"""
- **{round(p1*100)}%** des électeurs du candidat Celline GACON au 1er tour s'abstiennent au 2nd tour
- **{round(p2*100)}%** des électeurs du candidat Cécile GALLIEN au 1er tour s'abstiennent au 2nd tour
- **{round(p3*100)}%** des électeurs du candidat Electre DRACOS au 1er tour s'abstiennent au 2nd tour
- **{round(r1*100)}%** des électeurs du candidat Celline GACON reportent leur vote sur le candidat Laurent WAUQUIEZ et donc **{round((1-r1)*100)}%** des électeurs reportent leur vote sur le candidat Alexandre HEUZEY
- **{round(r2*100)}%** des électeurs du candidat Cécile GALLIEN reportent leur vote sur le candidat Laurent WAUQUIEZ et donc **{round((1-r2)*100)}%** des électeurs reportent leur vote sur le candidat Alexandre HEUZEY
- **{round(r3*100)}%** des électeurs du candidat Electre DRACOS reportent leur vote sur le candidat Laurent WAUQUIEZ et donc **{round((1-r3)*100)}%** des électeurs reportent leur vote sur le candidat Alexandre HEUZEY
""")

import streamlit as st
import plotly.graph_objects as go


# Création de l'histogramme en barre horizontale avec Plotly
fig = go.Figure(go.Bar(
    x=[res_heu, res_wau],
    y=['Alexandre HEUZEY', 'Laurent WAUQUIEZ'],
    orientation='h',
    marker=dict(color=['#000080', 'blue']),  # Bleu marine et vert
    text=[f'{res_heu:.4f}', f'{res_wau:.4f}'],
    textposition='outside',
    width=0.3  # Largeur des barres, plus petite valeur pour barres plus fines
))

fig.update_layout(
    title='Résultats des votes',
    xaxis=dict(range=[0, 0.7]),
    yaxis=dict(showticklabels=True),
    height=200,  # Hauteur totale du graphique réduite
    margin=dict(l=40, r=40, t=40, b=40),
    bargap=0.1  # Espace entre les barres
)

# Désactiver les options de transformation du graphique
config = {
    'scrollZoom': False,
    'displayModeBar': False,
    'staticPlot': True  # Rendre le graphique statique
}

st.plotly_chart(fig, use_container_width=True, config = config)

# Texte conditionnel et bouton
if res_wau > res_heu:
    st.markdown("### Laurent WAUQUIEZ sera élu député de la 1ère circonscription de la Haute-Loire au soir du 2nd tour")

else:
    st.markdown("### Alexandre HEUZEY sera élu député de la 1ère circonscription de la Haute-Loire au soir du 2nd tour")

if res_wau > res_heu:
    st.markdown("[Découvrir le programme des Républicains](https://republicains.fr/)")
else:
    st.markdown("[Découvrir le programme du Rassemblement National](https://rassemblementnational.fr/)")