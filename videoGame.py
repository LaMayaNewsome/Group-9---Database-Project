class videoGames:
    def __init__(self, ID, description, name, cost, platform):
        self.ID = ID
        self.description = description
        self.name = name
        self.cost = cost
        self.platform = platform

        game1 = videoGames("001", "Action-packed game with hight-end graphics", "Call of Duty: Modern Warfare", 59.99, "Xbox One")