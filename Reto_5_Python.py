def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    with open("GLOBANT.csv", "r") as archivo:
      contenido = csv.reader(archivo)
      encabezado = next(contenido)
      fecha = []
      comportamientoAccion = []
      puntoMedio = []

      linea = []
      informe_1 = []
      dicc = {}
      listaContenido = []
      catidadSube = 0
      cantidadBaja = 0
      cantidadEstable = 0
      lista_json = []

      dic_fecha_valor = {}
      dic_fecha_valor2 = {}
      for fila in contenido:
        linea = []
        linea.append(fila[0])
        if (float(fila[4]) -float(fila[1])) > 0:
          linea.append("SUBE")
          catidadSube +=1
        elif (float(fila[4]) -float(fila[1])) < 0:
          linea.append("BAJA")
          cantidadBaja+=1
        elif (float(fila[4]) -float(fila[1])) == 0:
          linea.append("ESTABLE")          
        linea.append((float(fila[2]) - float(fila[3])) / 2)
        informe_1.append(linea)
        listaContenido.append(fila)        
        dic_fecha_valor[fila[0]] = fila[3]
        dic_fecha_valor2[fila[0]] = fila[2]

      
      dicc["date_lowest_price"] = min(dic_fecha_valor, key=dic_fecha_valor.get)
      #dicc["lowest_price"] = float(min(listaContenido[4]))
      dicc["lowest_price"] = float(dic_fecha_valor[dicc["date_lowest_price"]])
      dicc["date_highest_price"] = max(dic_fecha_valor2, key=dic_fecha_valor2.get)
      #dicc["highest_price"] = float(max(listaContenido[5]))
      dicc["highest_price"] = float(dic_fecha_valor2[dicc["date_highest_price"]])
      dicc["cantidad_veces_sube"] = int(catidadSube)
      dicc["cantidad_veces_baja"] = int(cantidadBaja)
      dicc["cantidad_veces_estable"] = int(cantidadEstable)
      #lista_json.append(dicc)      
      


    with open("analisis_archivo.csv", "w") as informe:
      escribir = csv.writer(informe, delimiter="\t")
      escribir.writerow(["Fecha", "Comportamiento de la accion" ,"Punto medio HIGH-LOW"])
      escribir.writerows(informe_1)
    datosJson = json.dumps(dicc,indent=4)
    with open("detalles.json","w") as jsonFile:
      jsonFile.write(datosJson)
    