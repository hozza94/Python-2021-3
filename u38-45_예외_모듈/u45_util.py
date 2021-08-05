class Account:
    def __init__(self, ano, owner, balance):
        self.ano = ano
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if self.__balance + amount >= 10000000:
            print("잔액 초과로 입금 불가")
        else:
            self.__balance += amount
            print(f'잔액은 {self.__balance}원 입니다.')

    def withdraw(self, amount):
        if self.__balance - amount < 0:
            print("잔액이 부족하여 출금할수 없습니다.")
        else:
            self.__balance -= amount
            print(f'잔액은 {self.__balance}원 입니다.')

    def __str__(self):
        return f'계좌번호: {self.ano}, 계좌주: {self.owner}, 잔액: {self.__balance:9,d}'