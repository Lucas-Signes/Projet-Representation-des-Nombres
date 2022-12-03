#non entiers

from entiers import * #on importe les instructions du module pour pouvoir les réutiliser

bit = 8

#INSTRUCTION 17:
    
def est_representable_bin(n, b = bit):
    """

    Parameters
    ----------
    n : int
        Prend un entiers natuel en décimale.
    b : int
        Un nombre de bit.

    Returns
    -------
    bool
        True si representable sur b bit et False le cas contraire.

    """
    n = dec_vers_bin(n)
    return b >= len(n)


#INSTRUCTION 18:
    
def est_representable_signe(n, b = bit):
    """

    Parameters
    ----------
    n : int
        Entier relatif en décimale et.
    b : int
        Un nombre de bit.

    Returns
    -------
    bool
        True si representable en binaire signé sur b bits et False le cas contraire .

    """
    n = dec_vers_bin(n)
    return b >= len(n) + 1


#INSTRUCTION 19:
    
def est_representable_comp2(n, b = bit):
    """

    Parameters
    ----------
    n : int
        Entiers relatif en décimal.
    b : int
        Un nombre de bit.

    Returns
    -------
    bool
        True si representable en complement à 2 sur b bits et False le cas contraire.

    """
    n = dec_vers_bin(n)
    for i in range(len(n)):
        if n[i] == 0:
            n[i] = 1
        else:
            n[i] = 0
    n = addition_binaire(n, [1])
    return b >= len(n)


#INSTRUCTION 20:
    
def addition_binaire_machine(liste_bit1, liste_bit2, b = bit):
    """

    Parameters
    ----------
    liste_bit1 : list
        Liste n°1 des bits de la represenation biniare d'un nombre.
    liste_bit2 : list
        Liste n°2 des bits de la represenation biniare d'un nombre.
    b : int
        nombre de bits.

    Returns
    -------
    dict
        Résultat de l'addition et le bit de la dernière retenue.

    """
    liste_bit3 = addition_binaire(liste_bit1, liste_bit2)
    liste_bit3.reverse()
    if b > len(liste_bit3):
        bit_derniere_retenue = liste_bit3[-1]
        
    else:
        bit_derniere_retenue = liste_bit3[b]
    liste_bit3 = liste_bit3[:b]
    liste_bit3.reverse()
    
    return {"addition": liste_bit3, "bit retenue": bit_derniere_retenue}


#INSTRUCTION 21:
    
def dec_vers_bin_machine(n, b = bit):
    """

    Parameters
    ----------
    n : int
        Entier decimale.
    b : int
        Nombre de bits.

    Returns
    -------
    n : list 
        Liste correspondant a la représentation binaire de n sur b bit.

    """
    n = dec_vers_bin(n)
    n.reverse()
    n = n[:b] #on reprend la liste de 0 à b
    while len(n) < b: 
        n.append(0) #comme ça on rajoute pour compléter sur plus de bits que necessaire
    n.reverse()
    return n


#INSTRUCTION 22:
    
def bin_vers_dec_machine(liste_bit, b = bit): 
    """

    Parameters
    ----------
    liste_bit : list
        liste de bit d'un entier naturel.
    b : int
        nombre de bit.

    Returns
    -------
    int
        Representation de la liste en décimale.

    """
    liste_bit.reverse()
    liste_bit = liste_bit[:b]
    liste_bit.reverse()
    return bin_vers_dec(liste_bit)


#INSTRUCTION 23:
    
def dec_vers_bin_signe(dec, b = bit):
    """

    Parameters
    ----------
    dec : int
        Entier en décimale.
    b : int
        Un nombre de bit.

    Returns
    -------
    list
        Liste correspondant à la représentation de n en bin.

    """
    L = dec_vers_bin(abs(dec)) #abs pour valeur absolue 
    L.reverse()
    L = L[:b - 1] #on reprend la liste de 0 à b-1
    L.reverse()
    if dec < 0:
        return [1] + L
    else:
        return [0] + L


#INSTRUCTION 24:
    
def bin_signe_vers_dec(Liste_bit):
    """

    Parameters
    ----------
    Liste_bit : list
        liste des bits de la represenation binaire signé d'un entier relatif.

    Returns
    -------
    int
        représentation en décimale.

    """
    signe = Liste_bit[0]
    Liste_nombre = Liste_bit[1:]

    if signe == 1:
        signe = -1
    else:
        signe = 1

    return bin_vers_dec(Liste_nombre) * signe


#INSTRUCTION 25:
    
def dec_vers_compl2(dec, b = bit):
    """

    Parameters
    ----------
    dec : int
        Entier en décimale.
    b : int
        Nombre de bit.

    Returns
    -------
    list
        Representation sur b bit de dec.

    """
    dec = dec_vers_bin_machine(dec, b = bit)

    for i in range(len(dec)):
        if dec[i] == 0:
            dec[i] = 1
        else:
            dec[i] = 0
    dec = addition_binaire(dec, [1])
    dec.reverse()
    dec = dec[:b] 
    dec.reverse()
    return dec


#INSTRUCTION 26:
    
def compl2_vers_dec(Liste_bit):
    """

    Parameters
    ----------
    Liste_bit : list
        Liste des bits de la representation en complément à 2 d'un entier relatif.

    Returns
    -------
    list
        representation en décimale.

    """
    signe = Liste_bit[0]
    Liste_nombre = Liste_bit[1:]
    if signe == 1:
        signe = -1
    else:
        signe = 1

    for i in range(len(Liste_nombre)): #on effectue un parcours de liste de la taille de Liste_nombre
        if Liste_nombre[i] == 0:
            Liste_nombre[i] = 1
        else:
            Liste_nombre[i] = 0

    Liste_nombre = addition_binaire(Liste_nombre, [1])

    return bin_vers_dec(Liste_nombre) * signe


#INSTRUCTION 27:

def jeu_de_tests ():
    """
    La fonction test toutes les fonctions de representation de nombres entiers en machine avec une assertion positive et negative

    Returns
    -------
    Une assertion positive et negative par fonction

    """
    assert est_representable_bin(5, 5) == True
    assert est_representable_bin(5, 5) != False
    
    assert est_representable_signe(5, 5) == True
    assert est_representable_signe(5, 5) != False
    
    assert est_representable_comp2(5, 5) == True
    assert est_representable_comp2(5, 5) != False
    
    assert addition_binaire_machine([0,1,0], [1,0,1], 5) == {'addition': [1, 1, 1], 'bit retenue': 1}
    assert addition_binaire_machine([0,1,0], [1,0,1], 5) != {'addition': [0, 1, 1], 'bit retenue': 1}
    
    assert dec_vers_bin_machine(5, 5) == [0, 0, 1, 0, 1]
    assert dec_vers_bin_machine(5, 5) != [1, 0, 1, 0, 1]
    
    assert bin_vers_dec_machine([1,0,1], 5) == 5
    assert bin_vers_dec_machine([1,0,1], 5) != 4
    
    assert dec_vers_bin_signe(5, 5) == [0, 1, 0, 1]
    assert dec_vers_bin_signe(5, 5) != [1, 1, 0, 1]
    
    assert bin_signe_vers_dec([1,0,1]) == -1
    assert bin_signe_vers_dec([1,0,1]) != 1
    
    assert dec_vers_compl2(5, 5) == [1, 1, 0, 1, 1]
    assert dec_vers_compl2(5, 5) != [0, 1, 0, 1, 1]
    
    assert compl2_vers_dec([1,0,1]) == -3
    assert compl2_vers_dec([1,0,1]) != 3
    
jeu_de_tests()




