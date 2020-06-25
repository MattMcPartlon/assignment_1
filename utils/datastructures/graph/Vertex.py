class Vertex:
    
    def __init__(self, idx = None, data=None):
        self.data = data
        self.idx = idx
        
    def get_data(self):
        return self.data

    def get_index(self):
        return self.idx

    def __hash__(self):
        if self.idx is None:
            raise Exception('no hash code given')
        return self.idx

    def has_index(self):
        return self.idx is not None

    def has_hash(self):
        return True

    def __str__(self):
        return 'Vertex : ' + str(self.idx)




