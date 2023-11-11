class Level:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"
    
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description
        }


class Mountains(Level):
    def __init__(self, elevation = 0):
        super().__init__(name="Mountains", description="A cold and treacherous mountain range filled with danger and mystery.")
        self.elevation = elevation
        
    def to_dict(self):
        data = super().to_dict()
        data['elevation'] = self.elevation
        return data

class Desert(Level):
    def __init__(self, elevation = 0):
        super().__init__(name="Desert", description="An unforgiving desert landscape with scorching heat and hidden threats.")
        self.elevation = elevation

    def to_dict(self):
        data = super().to_dict()
        data['elevation'] = self.elevation
        return data

class Forest(Level):
    def __init__(self, elevation = 0):
        super().__init__(name="Forest", description="A dense and vibrant forest teeming with life and lurking perils.")
        self.elevation = elevation

    def to_dict(self):
        data = super().to_dict()
        data['elevation'] = self.elevation
        return data