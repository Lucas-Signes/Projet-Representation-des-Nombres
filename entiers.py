#entier.py

espace = 4

#INSTRUCTION 0:
    
def afficher_binaire (liste_bin, esp = espace):
    """
    
    Parameters
    ----------
    liste_bin : list
       Liste binaire.
    esp : int
        espace tout les 4 bits.

    Returns
    -------
    c'est une procedure pas de return.

    """
    result = ""
    cpt = 1
    liste_bin = liste_bin[::-1] #reverse la liste 
    for i in liste_bin:
       result += str(i)
       if cpt % esp == 0 and cpt != len(liste_bin):
           result += " "
       cpt += 1
    print (result[::-1]) #on re-revers pour l'avoir dans le bon sens 
    

#INSTRUCTION 1:

def bin_vers_dec (liste_bin): 
    """

    Parameters
    ----------
    liste_bin : list
        liste de bits.

    Returns
    -------
    nombre decimal (int).
    
    """
    puissance = len(liste_bin)-1 
    result = 0
    for i in range(len(liste_bin)):
        result = result + (2**puissance)*liste_bin[i] 
        puissance = puissance - 1
    return result
   
    
#INSTRUCTION 2:  
    
def dec_vers_bin (dec): 
    """

    Parameters
    ----------
    dec : int
        nombre base 10.

    Returns
    -------
    liste de binaire.

    """
    liste_bits = []
    while (dec // 2) != 0:
        liste_bits.append(dec % 2)
        dec = dec // 2
    liste_bits.append(dec % 2) #car si reste=0 la boucle s'arrête il faut rajouter le dernier reste
    liste_bits.reverse() 
    return liste_bits


#INSTRUCTION 3:  
    
def oct_vers_dec (liste_octal):
    """

    Parameters
    ----------
    liste_octal : liste
        liste de chiffres octal.

    Returns
    -------
    entier naturel decimale.

    """
    puissance = len(liste_octal)-1 
    result = 0
    for i in range(len(liste_octal)):
        result = result + (8**puissance)*liste_octal[i]
        puissance = puissance - 1
    return result


#INSTRUCTION 4:
    
def dec_vers_oct (dec):    
    
    """

    Parameters
    ----------
    dec : int
        entier naturel base 10.

    Returns
    -------
    liste octal.

    """
    
    liste_oct = []
    while dec//8 != 0:
        liste_oct.append(dec % 8)
        dec = dec // 8
    liste_oct.append(dec % 8) #car si reste=0 la boucle s'arrête il faut rajouter le dernier reste
    liste_oct.reverse() 
    return liste_oct


#INSTRUCTION 5:

def hex_vers_dec(liste_hexa):
   """

    Parameters
    ----------
    liste_hexa : list
        liste de chiffres hexadecimals.

    Returns
    -------
    entier naturel decimal.

    """
    
   hexa_lettres = {"A":10 , "B":11 , "C":12 , "D":13 , "E":14 , "F":15} #dictionnaire où chaque valeur au dessus de 10 est assigné à sa clé en lettre.
    
   puissance = len(liste_hexa)-1 
   result = 0
   for i in range(len(liste_hexa)):
        if type(liste_hexa[i]) == int:
            result = result + (16**puissance)*liste_hexa[i]
            puissance = puissance - 1
        else:
            result = result + (16**puissance)*(hexa_lettres[liste_hexa[i]])
            puissance = puissance - 1
   return result
 

#INSTRUCTION 6:

def dec_vers_hex(dec):

    """
    
    Parameters
    ----------
    dec : int
        entier naturel decimal.

    Returns
    -------
    liste de hexadecimale.

    """

    hexa_lettres = {10:"A" , 11:"B" , 12:"C" , 13:"D" , 14:"E" , 15:"F"} #dictionnaire où chaque lettre ayant une valeur au dessus de 10 est assigné à sa clé en chiffre.
    if 10<=dec<=15:
        return hexa_lettres[dec] #car ces valeurs correpondent directement au lettres assignées dans le dictionnaire
    
    liste_hex = []
    while dec//16 != 0:
        liste_hex.append(dec % 16) 
        dec = dec // 16
        if liste_hex[-1] > 9:
            liste_hex[-1] = hexa_lettres[liste_hex[-1]]
            
    liste_hex.append(dec % 16) #car si reste=0 la boucle s'arrête il faut rajouter le dernier reste
    liste_hex.reverse() 
    return liste_hex
    

#INSTRUCTION 7:
    
def bin_vers_hex(liste_bin):
    """

    Parameters
    ----------
    liste_bits : list
        liste de bits.

    Returns
    -------
    liste de hexadecimale.

    """
    nb_dec = bin_vers_dec(liste_bin) #on réutilise les fonctions pour passé d'un binaire donné en entrée a un héxadécimal en sortie en passant par un décimal
    nb_hexa = dec_vers_hex(nb_dec)
    return nb_hexa
        

#INSTRUCTION 8:

def hex_vers_bin(liste_hexa):
    """

    Parameters
    ----------
    liste_hexa : list
        Liste de chiffres hexadécimaux d'un entier naturel.

    Returns
    -------
    Liste des bits de sa representation binaire.

    """
    nb_dec = hex_vers_dec(liste_hexa) #même principe que la fonction précédente mais "à l'envers"
    nb_bin = dec_vers_bin (nb_dec)
    return nb_bin
    

#INSTRUCTION 9:
    
def bin_vers_chaine(liste_bin): 
    """

    Parameters
    ----------
    liste_bin : list
        Liste des bits d'un entier naturel.

    Returns
    -------
    Representation binaire sous forme de chaine de charactère (str). 

    """
    result = ""
    liste_bin = liste_bin[::-1] #on revers la liste 
    for i in liste_bin:
       result += str(i)
    return result[::-1] #on re-reverse la liste pour l'avoir dans le bon sens 

   
#INSTRUCTION 10:

def bin_vers_entier(liste_bin):
    """

    Parameters
    ----------
    liste_bin : list
        Liste des bits de la representation binaire d'un entier naturel.

    Returns
    -------
    int (un entier).

    """    
    res = 0
    liste_bin.reverse()
    for i in range(len(liste_bin)):
        res = res + 10**i*liste_bin[i]  
    liste_bin.reverse()
    return res


#INSTRUCTION 11:
    
def hexa_vers_chaine(liste_hexa): 
    """

    Parameters
    ----------
    liste_hexa : list
        Prend une liste en hexadécimal.

    Returns
    -------
    Sa repréentation en chaine de charactère (str).

    """
    result = ""
    liste_hexa = liste_hexa[::-1]
    for i in liste_hexa:
       result += str(i)
    return result[::-1]


#INSTRUCTION 12:

def addition_binaire(liste_bit1 ,liste_bit2):
    """

    Parameters
    ----------
    liste_bit1 : list
        liste des bit de la représentation binaire d'un nombre de l'addition.
    liste_bit2 : list
        liste des bit de la représentation binaire d'un nombre de l'addition.
    
    Returns
    -------
    liste 3 => liste des bit de la représentation binaire du résultat.

    """
    liste_bit1.reverse()
    liste_bit2.reverse()
    liste_bit3 = [] #liste du résultat
    retenue = 0
    if len(liste_bit1) > len(liste_bit2): #on regarde quelle liste est la plus longue
        long_liste = len(liste_bit1)
    else:
        long_liste = len(liste_bit2)
    
    for i in range(long_liste):
        if i < len(liste_bit1) and i < len(liste_bit2): #on verifie si i est < à la longeur des listes
        
          if liste_bit1[i] == 0 or liste_bit2[i] == 0:
             liste_bit3.append(liste_bit1[i] + liste_bit2[i]) #si on additionne 2 0
             if liste_bit3[i] != 0 and retenue == 1:
                 liste_bit3[i] = 0
             elif retenue == 1 and liste_bit3[i] == 0:   #si le resultat = 0 mais qu'il y a une retenue le résultat est 1
                liste_bit3[i] = 1
                retenue = 0
                
          elif liste_bit1[i] == 1 and liste_bit2[i] == 1: #cas où on additionne 2 1
            if retenue == 1:
                liste_bit3.append(1)
            else:
                liste_bit3.append(0)
                retenue = 1
        
        else:
            if len(liste_bit1) > i:   #si la taille est supèrieur a i 
                if liste_bit1[i] == 1: 
                    if retenue == 1:
                        liste_bit3.append(0) #si il y a une retenue alors 0 
                    else:
                        liste_bit3.append(1) #sinon 1
                    
                else:
                    if retenue == 1:
                        liste_bit3.append(1) #si il y a une retenue le resultat est 1 et il n'y a plus de retenue
                        retenue = 0
                    else:
                        liste_bit3.append(0)
    
            if len(liste_bit2) > i: #pareil avec le cas de liste 2 est plus gande
                if liste_bit2[i] == 1:
                    if retenue == 1:
                        liste_bit3.append(0)
                    else:
                        liste_bit3.append(1)
                    
                else:
                    if retenue == 1:
                        liste_bit3.append(1)
                        retenue = 0
                    else:
                        liste_bit3.append(0)
    if retenue == 1:
        liste_bit3.append(1)
    
    liste_bit1.reverse() #on re-retourne les listes 
    liste_bit2.reverse()
    liste_bit3.reverse()
    
    return liste_bit3 #on return le résultat 
    

#INSTRUCTION 13:

def jeu_de_tests():
    """
    La fonction test toutes les fonctions de representation de nombres entiers avec une assertion positive et negative

    Returns
    -------
    Une assertion positive et negative par fonction

    """
    assert bin_vers_dec([1,0,0]) == 4
    assert bin_vers_dec([1,0,0]) != 5 
    
    assert dec_vers_bin(4) == [1,0,0]
    assert dec_vers_bin(4) != [0,0,0]
    
    assert oct_vers_dec([1,0]) == 8
    assert oct_vers_dec([1,0]) != 9
    
    assert dec_vers_oct(8) == [1,0]
    assert dec_vers_oct(8) != [0,0]
    
    assert hex_vers_dec([1,0]) == 16
    assert hex_vers_dec([1,0]) != 17
    
    assert dec_vers_hex(16) == [1,0]
    assert dec_vers_hex(16) != [0,0]
    
    assert bin_vers_hex([1,0,0,0,0]) == [1,0]
    assert bin_vers_hex([1,0,0,0,0]) != [0,0] 
    
    assert hex_vers_bin([1,0]) == [1,0,0,0,0]
    assert hex_vers_bin([1,0]) != [0,0,0,0,0]
    
    assert bin_vers_chaine([1,0,1,0]) == "1010"
    assert bin_vers_chaine([1,0,1,0]) != "0010"
    
    assert bin_vers_entier([1,0,1,0]) == 1010
    assert bin_vers_entier([1,0,1,0]) != 1000
    
    assert hexa_vers_chaine([1,0,1,0]) == "1010" 
    assert hexa_vers_chaine([1,0,1,0]) != "0010" 
    
    assert addition_binaire([1,0,1] ,[1,0,0]) == [1, 0, 0, 1]
    assert addition_binaire([1,0,1] ,[1,0,0]) != [0, 0, 0, 1]
    
jeu_de_tests()


    
    