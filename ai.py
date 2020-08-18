from copy import deepcopy
from random import choice

from utils import from_index_to_coord, PlayerSign
from field import Field


class AI:
    """
        ai abstract class
    """


    """
        return coordinates of a random move
    """

    @staticmethod
    def generate_random_move(field):
        free_cells = field.get_free_cell_indexes()
        chosen_cell = choice(free_cells)
        return from_index_to_coord(chosen_cell)

    """
        return coordinates of move that win a game; otherwise None
    """

    @staticmethod
    def generate_move_to_win(field):
        for free_cell_coord in field.get_free_cell_coords():
            changed_field = Field(field.cells, field.active_player)
            changed_field.modify_field(free_cell_coord)
            changed_field_winner = changed_field.try_get_winner()
            if changed_field_winner is not None:
                return free_cell_coord
        return None

    """
        return coordinates of move that blocks opponent possibility
        to win by next move        
    """

    @staticmethod
    def generate_move_to_defend(field):
        for free_cell_coord in field.get_free_cell_coords():
            changed_field = Field(
                field.cells, PlayerSign.get_opposite(field.active_player))
            changed_field.modify_field(free_cell_coord)
            changed_field_winner = changed_field.try_get_winner()
            if changed_field_winner is not None:
                return free_cell_coord
        return None

    @staticmethod
    def generate_move(field):
        pass


class EasyAI(AI):
    @staticmethod
    def generate_move(field):
        if not isinstance(field, Field):
            return None

        return AI.generate_random_move(field)


class MediumAI(AI):
    @staticmethod
    def generate_move(field):
        if not isinstance(field, Field):
            return None

        coord = AI.generate_move_to_win(field)
        if coord is None:
            coord = AI.generate_move_to_defend(field)
        if coord is None:
            coord = AI.generate_random_move(field)
        return coord


class HardAI(AI):
    class Move:
        def __init__(self, index, score):
            self.index = index
            self.score = score

    @staticmethod
    def get_points(winner, ai_player):
        res = HardAI.Move(-1, 0)
        if winner is not None:
            res.score = 10 if winner == ai_player else -10
        return res

    """
        :return a namedtuple (index, score)
    """

    @staticmethod
    def minimax(field, ai_player):
        is_game_over, winner = field.try_game_over()
        if is_game_over:
            return HardAI.get_points(winner, ai_player)

        moves = []
        for empty_cell_index in field.get_free_cell_indexes():
            move = HardAI.Move(empty_cell_index, 0)
            new_field = deepcopy(field)
            new_field.modify_field(from_index_to_coord(empty_cell_index))
            move.score = HardAI.minimax(new_field, ai_player).score

            moves.append(move)

            if field.active_player == ai_player and move.score >= 10:
                return move
            if field.active_player != ai_player and move.score <= -10:
                return move

        for move in moves:
            if move.score == 0:
                return move

        return moves[0]

    @staticmethod
    def generate_move(field):
        # if first move
        if len(field.get_free_cell_indexes()) == 9:
            return from_index_to_coord(0)

        index = HardAI.minimax(deepcopy(field), field.active_player).index
        return from_index_to_coord(index)
