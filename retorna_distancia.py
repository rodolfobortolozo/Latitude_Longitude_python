from geopy import distance
from geopy import Nominatim

class lat_long_distancia:
    """ Desenvolvido por Rodolfo Bortolozo - 31/01/2022
        Clacula Distancia Endereço"""
      
    def calcular_distancia(self,local_lista):
        totalKm = 0
        listaInicio =0
        listaProximo = 1
        totalLista = len(local_lista)
        total = True
        
        while total:
            totalKm += distance.distance(local_lista[listaInicio],local_lista[listaProximo]).km
            listaInicio +=1
            listaProximo +=1
            if(listaProximo == totalLista):
                break
        return totalKm