# Iterator Pattern

import string


class SportTeamIterator:
    def __init__(self, members):
        self._members = members
        self._idx = 0

    def __next__(self):
        if self._idx < len(self._members):
            val = self._members[self._idx]
            self._idx += 1
            return val
        else:
            raise StopIteration

    def __iter__(self):
        print('SportTeamIterator __iter__() method called ')
        return self


class SportTeam:
    def __init__(self):
        self._members = []

    def add_member(self, name):
        if name.strip():
            self._members.append(string.capwords(name))

    def __iter__(self):
        print('SportTeam __iter__() method called ')
        return SportTeamIterator(self._members)


def main():
    sport_team = SportTeam()
    sport_team.add_member(' dudley stokes')
    sport_team.add_member('  devon harris')
    sport_team.add_member('michael white ')
    sport_team.add_member('  chris stokes')

    for member in sport_team:
        print(member)


if __name__ == '__main__':
    main()