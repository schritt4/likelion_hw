word = input('Enter a sentence: ')
x= word.lower()
vowel = ['a','e','i','o','u']

n=0
for i in vowel:
    n += x.count(i)
       
if(n==1):
    print('Your sentence contains', n, 'vowel')
else:
    print('Your sentence contains', n, 'vowels')