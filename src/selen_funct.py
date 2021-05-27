def buy_rent_share():
    '''
    This function requests a value between buying, renting or sharing from the user.
    '''
    opciones = ["buy","rent","share"]
    
    brs = input("Select whether you want to buy, rent or share a property: ")
    eleccion = brs.lower()

    while eleccion not in opciones:
        print("You must choose between buy, rent or share. ")
        brs = input("Select whether you want to buy, rent or share a property: ")
        eleccion = brs.lower()

    return eleccion