import retorna_latlong as geolocalizacao
import retorna_distancia as distancia


if __name__ == '__main__':
    distancia = distancia.lat_long_distancia()
    
    localizacao = geolocalizacao.lat_long(API_KEY = '',
                                           DOMAIN = 'maps.googleapis.com')
    
    localizacao_bing = geolocalizacao.lat_long(API_KEY = '',
                                           DOMAIN = '')
    
    localizacao_here = geolocalizacao.lat_long(API_KEY = '',
                                           DOMAIN = '',
                                           APP_ID='')
    
    sair = True
    enderecos = []
    latlong_google = []
    latlong_osrm = []
    latlong_bing = []
    latlong_here = []
    
    """while sair:
        enderecos.append(input("Insira um endereço ou o nome da empresa que deseja: "))
        sai = input('Deseja Sair S/N: ')
        if sai in ('Ss'):
            break"""
    enderecos.append('Rua Rio de Janeiro, 234, Centro, Fernandópolis, Brasil')        
    enderecos.append('Rua Joaquim Antonio, 1825, Centro, Meridiano, Brasil')     
    enderecos.append('Penanbucanas, Fernandópolis')
    enderecos.append('Fernandópolis, São Paulo')
    enderecos.append('São Paulo, São Paulo')
    #print (enderecos)
    
    for i in range(0,len(enderecos)):
        latlong_google.append(localizacao.retornar_latlong(enderecos[i],'GOOGLEV3'))
        latlong_osrm.append(localizacao.retornar_latlong(enderecos[i],'NOMINATIM'))
        latlong_bing.append(localizacao_bing.retornar_latlong(enderecos[i],'BING'))
        latlong_here.append(localizacao_bing.retornar_latlong(enderecos[i],'HERE'))
        
    for x in range(0,len(latlong_google)):
            print('GOOGLE: ',enderecos[x],latlong_google[x])
            print('OSRM: ', enderecos[x], latlong_osrm[x])
            print('BING: ', enderecos[x],latlong_bing[x])
            print('HERE: ',enderecos[x],latlong_here[x])
            print('**'*20)

    distancia_total = distancia.calcular_distancia(latlong_google)
    distancia_total2 = distancia.calcular_distancia(latlong_osrm)
    distancia_total3 = distancia.calcular_distancia(latlong_bing)
    distancia_total4 = distancia.calcular_distancia(latlong_here)
    
    print ("GOOGLE - Distância em Plano Cartesiano: {:.2f} Km".format(distancia_total))
    print ("OSRM - Distância em Plano Cartesiano: {:.2f} Km".format(distancia_total2))
    print ("BING - Distância em Plano Cartesiano: {:.2f} Km".format(distancia_total3))
    print ("HERE - Distância em Plano Cartesiano: {:.2f} Km".format(distancia_total4))