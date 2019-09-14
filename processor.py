from indexerclient import IndexerClient

class Processor:
    def __init__(self):
        self.indexerClient = IndexerClient()
        self.indexerClient.getAccessToken()
    
    def search(phrase):
        return indexerClient.search(phrase)