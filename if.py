money = True
if money:
    print("택시를 타고가라")
else:
    print("걸어가라")

money = 2000
card = True
if money >=3000 or card:
    print("택시를 타고가야지")
else:
    print("걸어가야지")

print(1 in [1, 2, 3])
print('j' not in 'python')

pocket = ['paper', 'cellphon', 'money']
if 'money' in pocket:
    print("운동위해 걸어")
else:
    print("돈없어서 걸어")

    
pocket = ['paper', 'cellphon', 'money']
if 'money' in pocket:
    pass
else:
    print("카드사용")