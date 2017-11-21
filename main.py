# -*-coding: utf-8 -*-

import gestion_fichier
import vigenere
import cesar
import os

chemin = "data/test.txt"
fichier = gestion_fichier.chemin_convertir_fichier(chemin)
gestion_fichier.chemin_enlever_ponctuation(fichier)
