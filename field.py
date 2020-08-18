from utils import from_coord_to_index, from_index_to_coord, PlayerSign, FieldSign


class Field:

    def __init__(self, initial_field=(FieldSign.EMPTY * 9), active_player=PlayerSign.X):
        self.winner = None
        self.cells = initial_field
        self.active_player = active_player

    """
        :return None if there is no winner
                'X' if X is a winner
                'O' if O is a winner
    """

    def try_get_winner(self):
        def get_winner_of_rows(cells):
            _winner = None
            for row in range(3):
                start_index = row * 3
                end_index = start_index + 3
                if all(cell == FieldSign.X for cell in cells[start_index:end_index]):
                    _winner = PlayerSign.X
                elif all(cell == FieldSign.O for cell in cells[start_index:end_index]):
                    _winner = PlayerSign.O
            return _winner

        def get_winner_of_cols(cells):
            _winner = None
            for col in range(3):
                start_index = col
                end_index = 9
                step = 3
                if all(cell == FieldSign.X for cell in cells[start_index:end_index:step]):
                    _winner = PlayerSign.X
                elif all(cell == FieldSign.O for cell in cells[start_index:end_index:step]):
                    _winner = PlayerSign.O
            return _winner

        def get_winner_of_diagonals(cells):
            _winner = None
            if (cells[0] == cells[4] == cells[8]) \
                    or (cells[2] == cells[4] == cells[6]):
                if cells[4] == FieldSign.X:
                    _winner = PlayerSign.X
                elif cells[4] == FieldSign.O:
                    _winner = PlayerSign.O
            return _winner

        def get_game_winner(cells):
            _winner = get_winner_of_rows(cells)
            if _winner is None:
                _winner = get_winner_of_cols(cells)
            if _winner is None:
                _winner = get_winner_of_diagonals(cells)
            return _winner

        self.winner = get_game_winner(self.cells)
        return self.winner

    def modify_cell(self, coord, pl_sign):
        if pl_sign not in PlayerSign.possible_player_signs:
            return TypeError

        cells_list = list(self.cells)
        x, y = coord
        if pl_sign == PlayerSign.X:
            cells_list[from_coord_to_index(x, y)] = FieldSign.X
        else:
            cells_list[from_coord_to_index(x, y)] = FieldSign.O

        self.cells = ''.join(cells_list)

    def modify_field(self, coord):
        self.modify_cell(coord, self.active_player)
        self.active_player = PlayerSign.get_opposite(self.active_player)

    def has_empty_cell(self):
        return any(cell == '_' for cell in self.cells)

    """
    :return True when game has finished successfully, 
            False when game has not finished yet
            None when an error has occurred
    """

    def try_game_over(self):
        winner = self.try_get_winner()

        if not isinstance(self, Field):
            return None

        if winner is not None:
            return True, winner
        else:
            return not self.has_empty_cell(), winner

    def get_free_cell_indexes(self):
        return [item[0] for item in enumerate(self.cells) if item[1] == FieldSign.EMPTY]

    def get_free_cell_coords(self):
        return [from_index_to_coord(item) for item in self.get_free_cell_indexes()]

    def __str__(self):
        cell_list = list(self.cells.replace('_', ' '))
        field_lines = "\n".join(
            [f'| {" ".join(cell_list[start: (start + 3)])} |'
             for start in range(0, 9, 3)]
        )
        return f"---------\n{field_lines}\n---------"
