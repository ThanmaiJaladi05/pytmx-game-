class Game:
    def __init__(self):
        self.score = 0
        self.health = 100

    def update_score(self, points):
        self.score += points

    def update_health(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.end_game()

    def end_game(self):
        print("Game Over")
        # Display end screen
