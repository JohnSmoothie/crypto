# -*-coding: utf-8 -*-

import os
import string

# Retourne le chemin absolu du chemin passé en paramètre
def chemin_absolu(chemin):
    return os.path.abspath(chemin)

# Lit le fichier dont le chemin est spécifié
# Si le chemin est incorrect, un message d'erreur s'affiche
# Retourne le fichier lu
def lire_fichier(chemin):
    try:
        fichier = open(chemin_absolu(chemin), 'r')
    except:
        print("Chemin ou fichier incorrect !")
    return fichier

# Converti le fichier (dont le chemin est spécifié) en UTF-8
# Retourne le chemin du fichier converti
def chemin_convertir_fichier(chemin):
    commande = "iconv -f WINDOWS-1252 -t UTF-8 " + chemin_absolu(chemin) + " > " + os.path.dirname(
        os.path.abspath(chemin)) + "/" + os.path.splitext(os.path.basename(chemin))[0] + "_utf8.txt"
    os.system(commande)
    return  os.path.dirname(os.path.abspath(chemin)) + "/" + os.path.splitext(os.path.basename(chemin))[
        0] + "_utf8.txt"

# Retourne le nombre de lignes du fichier spécifié
def fichier_nombre_lignes(fichier):
    count = 0
    try:
        for _ in fichier:
            count += 1
    except:
        print()
    return count


# Retourne le nombre de lignes d'un fichier dont le chemin est spécifié
def chemin_nombre_lignes(chemin):
    fichier = lire_fichier(chemin)
    count = 0
    try:
        for _ in fichier:
            count += 1
    except:
        print()
    return count


# Transforme un texte (dont le chemin est spécifié) en un texte avec un mot par colonne
# Retourne le chemin du fichier créé
def txt_to_column(chemin):
    commande = "tr \" \" \"\\012\" <" + os.path.abspath(chemin) + "> " + os.path.dirname(
        os.path.abspath(chemin)) + "/" + os.path.splitext(os.path.basename(chemin))[0] + "_column.txt"
    os.system(commande)
    return os.path.dirname(os.path.abspath(chemin)) + "/" + os.path.splitext(os.path.basename(chemin))[
        0] + "_column.txt"


# Enlève la ponctuation du fichier spcifié
# Retourne le fichier créé
def fichier_enlever_ponctuation(fichier):
    fichier2 = open(fichier, 'w')
    for ligne in fichier:
        fichier2.write(ligne.translate(None, string.punctuation))
    return fichier2

# Enlève la ponctuation du fichier (dont le chemin est spécifié)
# Retourne le fichier créé
def chemin_enlever_ponctuation(chemin):
    fichier1 = lire_fichier(chemin)
    st1 = os.path.dirname(os.path.abspath(chemin)) + "/" + os.path.splitext(os.path.basename(chemin))[
        0] + "_ponctuation.txt"
    fichier2 = open(chemin, 'w')
    for ligne in fichier1:
        fichier2.write(ligne.translate(None, string.punctuation))
    return os.path.dirname(os.path.abspath(chemin)) + "/" + os.path.splitext(os.path.basename(chemin))[
        0] + "_ponctuation.txt"