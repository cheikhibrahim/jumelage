import random
n=random.randint(1,100)
nbretentative=5
while nbretentative>0:
    nbretentative-=1
    var=int(input('entrer un nombre :'))
    if var<n:
        print('tres petite')
    elif var>n:
            print('plus grand')
else:
                print('tu as gagner')
