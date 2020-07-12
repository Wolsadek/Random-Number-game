import random

flag = True
while flag:
    num = input('digite um número:')

    if num.isdigit() :
        print('vamos jogar!')
        num = int(num)
        flag = False
    else:
        print('entrada invalida! tente denovo!')

secret = random.randint(1,num)             

guess = None
count = 1

while guess != secret:
    guess = input('por favor escolha um número entre 1 e ' + str(num) + ':')
    if guess.isdigit():
        guess = int(guess)
         
    if guess == secret:
         print('você conseguiu! Parabéns')  
    else:
        print('por favor, tente denovo!')
        count += 1

print('o seu número é', count, ', este número é quantas pessoas querem te namorar!')  


print('Obrigado por jogar! Volte sempre!')     