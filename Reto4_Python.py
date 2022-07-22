def es_semestre_valido(p, s):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    es_semestre=False
    if s<=0:
        es_semestre=False
    elif(len(p)>0 and s<=len(p)) :
        es_semestre=True
    else:
        es_semestre=False
    return es_semestre

def es_semestre_vacio(p, s):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    es_vacio=True
    if p[s-1]:
        es_vacio=False
    return es_vacio

def es_materia_valida(p, s, m):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    mimateria = p[s-1]
    if (mimateria.get(m) != None):
        materia_valida = True
    else:
        materia_valida = False
    return materia_valida

def modificar_materia(pensum, semestre, materia, nombre, creditos):
    # ACÁ INICIA LA FUNCIÓN
    if es_semestre_valido(pensum, semestre):
        if es_semestre_vacio(pensum,semestre):
            if es_materia_valida(pensum,semestre,materia):
                mimateria = pensum[semestre-1]
                datosMateria = mimateria.get(materia)
                datosMateria.update({'nombre':nombre, 'créditos':creditos})
    
    
    
    # ACÁ TERMINA LA FUNCIÓN
    # ESTA VEZ TU DEFINES TUS RETORNOS

def eliminar_materia(pensum, semestre, materia):
    # ACÁ INICIA LA FUNCIÓN
    if es_semestre_valido(pensum, semestre):
        if es_semestre_vacio(pensum,semestre):
            if es_materia_valida(pensum,semestre,materia):
                mimateria = pensum[semestre-1]
                mimateria.pop(materia)
                print(pensum)
    # ACÁ TERMINA LA FUNCIÓN
    # ESTA VEZ TU DEFINES TUS RETORNOS