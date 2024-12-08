import requests

class RandomDogFactsAPI:
    def __init__(self, amount):
        '''
        initializes the random dog facts API
        args: amount - int - the amount of dog facts the user wants to see
        retuns: none 
        '''        
        self.url = f'http://dog-api.kinduff.com/api/facts?number={amount}'
    
    def get(self):
        '''
        pulls data from the random dog facts api
        args: none
        retuns: none 
        '''
        result = requests.get(self.url)
        response = result.json()
        print(response)