import streamlit as st

def chiffrement_rail_fence(message, k):
    message = message.replace(" ", "").upper()
    n = len(message)
    rail = [['\n' for _ in range(n)] for _ in range(k)]
    
    ligne, col, dir_bas = 0, 0, False
    for char in message:
        if ligne == 0:
            dir_bas = True
        if ligne == k - 1:
            dir_bas = False
        
        rail[ligne][col] = char
        col += 1
        
        if dir_bas:
            ligne += 1
        else:
            ligne -= 1
    
    texte_chiffre = ''.join([''.join(row) for row in rail]).replace('\n', '')
    texte_chiffre_espacé = ' '.join(texte_chiffre[i:i+5] for i in range(0, len(texte_chiffre), 5))
    
    return texte_chiffre_espacé

def dechiffrement_rail_fence(texte_chiffre, k):
    texte_chiffre = texte_chiffre.replace(" ", "")
    n = len(texte_chiffre)
    rail = [['\n' for _ in range(n)] for _ in range(k)]
    
    ligne, col, dir_bas = 0, 0, False
    for i in range(n):
        if ligne == 0:
            dir_bas = True
        if ligne == k - 1:
            dir_bas = False
        
        rail[ligne][col] = '*'
        col += 1
        
        if dir_bas:
            ligne += 1
        else:
            ligne -= 1
    
    index = 0
    for i in range(k):
        for j in range(n):
            if (rail[i][j] == '*' and index < n):
                rail[i][j] = texte_chiffre[index]
                index += 1
    
    resultat = []
    ligne, col = 0, 0
    for i in range(n):
        if ligne == 0:
            dir_bas = True
        if ligne == k - 1:
            dir_bas = False
        
        if rail[ligne][col] != '\n':
            resultat.append(rail[ligne][col])
            col += 1
        
        if dir_bas:
            ligne += 1
        else:
            ligne -= 1
    
    return ''.join(resultat)

# Interface avec Streamlit
st.title("Chiffrement Rail Fence")

# Entrée utilisateur
message = st.text_input("Entrez le message ou le texte chiffré :", "")
k = st.number_input("Entrez la clé (k) :", min_value=1, step=1, format="%d")

# Boutons d'action
action = st.radio("Action :", ["Chiffrer", "Déchiffrer"])

if st.button("Exécuter"):
    if action == "Chiffrer":
        if message and k > 0:
            texte_chiffre = chiffrement_rail_fence(message, k)
            st.subheader("Texte chiffré :")
            st.text(texte_chiffre)
        else:
            st.error("Veuillez entrer un message valide et une clé positive.")
    elif action == "Déchiffrer":
        if message and k > 0:
            texte_dechiffre = dechiffrement_rail_fence(message, k)
            st.subheader("Texte déchiffré :")
            st.text(texte_dechiffre)
        else:
            st.error("Veuillez entrer un texte chiffré valide et une clé positive.")
