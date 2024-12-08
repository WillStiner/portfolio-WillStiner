import requests

class RandomCatFactsAPI:
    def __init__(self, amount):
        '''
        initializes the random cat facts API
        args: amount- int - the amount of cat facts the user wants to see
        retuns: none 
        '''
        self.url = f'https://meowfacts.herokuapp.com/?count={amount}'
        
    def get(self):
        '''
        pulls data from the random cat facts api
        args: none
        retuns: none 
        '''
        result = requests.get(self.url)
        response = result.json()
        print(response)