from geopy.geocoders import GoogleV3, Nominatim, Bing, Here
import geopy.geocoders

class lat_long:
    """ Desenvolvido por Rodolfo Bortolozo - 31/01/2022
        Retorna a Latitude Longitude e Altitude de um endereço"""
   
    def __init__(self, API_KEY = '', DOMAIN = '', LANGUAGE = 'pt-BR', APP_ID = ''):
        
        self.API_KEY = API_KEY
        self.DOMAIN = DOMAIN
        self.LANGUAGE = LANGUAGE
        self.APP_ID = APP_ID
          
    def retornar_latlong(self, local, mecanismo_busca):
        """Utiliza API do para retornar a Localização
           Retonrna uma tupla com os dados senão retornar retorna (0,0,0) 
           """
        if mecanismo_busca == 'GOOGLEV3':
            geolocator = GoogleV3(api_key = self.API_KEY, domain= self.DOMAIN)
            
        elif mecanismo_busca =='NOMINATIM':
            geolocator = Nominatim(user_agent = "Localização")
            geopy.geocoders.options.default_timeout = 7
            
        elif mecanismo_busca =='BING':
            geolocator = Bing(api_key = self.API_KEY)
               
        elif mecanismo_busca =='HERE':
            geolocator = Here(apikey = self.API_KEY, app_id=self.APP_ID)
                 
        try:
            
            loc = geolocator.geocode(local, language= self.LANGUAGE)
            
            local_lat, local_long, local_alt = loc.latitude, loc.longitude, loc.altitude
            
            return(local_lat, local_long, local_alt)
        
        except:
            return(0,0,0)
    
    def ret_lat_ou_long(self, local, ret):

        geolocator = GoogleV3(api_key = self.API_KEY, domain= self.DOMAIN)
        
        loc = geolocator.geocode(local, language= self.LANGUAGE)

        if(ret=="lat"):
            return loc.latitude
        elif(ret=="long"):
            return loc.longitude
        else:
            return 0