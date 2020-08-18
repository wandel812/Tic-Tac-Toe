from abc import ABC, abstractmethod

from utils import read_coord, PlayerType
from ai import EasyAI, MediumAI, HardAI


class Player(ABC):
    def __init__(self, player_type, player_sign):
        self.player_type = player_type
        self.payer_sign = player_sign

    @abstractmethod
    def print_move_message(self):
        pass

    @abstractmethod
    def make_move(self, field):
        pass


class HuPlayer(Player):
    def __init__(self, player_sign):
        super().__init__(PlayerType.USER, player_sign)

    def make_move(self, field):
        coord = read_coord(field)
        field.modify_field(coord)

    def print_move_message(self):
        print("Game not finished")


class AIPlayer(Player):

    def __init__(self, ai_player_type, player_sign):
        super().__init__(ai_player_type, player_sign)

    @abstractmethod
    def print_move_message(self):
        pass

    @abstractmethod
    def make_move(self, field):
        pass


class EasyAIPlayer(AIPlayer):
    def __init__(self, player_sign):
        super().__init__(PlayerType.EASY, player_sign)

    def make_move(self, field):
        coord = EasyAI.generate_move(field)
        field.modify_field(coord)

    def print_move_message(self):
        print('Making move level "easy"')


class MediumAIPlayer(AIPlayer):
    def __init__(self, player_sign):
        super().__init__(PlayerType.MEDIUM, player_sign)

    def make_move(self, field):
        coord = MediumAI.generate_move(field)
        field.modify_field(coord)

    def print_move_message(self):
        print('Making move level "medium"')


class HardAIPlayer(AIPlayer):
    def __init__(self, player_sign):
        super().__init__(PlayerType.HARD, player_sign)

    def make_move(self, field):
        coord = HardAI.generate_move(field)
        field.modify_field(coord)

    def print_move_message(self):
        print('Making move level "hard"')


class PlayerFabric:
    @staticmethod
    def create_player(pl_type, pl_sign) -> Player:
        player = None
        if pl_type == PlayerType.USER:
            player = HuPlayer(pl_sign)
        elif pl_type == PlayerType.EASY:
            player = EasyAIPlayer(pl_sign)
        elif pl_type == PlayerType.MEDIUM:
            player = MediumAIPlayer(pl_sign)
        elif pl_type == PlayerType.HARD:
            player = HardAIPlayer(pl_sign)
        return player
