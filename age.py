# else if 另外如果
#此程式讓使用者輸入年齡並與最近有沒有開車
license = input('請問您最近有開車嗎?')
if license != '有' and license != '沒有':
	print('只能輸入  有/沒有  ，請重新操作!')
	raise SystemExit
age = input('請輸入您的年齡:')
age = int(age)
age2 = 18 - age
if age >= 18 and age <= 65:
	if license == '有':
		print('恭喜您通過驗證')
	elif license == '沒有':
		print('建議您去考駕照!')
	else:
		print('您輸入的資訊可能有誤，請重新操作!')
elif age >= 0 and age < 18:
	if license == '有':
		print('18歲以上才可以考駕照，請不要無照駕駛')
	elif license == '沒有':
		print('沒關係，您再過', age2, '年就可以考駕照囉!')
	else:
		print('您輸入的資訊可能有誤，請重新操作!')
elif age >= 65 and age < 150:
	if license == '有':
		print('請注意駕照有無過期')
	elif license == '沒有':
		print('已收到您的資訊!')
	else:
		print('您輸入的資訊可能有誤，請重新操作!')
else:
	print('您輸入的年齡可能有誤，請重新操作!')