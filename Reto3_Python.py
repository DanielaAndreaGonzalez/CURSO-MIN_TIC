def clima(datos):
    
    #ESCRIBA EN ESTA REGIÓN SU PROPUESTA DE SOLUCIÓN PARA HALLAR LAS
    #FECHAS DE LOS EVENTOS DEL TIEMPO MENCIONADOS EN EL ENUNCIADO.
    #ATÉNGASE AL USO DE LOS RETORNOS PUESTOS AL FINAL DE ESTA FUNCIÓN
    
    n=7
    listaModificada=[datos[i:i + n] for i in range(0, len(datos), n)]
    array_np = np.array(listaModificada, dtype='object')
    filas = len(array_np)
    datos_matriz = array_np.reshape(filas,7)
    datos_sin_fecha =np.delete(datos_matriz,0,axis=1)  
    
    #minimo = datos_sin_fecha.min()#de toda la matriz
    minimo = datos_sin_fecha.min(axis=0)
    maximos = datos_sin_fecha.max(axis=0)
    
    promedio = datos_sin_fecha.mean(axis=0)#promedio
    
    fechas_temp_min = []
    fechas_temp_max = []
    fechas_precip_min = []
    fechas_precip_max = []
    fechas_max_dias_sol=[]
    
    for i in range(filas):
        if datos_matriz[i][1] == minimo[0]:
            fechas_temp_min.append(datos_matriz[i][0])
            
        if datos_matriz[i][2] == maximos[1]:
            fechas_temp_max.append(datos_matriz[i][0])
            
        if datos_matriz[i][3] == minimo[2]:
            fechas_precip_min.append(datos_matriz[i][0])
            
        if datos_matriz[i][3] == maximos[2]:
            fechas_precip_max.append(datos_matriz[i][0])
        
        if datos_matriz[i][6] == maximos[5]:
            fechas_max_dias_sol.append(datos_matriz[i][0])
        
    return fechas_temp_min, fechas_temp_max, fechas_precip_min, fechas_precip_max, fechas_max_dias_sol