# Simulateur Résultat Élection Législatives 2nd tour 1ère circonscription Haute-Loire

Cette application Streamlit permet de calculer en temps réel le résultat de l'élection législative pour la 1ère circonscription de la Haute-Loire au 2nd tour, selon différents critères d'abstention et de report de voix des électeurs.

## Fonctionnalités

- **Pourcentage d'abstention des électeurs** : Ajustez les pourcentages d'abstention des électeurs des candidats Celline GACON, Cécile GALLIEN et Electre DRACOS au 1er tour.
- **Report des voix des électeurs** : Déterminez le pourcentage de voix des électeurs de ces mêmes candidats qui se reportent sur Laurent WAUQUIEZ ou Alexandre HEUZEY au 2nd tour.
- **Résultats en temps réel** : Visualisez en temps réel les résultats de l'élection sous forme de graphique en barres horizontales et de texte conditionnel indiquant le candidat élu.

## Comment utiliser

1. Ajustez les sliders dans la barre latérale pour définir les pourcentages d'abstention et de report des voix.
2. Les résultats s'affichent en temps réel dans le graphique et le texte principal.
3. Cliquez sur les liens pour découvrir les programmes des candidats.

## Déploiement

Cette application est déployée sur [resultat-circo1-hauteloire.streamlit.app](https://resultat-circo1-hauteloire.streamlit.app/) et peut être accédée via le lien.

## Installation locale

Pour exécuter cette application localement, suivez les étapes ci-dessous :

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/Stabadev/resultat.git
   ```
2. Accédez au répertoire du projet :
   ```bash
   cd resultat
   ```
3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
4. Exécutez l'application :
   ```bash
   streamlit run app.py
   ```

## Exemple de résultat

Au soir du 2nd tour des élections législatives, le député de la 1ère circonscription de la Haute-Loire sera :

- **Laurent WAUQUIEZ** si le pourcentage de voix en sa faveur est supérieur à celui d'Alexandre HEUZEY.
- **Alexandre HEUZEY** si le pourcentage de voix en sa faveur est supérieur à celui de Laurent WAUQUIEZ.

Cliquez sur les liens pour découvrir les programmes des candidats respectifs.

## Auteurs

- Alexandre ROGUES- [Stabadev](https://github.com/Stabadev)