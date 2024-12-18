from rest_base import RestBase

class AppCtrl(RestBase):
    
    def __init__(self, url= 'http://127.0.0.1:8080'):
        self.url = url

    def image_upload(self, url=None, params = None, data= None, files = None,  status_code=201):
        if url is None:
            url = f'{self.url}/upload' 
        
        return self._execute_request(method='post', url=url, params=params, data=data, files=files, status_code=status_code)
    
    def image_get(self, filename, url=None, params=None, status_code=200):
        if url is None:
            url = f'{self.url}/image/{filename}' 

            return self._execute_request(method='get', url=url, params=params, status_code=status_code)
            
