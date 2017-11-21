# -*- coding: utf-8 -*-


# Chiffrement de Vigenère (pour un mot ou une phrase)
# cle est la liste [n_1,n_2,...,n_k]
def vigenere(mot, cle):
    message_code = []
    k = len(cle)  # longueur de la clé
    i = 0  # rang dans le bloc
    # Pour chaque lettre
    for lettre in mot:
        if lettre == " ":  # On ne touche pas aux espaces
            lettre_code = " "
        else:
            nomb = ord(lettre) - 65  # Lettre devient nombre de 0 à 25
            nomb_code = (nomb + cle[i]) % 26  # Chiffrement de Vigenère : on ajoute n_i
            lettre_code = chr(nomb_code + 65)  # On repasse aux lettres
            i = (i + 1) % k  # On passe au rang suivant
        message_code.append(lettre_code)  # On ajoute la lettre codée au message
    message_code = "".join(message_code)  # On revient à une chaine de caractère
    return (message_code)


# Déchiffrement de Vigenère (pour un mot ou une phrase)
def decode_vigenere(mot, cle):
    return vigenere(mot, [-n for n in cle])

# Statistiques (pour un mot ou une phrase)
def statistiques(phrase):
    liste_stat = [0 for x in range(26)]  # On part d'une liste avec des 0
    for lettre in phrase:  # On parcourt la phrase
        i = ord(lettre) - 65
        if 0 <= i < 26:  # Si c'est une vraie lettre
            liste_stat[i] = liste_stat[i] + 1
    return (liste_stat)


# Tri des statistiques
def tri_statistiques(liste):
    pastri = []  # Liste avec lettre en face
    for i in range(26):
        pastri.append((chr(65 + i), liste[i]))
    tri = sorted(pastri, key=lambda freq: freq[1], reverse=True)
    return (tri)