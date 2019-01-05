class LowBalanceError(Exception):
	def __init__(self):
		pass	

class Account:
	'Simulates a bank accout'
	min_bal = 50;
	def __init__(self, acc_no, bal = 0.0):
		self.account_no = acc_no
		self.balance = bal

	def deposit(self, amnt):
		self.balance += amnt

	def withdraw(self, amnt):
		bal = self.balance 
		if(bal - amnt <= Account.min_bal):
			raise LowBalanceError()
		else:
			self.balance -= amnt
		

	def show_balance(self):
		print("Balance in account %s is Rs %.2f" % (self.account_no, self.balance))

class Savings(Account):
	int_rate = 0.04
	def deposit(self, amnt):
		self.balance = self.balance + (amnt + (amnt * Savings.int_rate))

class Current(Account):
	max_od = 1000
	def withdraw(self, amnt):
		self.balance -= amnt

class Bank:

	'Simulates a bank'
	def open_account(self):		
		print("Welcome to Bank")
		while(True):
			atype = input("Select your account type: (1)Savings (2)Current ")
			if(atype in ("1", "2")):
				an = input("Enter account number: ")
				acc1 = Bank.get_acc(atype, an)
				return acc1
			else:
				print("%s is an invalid entry, try again..." % (atype))
				continue;

	def do_transaction(self, acc):		
		while(True):
			opt = input("Select an operation: (1)Deposit (2)Withdraw (3)Balance (0)Exit ")
			if(opt in ("1", "2", "3", "0")):
				Bank.transact(acc, opt)
			else:
				print("%s is an invalid entry, try again..." % (opt))
				continue;
	
	def get_acc(atype, ano):
		acc1 = None
		if(int(atype) is 1):
			acc1 = Savings(ano)	
		else:
			acc1 = Current(ano)			
		return acc1

	def transact(acc, opt):
		if(int(opt) is 1):
			amnt = float(input("Enter amount to deposit: "))
			acc.deposit(amnt)
		elif(int(opt) is 2):
			amnt = float(input("Enter amount to withdraw: "))
			try:
				acc.withdraw(amnt)
			except LowBalanceError:
				print("Error. Insufficient Fund!!")			
		elif(int(opt) is 3):			
			acc.show_balance()			
		else:
			print("Thank you for banking with us..")
			exit()

b = Bank()	
acc1 = b.open_account()
try:
	b.do_transaction(acc1)
except Exception:
	print("Error")
