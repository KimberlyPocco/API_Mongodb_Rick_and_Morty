from pymongo import MongoClient

class DabataseConnection():
    def __init__(self, npags):
        self.client = MongoClient("mongodb://localhost:27017")
        self.url = "https://rickandmortyapi.com/api/character?page="
        self.ctx = self.client['rick_morty']
        self.collection = self.ctx.principal
        self.npags = npags