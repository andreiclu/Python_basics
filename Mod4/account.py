from abc import abstractmethod
import json


class Human:
    def __init__(self, name, lastname, cnp, accountId, cash):
        self.name = name
        self.lastname = lastname
        self.cnp = cnp
        self.accountId = accountId
        self.cash = cash

    @abstractmethod
    def salariu(self):
        pass
class Student(Human):
    def salariu(self):
        self.cash += 500

class Teacher(Human):
    def salariu(self):
        self.cash += 2500

class Doctor(Human):
    def salariu(self):
        self.cash += 4500



class ATM:
    def __init__(self, accounts, transactions, location):
        self.transactions = transactions
        self.location = location
        self.accounts_dict = {}
        for account in accounts:
            self.accounts_dict[account['id']] = account

    def _get_user_account(self, user):
        return self.accounts_dict.get(user.accountId, None)

    def withdrawMoney(self, user: Human, amount):
        account = self._get_user_account(user)
        if account is None:
            raise Exception("User account does not exist")

        if amount > account['ammount']:
            raise Exception("User account does not have enough money")

        self.transactions.append({'id': len(self.transactions),
                                  'ammount': amount,
                                  'accountId': user.accountId,
                                  'type': 'retragere'})
        account['ammount'] -= amount

    def addMoney(self, user: Human, amount: int):
        account = self._get_user_account(user)
        if account is None:
            account = {'id': user.accountId,
                       'ammount': -25}  # comision deschidere cont xD
            self.accounts_dict[user.accountId] = account
        self.transactions.append({'id': len(self.transactions),
                                  'ammount': amount,
                                  'accountId': user.accountId,
                                  'type': 'depunere'})
        account['ammount'] += amount

    # acccount = { "id": id, "ammount": ammount}

    def getMoney(self, user: Human):
        account = self._get_user_account(user)
        if account is None:
            raise Exception("User account does not exist")
        return account["ammount"]
    def getReport(self):
        with open("transactions.json", 'w') as fp:
            json.dump(self.transactions, fp, indent = 2)


def main():
    humans = [Student("Bogdan", "Moraru", 1929923130123, 1, 0),
         Teacher("T1", "T2", 1891421412459, 2, 400),
         Doctor("D1", "D2", 1659545259295, 3, 500)]
    for human in humans:
        human.salariu()

    atm = ATM([],[],'')
    atm.addMoney(humans[0], 1500)
    atm.addMoney(humans[1],2500)
    atm.addMoney(humans[2],3000)

    atm.withdrawMoney(humans[1], 200)
    atm.withdrawMoney(humans[2], 150)

    print(atm.getMoney(humans[1]))

    atm.getReport()



if __name__ == '__main__':
    main()