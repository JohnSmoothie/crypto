# -*- coding: utf-8 -*-

# ------------------------------------------
# Le code de César
# ------------------------------------------

# Chiffrement de César pour un chiffre
def chiffrement_nombre(x, k):
    return (x + k) % 26


# Déchiffrement de César pour un chiffre
def dechiffrement_nombre(x, k):
    return (x - k) % 26


# Chiffrement de César (pour un mot ou une phrase)
def chiffrement(mot, n):
    message_code = []
    # Pour chaque lettre
    for lettre in mot:
        if lettre == " ":  # On ne touche pas aux espaces
            lettre_code = " "
        else:
            nomb = ord(lettre) - 65  # Lettre devient nombre de 0 à 25
            nomb_code = (nomb + n) % 26  # Chiffrement de César : on ajoute n
            lettre_code = chr(nomb_code + 65)  # On repasse aux lettres
        message_code.append(lettre_code)  # On ajoute la lettre codée au message

    message_code = "".join(message_code)  # On revient à une chaine de caractères
    return (message_code)


# Déchiffrement de César (pour un mot ou une phrase)
def dechiffrement(mot, n):
    return chiffrement(mot, -n)

# Attaque exhaustive
def attaque(mot):
    for n in range(26):
        print(dechiffrement(mot, n))
    return None

