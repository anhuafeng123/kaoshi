import random
class HuYouJia_Num(object):
	def __init__(self):
		self.HuYouJia_sum = 0
		self.HuYouJia_sum1 = 0
		self.HuYouJia_list = []
		self.HuYouJia_dic = {}
		self.HuYouJia_count =0
		self.HuYouJia_count1 = 1

	def HuYouJia_cai(self):
		i = random.randint(0, 100)
		while True:
			player = int(input("输入你猜的数字")) 
			if player > i:
				print("猜的数字太大了")
				self.HuYouJia_count+=1
				continue
			if player <i:
				print("猜的太小了哈哈")
				self.HuYouJia_count+=1
			if player == i:
				print("哇,猜中了")
				print("你一共猜了%d次才猜中!"%self.HuYouJia_count)
				self.HuYouJia_count1+=1
				o = int(input("请问您还要继续玩吗\n1.继续  2.退出"))
				if o == 1:
					print("又开始喽")
					self.HuYouJia_dic = {self.HuYouJia_count1 - 1:self.HuYouJia_count}
					self.HuYouJia_list.append(self.HuYouJia_dic)
					print(self.HuYouJia_list)
					continue
				if o == 2:
					self.HuYouJia_dic = {self.HuYouJia_count1 - 1:self.HuYouJia_count}
					self.HuYouJia_list.append(self.HuYouJia_dic)
					print("你一共玩了%d次"%(self.HuYouJia_count1-1))
					for i in self.HuYouJia_list:
						for k,v in i.items():
							print("你第%d次猜了%d次才猜中"%(k,v))
							self.HuYouJia_sum1+=v
					print("平均猜中的次数是%d"%(self.HuYouJia_sum1/(self.HuYouJia_count1-1)))
					break
if __name__ == "__main__":
	HuYouJia  = HuYouJia_Num()
	HuYouJia.HuYouJia_cai()

