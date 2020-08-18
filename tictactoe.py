from sys import setrecursionlimit

from menu import Menu
from player import PlayerFabric, Player
from field import Field
from utils import PlayerSign, PlayerType, Commands


"""
    prints game's info
"""


def print_info(is_game_over, winner, x_player, o_player, game_field):
    if is_game_over is None or not isinstance(game_field, Field):
        print('An error has occurred!')

    print(game_field)
    if is_game_over:
        print(f"{winner} wins" if winner is not None else "Draw")
    else:
        if game_field.active_player == x_player.payer_sign:
            x_player.print_move_message()
        else:
            o_player.print_move_message()


"""
    run main game cycle
"""


def run_game(x_player, o_player, game_field):
    if not isinstance(x_player, Player) \
            or not isinstance(o_player, Player) \
            or not isinstance(game_field, Field):
        return None

    is_game_over, winner = False, None
    while True:
        print_info(is_game_over, winner, x_player, o_player, game_field)
        if is_game_over is None or is_game_over is True:
            return is_game_over

        if game_field.active_player == x_player.payer_sign:
            x_player.make_move(game_field)
        else:
            o_player.make_move(game_field)

        is_game_over, winner = game_field.try_game_over()


def do_start_command(command_text, game_field):
    command_lst = command_text.split()
    if len(command_lst) != 3 \
            or command_lst[1] not in PlayerType.possible_player_types \
            or command_lst[2] not in PlayerType.possible_player_types:
        print("Bad parameters!")
        return None

    _, x_player_type, o_player_type = command_lst
    x_player = PlayerFabric.create_player(x_player_type, PlayerSign.X)
    o_player = PlayerFabric.create_player(o_player_type, PlayerSign.O)

    return run_game(x_player, o_player, game_field)


def main():
    setrecursionlimit(10000)

    game_field = Field()

    while True:
        command = Menu.get_command()

        if command.startswith(Commands.EXIT):
            return
        elif command.startswith(Commands.START):
            result = do_start_command(command, game_field)
            if result is True:
                game_field = Field()


if __name__ == '__main__':
    main()
