class Level:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class Mountains(Level):
    def __init__(self):
        super().__init__(name="Mountains", description="A cold and treacherous mountain range filled with danger and mystery.")


class Desert(Level):
    def __init__(self):
        super().__init__(name="Desert", description="An unforgiving desert landscape with scorching heat and hidden threats.")


class Forest(Level):
    def __init__(self):
        super().__init__(name="Forest", description="A dense and vibrant forest teeming with life and lurking perils.")
