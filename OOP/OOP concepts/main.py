from banckaccountexercise import *
import random

hapoalem = Bank()

checking_account1 = CheckingAccount('chen', 90000, 211, 2000)
hapoalem.create_account(checking_account1)
saving_checking_account1 = SavingAccount('chen', 9876000, 4532, 0.016)
hapoalem.create_account(saving_checking_account1)
# print(checking_account1)
# print(saving_checking_account1)
# amount = float(input('enter the amount that you want to deposit'))
# checking_account1.deposit(amount)
# saving_checking_account1.add_interest()
# # once a month
#
# print(checking_account1)
# print(saving_checking_account1)
# print(saving_checking_account1.interest)

# checking_account1.deposit(24000)
# checking_account1.withdraw(20)
# checking_account1.deposit(211000)
# checking_account1.withdraw(2000)
# checking_account1.deposit(2000)
# checking_account1.deposit(200)
# checking_account1.withdraw(2600)
# checking_account1.deposit(2000)
#
# checking_account1.show_transactions()
#

print(hapoalem.find_account(4532))