class Soldier:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.health = 100

class Archer(Soldier):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        self.range = 2
        self.damage = 10

class Melee(Soldier):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)
        self.range = 1
        self.damage = 20

class Game:
    def __init__(self, n):
        self.board = [[x]*n for x in range(n)]
        self.players = [[], []]
        self.turn = 0

    def add_soldier(self, soldier_type, id, x, y):
        if any(soldier.id == id for soldier in self.players[self.turn]):
            return "duplicate tag"
        if not (0 <= x < len(self.board) and 0 <= y < len(self.board)):
            return "out of bounds"
        if soldier_type == 'archer':
            soldier = Archer(id, x, y)
        else:
            soldier = Melee(id, x, y)
        self.players[self.turn].append(soldier)
        self.board[x][y] = soldier
        self.turn = 1 - self.turn

    def move(self, id, direction):
        soldier = next((soldier for soldier in self.players[self.turn] if soldier.id == id), None)
        if soldier is None:
            return "soldier does not exist"
        dx, dy = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}[direction]
        new_x, new_y = soldier.x + dx, soldier.y + dy
        if not (0 <= new_x < len(self.board) and 0 <= new_y < len(self.board)):
            return "out of bounds"
        self.board[soldier.x][soldier.y] = None
        soldier.x, soldier.y = new_x, new_y
        self.board[new_x][new_y] = soldier
        self.turn = 1 - self.turn

    def attack(self, attacker_id, target_id):
        attacker = next((soldier for soldier in self.players[self.turn] if soldier.id == attacker_id), None)
        if attacker is None:
            return "soldier does not exist"
        target = next((soldier for soldier in self.players[1-self.turn] if soldier.id == target_id), None)
        if target is None:
            return "soldier does not exist"
        if abs(attacker.x - target.x) + abs(attacker.y - target.y) > attacker.range:
            return "the target is too far"
        target.health -= attacker.damage
        if target.health <= 0:
            self.players[1-self.turn].remove(target)
            self.board[target.x][target.y] = None
            return "target eliminated"
        self.turn = 1 - self.turn

    def info(self, id):
        for player in self.players:
            soldier = next((soldier for soldier in player if soldier.id == id), None)
            if soldier is not None:
                return f"health: {soldier.health}\nlocation: {soldier.x} {soldier.y}"
        return "soldier does not exist"

    def who_is_in_the_lead(self):
        healths = [sum(soldier.health for soldier in player) for player in self.players]
        if healths[0] > healths[1]:
            return "Player 1 is in the lead"
        elif healths[0] < healths[1]:
            return "Player 2 is in the lead"
        else:
            return "draw"

    def run(self):
        while True:
            command = input().split()
            if command[0] == 'end':
                break
            elif command[0] == 'new':
                soldier_type, id, x, y = command[1], int(command[2]), int(command[3]), int(command[4])
                if self.add_soldier(soldier_type, id, x, y)!=None:
                    print(self.add_soldier(soldier_type, id, x, y))
            elif command[0] == 'move':
                id, direction = int(command[1]), command[2]
                if self.move(id, direction)!=None:
                    print(self.move(id, direction))
            elif command[0] == 'attack':
                attacker_id, target_id = int(command[1]), int(command[2])
                if self.attack(attacker_id, target_id)!=None:
                    print(self.attack(attacker_id, target_id))
            elif command[0] == 'info':
                id = int(command[1])
                print(self.info(id))
            elif command[0] == 'who':
                print(self.who_is_in_the_lead())

n = int(input())
game = Game(n)
game.run()
