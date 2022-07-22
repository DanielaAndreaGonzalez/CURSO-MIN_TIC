def encriptador(mensaje):
    # ACÁ INICIA LA FUNCIÓN ENCRIPTADOR
    # (En este espacio debes poner el código necesario para encriptar)
    caracteresUnicos = {} 
    encriptado = ""  #el mensaje encriptado
    clave= {}
    conjunto= set(mensaje)
    listaMensaje = list(mensaje)

    clave = dict(zip(conjunto,alfabeto))

    for letra in mensaje:
        encriptado += clave[letra] 
    
    
    # ACÁ TERMINA LA FUNCIÓN ENCRIPTADOR
    # NO MODIFIQUES LA SIGUIENTE LÍNEA
    return encriptado, clave

    
def desencriptador(encriptado, clave):
    # ACÁ INICIA LA FUNCIÓN DESENCRIPTADOR 
    # (En este espacio debes poner el código necesario para desencriptar)
    
    desencriptado = ""
    diccionarioNuevo = {}
   
    
    diccionarioNuevo = dict(zip(clave.values(),clave.keys()))
    print(diccionarioNuevo)
    for letras in encriptado:
       desencriptado += diccionarioNuevo[letras]
    
    # ACÁ TERMINA LA FUNCIÓN DESENCRIPTADOR
    # NO MODIFIQUES LA SIGUIENTE LÍNEA
    return desencriptado