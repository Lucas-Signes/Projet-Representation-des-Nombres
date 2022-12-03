#entiers_en_machine.py

from entiers import * #on importe les instructions du module pour pouvoir les réutiliser

precision = 3

#INSTRUCTION 14:

def fractionnaire_dec_vers_bin(fractionnaire_dec, p = precision):
    """

    Parameters
    ----------
    fractionnaire_dec : int
        Partie entière.
    p : int
        Partie fractionnaire.

    Returns
    -------
    dict
        Representation binaire du nombre fractionnaire.

    """
    P_dec = fractionnaire_dec["virgule"]

    P_dec_copy = 0 #on ajoute cette variable pour vérifier que c'est codable
    List_P_dec = []

    P_entiere = dec_vers_bin(fractionnaire_dec["entier"])

    for i in range(1,p+1):
        if P_dec_copy + (2**-i) <= P_dec:

            P_dec_copy += (2**-i)
            List_P_dec.append(1)
        else:
            List_P_dec.append(0)
    
    return {"entier" : P_entiere , "virgule" : List_P_dec}


#INSTRUCTION 15:

def fractionnaire_bin_vers_dec(fractionnaire_bit):
    """

    Parameters
    ----------
    fractionnaire_bit : list
        liste en binaire d'un nombre fractionnaire.
    

    Returns
    -------
    dict
        Représentation en décimale de la représentation binaire d'un nombre fractionnaire.

    """
    P_entiere = fractionnaire_bit["entier"]
    P_dec = fractionnaire_bit["virgule"]

    P_dec_copy = 0

    P_entiere = bin_vers_dec(P_entiere)

    for i in range(len(P_dec)):
        P_dec_copy += (2**-(i+1))*P_dec[i]

    return P_entiere + P_dec_copy


#INSTRUCTION 16:

def jeu_de_tests ():
    """
    La fonction test toutes les fonctions de representation de nombres non entiers avec une assertion positive et negative

    Returns
    -------
    Une assertion positive et negative par fonction

    """
    assert fractionnaire_dec_vers_bin({"entier" : 10, "virgule" : 0.25}, 5) == {"entier": [1, 0, 1, 0], "virgule": [0, 1, 0, 0, 0]}
    assert fractionnaire_dec_vers_bin({"entier" : 10, "virgule" : 0.25}, 5) != {"entier": [0, 0, 1, 0], "virgule": [0, 1, 0, 0, 0]}
    
    assert fractionnaire_bin_vers_dec({"entier" : [1, 1, 0] , "virgule" : [0, 1]}) == 6.25
    assert fractionnaire_bin_vers_dec({"entier" : [1, 1, 0] , "virgule" : [0, 1]}) != 6.20
    
jeu_de_tests()







