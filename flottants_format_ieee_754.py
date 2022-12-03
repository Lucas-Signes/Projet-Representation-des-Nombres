#flottants_format_ieee_754

from entiers import * #on importe les instructions du module pour pouvoir les réutiliser
from non_entiers import *

bit = 3

#INSTRUCTION 28:
    
def forme_normalisee (dec, b = bit): 
    """

    Parameters
    ----------
    dec : int
        Nombre décimale quelconque.
    
    b : int
        Nombre de bit 

    Returns
    -------
    nuplet: triplet (s,e,m) => caractéristiques de la forme binaire normalisée.
    "entier" : 1,0,1
    "virgule" : 0,1
    """
    if dec < 0: #signe + ou - en fonction de si n est supèrieur ou infèrieur a 0
        s = 1
    else:
        s = 0
    
    partie_entiere = int(dec)
    partie_virgule = dec - partie_entiere
   
    dec = fractionnaire_dec_vers_bin({"entier": partie_entiere , "virgule": partie_virgule}, b)
    e = len(dec["entier"])-1
    
    m = []
    for i in range( 1, len(dec["entier"])):
        m.append(dec["entier"][i])
    
    for i in range(len(dec["virgule"])):
        m.append(dec["virgule"][i])
        
    return (s,e,m)


#INSTRUCTION 29:
    
def exposant (dec):
    """

    Parameters
    ----------
    dec : int
        Nombre décimale quelconque.

    Returns
    -------
    list: liste des bits de son exposant dans sa représentation IEEE.

    """  
    e = forme_normalisee(dec, 10)
    e = dec_vers_bin(e[1] + 127) #+127 car on code en exedant 127
    e.reverse()
    while len(e) < 8: #le champs de l'exposant est 8 bits 
        e.append(0)
    e. reverse()

    return e 


#INSTRUCTION 30:
    
def mantisse (dec):
    """

    Parameters
    ----------
    dec : int
        Nombre décimale quelconque.

    Returns
    -------
    list: liste des bits de sa mantisse dans sa représentation IEEE.

    """
    m = forme_normalisee(dec, 23)
    m2 = m[2]

    while len(m2) > 23: #le champs de la mantisse est de 23 bits 
        del m2[-1]

    return m2
   

#INSTRUCTION 31:

def dec_vers_ieee (dec): 
    """

    Parameters
    ----------
    dec : int
        Nombre décimale quelconque.

    Returns
    -------
    representation de dec en format ieee.

    """
    if dec < 0:
        s = 1
    else:
        s = 0
    
    e = exposant(dec)
    m = mantisse(dec)
    
    return(s,e,m)


#INSTRUCTION 32:

def ieee_vers_dec (n_ieee): 
    """

    Parameters
    ----------
    n_ieee:
        nombre format IEEE.

    Returns
    -------
    float: nombre flottant en format décimale.

    """
    signe = n_ieee[0]
    exposant = bin_vers_dec(n_ieee[1])-127
    mantisse = (n_ieee[2])
    
    
    res = ((-1)**signe) * (fractionnaire_bin_vers_dec({"entier": [1] , "virgule": mantisse})) * (2**exposant)
    return res 


#INSTRUCTION 33:
    
def afficher_ieee (n_ieee):
    """

    Parameters
    ----------
    n_ieee : list
        Represetation en IEEE d'un nombre décimale.

    Returns
    -------
    None.

    """  
    print(n_ieee[0],"|",end="" )
    for i in range(len(n_ieee[1])):
        print(n_ieee[1][i],end="")
    print("|",end="")
    for i in range(len(n_ieee[2])):
        print(n_ieee[2][i],end="")
    print("|")
    

#INSTRUCTION 34:

def jeu_de_tests ():    
    """
    La fonction test les fonctions dec_vers_ieee et ieee_vers_dec avec deux assertions positives
    
    Returns
    -------
    Deux assertions positives par fonction

    """    
    assert dec_vers_ieee(3) == (0, [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    assert dec_vers_ieee(6) == (0, [1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) 
    
    assert ieee_vers_dec((0, [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 3.0
    assert ieee_vers_dec((0, [1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 6.0
    
jeu_de_tests()

 