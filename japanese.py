from random import sample

hiragana = []
with open('./hiragana.txt', encoding='utf8') as f:
    for line in f:
        hiragana += line.rstrip('\n').split(' ')
eng_letter = []
with open('./eng_letter.txt', encoding='utf8') as f:
    for line in f:
        eng_letter += line.rstrip('\n').split(' ')

promt = 'Type 1 to Review all '
mode = input(promt)
if mode != '1':
    hiragana = hiragana[-10:]
    eng_letter = eng_letter[-10:]
    print('Preview lastest 10 words')

num = len(hiragana)
times = 5
score = 0
review = []

while True:
    rand = sample(range(num), times)
    for idx in rand:
        print(hiragana[idx], end='\t')
        if hiragana[idx] not in review:
            review.append(hiragana[idx])
    ans = input('Type in: ')
    if not ans :
        print(f'User quit, highscore: {score}')
        break
    if len(ans.split(' ')) != times:
        print('seperate whitespace')
        continue
    flag = False
    for i, idx in enumerate(rand):
        if eng_letter[idx] != ans.split(' ')[i]:
            flag = True
            break
    if flag:
        for idx in rand:
            print(eng_letter[idx], end='\t')
        print(f'\nFail, final score: {score}')
        score = 0
    else:
        score += 1
        print(f'Great, score: {score}')
        if len(review) == num:
            print('all revisited!')
            review = []
    
    
