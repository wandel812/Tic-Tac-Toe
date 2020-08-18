coord_to_index = {(1, 3): 0, (2, 3): 1, (3, 3): 2,
                  (1, 2): 3, (2, 2): 4, (3, 2): 5,
                  (1, 1): 6, (2, 1): 7, (3, 1): 8}

index_to_coord = {0: (1, 3), 1: (2, 3), 2: (3, 3),
                  3: (1, 2), 4: (2, 2), 5: (3, 2),
                  6: (1, 1), 7: (2, 1), 8: (3, 1)}


def from_coord_to_index(x, y):
    return coord_to_index[(x, y)]


def from_index_to_coord(index):
    return index_to_coord[index]


def read_coord(game_field):
    from field import Field

    if not isinstance(game_field, Field):
        return None

    while True:
        input_list = input("Enter the coordinates: ").split(' ')

        if len(input_list) != 2:
            print('You should enter numbers!')
            continue

        x, y = input_list

        if not (x.isdigit() and y.isdigit()):
            print('You should enter numbers!')
            continue

        x = int(x)
        y = int(y)

        if not (1 <= x <= 3 and 1 <= y <= 3):
            print('Coordinates should be from 1 to 3!')
            continue

        if not (game_field.cells[from_coord_to_index(x, y)] == '_'):
            print('This cell is occupied! Choose another one!')
            continue

        return x, y


class PlayerSign:
    X = 'X'
    O = 'O'
    possible_player_signs = [X, O]

    @staticmethod
    def get_opposite(player_sign):
        if player_sign == PlayerSign.X:
            return PlayerSign.O
        else:
            return PlayerSign.X


class PlayerType:
    USER = 'user'
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'
    possible_player_types = [USER, EASY, MEDIUM, HARD]


class FieldSign:
    X = 'X'
    O = 'O'
    EMPTY = '_'
    possible_field_sings = (X, O, EMPTY)


class Commands:
    START = "start"
    EXIT = "exit"
    possible_commands = [START, EXIT]
