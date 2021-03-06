class Game:
    def get_name(self):
        pass

    def get_type(self):
        pass

    def get_min_number_of_players(self):
        pass

    def get_max_number_of_players(self):
        pass

    def can_be_played_remotely(self):
        pass


class BoardGame(Game):
    def __init__(self, name, type, max_player_num):
        self._name = name
        self._type = type
        self._max_player_num = max_player_num

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_min_number_of_players(self):
        return 2

    def get_max_number_of_players(self):
        return self._max_player_num

    def can_be_played_remotely(self):
        return False

    def __str__(self):
        return f"{__name__} [name='{self._name}', type='{self._type}', max_player_num={self._max_player_num}]"


class PCGame(Game):
    def __init__(self, name, type, min_player_num, max_player_num, is_online):
        self._name = name
        self._type = type
        self._min_player_num = min_player_num
        self._max_player_num = max_player_num
        self._is_online = is_online

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_min_number_of_players(self):
        return self._min_player_num

    def get_max_number_of_players(self):
        return self._max_player_num

    def can_be_played_remotely(self):
        return False

    def __str__(self):
        return (f"{__name__} [name='{self._name}', type='{self._type}', min_player_num={self._min_player_num}"
                f", max_player_num={self._max_player_num}, is_online={self._is_online}]")


class GameFactory:
    def create(self):
        pass


class MonopolyGameCreator(GameFactory):
    def create(self):
        return BoardGame("Monopoly", "Family Game", 4)


class ValorantGameCreator(GameFactory):
    def create(self):
        return PCGame("Valorant", "FPS", 4, 10, True)


def main():
    game_type = input('Enter the type of game [PC, Board]: ')
    game_factory = None
    if game_type == 'PC':
        game_factory = ValorantGameCreator()
    elif game_type == 'Board':
        game_factory = MonopolyGameCreator()

    if game_factory:
        game = game_factory.create()
        print(game)


if __name__ == '__main__':
    main()