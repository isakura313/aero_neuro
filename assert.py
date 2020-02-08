import random 

kilometri = 100
mili = 62.13
# подбор коэфицента
# enter = input("введите коэфицент наудачу")
# coef = float(enter)

def assort(coef):
	Error = mili - (kilometri * coef)
	print("Your error:" + str(Error))
# lr = learning rate
#accur = accurancy точность

def assert_auto(epoch, lr, accur):
	coef = random.uniform(0, 1)
	for i in range(epoch):
		Error = mili - (kilometri * coef)
		print(Error)
		if Error>0:
			coef+=lr
		elif Error<0 :
			coef-=lr
		elif Error < accur:
			print("Our Final Score"+ str(Error))
epoch = int(input("epoch: "))
lr = float(input("enter learning rate"))
accur = float(input("enter accurancy"))



assert_auto(epoch, lr, accur)



