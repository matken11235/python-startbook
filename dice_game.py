#coding:utf-8
import dice

num = input('4,6,8,12,20のどれで勝負しますか？：')

my_dice = dice.Dice(num)
cpu_dice = dice.Dice(num)

my_pip = my_dice.shoot()
cpu_pip = cpu_dice.shoot()

print('CPU：' + str(cpu_pip) + '  あなた：' + str(my_pip))

if my_pip > cpu_pip:
	print('勝ち')
elif my_pip < cpu_pip:
	print('負け')
else:
	print('引き分け')