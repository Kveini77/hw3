class Bank:
    def __init__(self, name, balanse):
        self._name = name
        self._balanse = balanse

    def moneyX(self):
        amount = int(input("Введите число короторое хотите законуть на счет: "))
        if amount > 0:
            self._balanse += amount
            print(f"Счет поплнет на {amount} сомов. Текущий баланс: {self._balanse} сом")
        else:
            print("Сумма для пополнения должна быть положительной")

    def _kill(self):
        self._balanse = 0
        print("Баланс обнулён")

    def __jackpot(self):
        self._balanse *= 10
        print(f"Поздравляем, вы выиграли джекпот! Новый баланс: {bank._balanse}")

    def _combine_balance(self, other):
        if isinstance(other, Bank):
            self._balanse += other._balanse
            other._balanse = self._balanse
            print(f"Балансы объединены Текущий баланс: {self._balanse} сом")
        else:
            print("Ошибка: второй объект не является экземпляром класса Bank")


bank = Bank("Roman", 100)

print(f"Начальный баланс: {bank._balanse}")

bank.moneyX()

bank._Bank__jackpot()

another_bank = Bank("Batyr", 200)
bank._combine_balance(another_bank)

bank._kill()

print(f"Финальный баланс: {bank._balanse}")
