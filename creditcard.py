#Credit Card Luhn Test
class CreditCard:
	
	def __init__(self,card_num):
		self.card_num = card_num
		
		self.type = "Invalid"
		self.determine_type()
		
		self.passes_luhn = False
		self.luhn_test()
		
		self.valid = False
		if self.type != "Invalid" and self.passes_luhn:
			self.valid = True
		
	def determine_type(self):
		if self.card_num[0] == "4" and len(self.card_num) == 16:
			self.type = "Visa"
		if self.card_num[0:2:1] in ["51","52","53","54","55"] and len(self.card_num) == 16:
			self.type = "Mastercard"
		if self.card_num[0:2:1] in ["34","37"] and len(self.card_num) == 15:
			self.type = "AMEX"
		if self.card_num[0:4:1] == "6001" and len(self.card_num) == 16:
			self.type = "Discover"

	def luhn_test(self):
		regular = self.card_num[-1::-2]
		
		total = 0
		
		for x in regular:
			x = int(x)
			total += x
			#print(x) #04953999=48
		#print("regular: ",total) #48
		
		double = self.card_num[-2::-2]
		for x in double:
			x = int(x)*2
			#print(x) 
			if x >= 10:
				x = str(x)
				#print(x) #14 10 12 16
				for y in x:
					y = int(y)
					total += y
					#print(y) #14101216 = 16
			else:
				total += x
				#print(total) #59678290
		#print("double: ",total) #42

		if total % 10 == 0:
			self.passes_luhn = True

		

v1 = CreditCard("4929896355493470")
m1 = CreditCard("5515460934365316")
a1 = CreditCard("341640057061013")
d1 = CreditCard("6011053711075799")

print("v1=",v1.type,"is",v1.valid)
print("m1=",m1.type,"is",m1.valid)
print("a1=",a1.type,"is",a1.valid)
print("d1=",d1.type,"is",d1.valid)
