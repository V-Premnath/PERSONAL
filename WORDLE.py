"""Python program for a game"""
# a 5 letterd word is given as input
# the user has 6 chances
# usr needs to guess a randonm word correctly

import random
list=['patch','reach','match','cheat','quite','pride','bride','chant','chord','trade','earth','abuse','rival','frame','argue','treck','react','thick','trial','tuple','relay','delay','aloud','valid','gloat','vigor','value','slate','suite','shown','early','youth','exact','exist','table','blade','drain','pound','ounce','storm','charm','north','south','beach','trial','erupt','moral','haunt','young','yield','loser','sober','flare','glare','spike','pixel','nexus','hoard','adore','flush','flesh','prime','video','worth','cargo','trend','blend','ocean','bread','inter','intra','clean','beans','extra','ultra','alter','shift','wheat','alter','space','white','prawn','blink','blank','dream','tolet','giant','saint','paint','house','chart','mount','count','blunt','image','mango','maize','heart','liver','urine','minor','chalk','cheap','super','under','waste','haste','paste','mouse','house','horse','scorn','penis','shock','bench','belch','chair','choir','prose','crane','study','scale','whale','chief','purse','strip','store','stone','shine','binge','bingo','being','short','smart','sharp','shark','jeans','niche','night','witch','shape','morph','bitch','guard','grave','force','score','spore','ready','spine','learn','tough','music','story','pause','stare','glare','scare','other','think','honey','fancy','minus','delta','month','plane','about','ought','child','penta','sword','royal','today','speak','style','siren','viral','virus','clown','clone','cramp','clamp','swamp','bulge','fetch','cloak','imply','erupt','batch','split','smoke','slope','dwarf','torch','surge','flute','arise','stain','track','trick','excel','axiom','youth','yatch','naive','peach','truck','trunk','thumb','maize','cabin','crime','abide','rinse','bunch','punch','lunch','flame','blame','slave','great','comet','combo','slate','slice','plate','helio','guest','tiger','drown','multi','swear','noise','reign','later','focus','plain','climb','lymph','grunt','sweat','drive','front','drone','index','piano','drunk','stove','quest','spoil','yeast','beast','heist','worst','brain','grain','olive','debug','first','feast','proud','cloud','mould','sound','field','false','dance','cause','teach','zebra','anime','pilot','style','chain','clove','glove','touch','burst','curse','craft','group','print','point','while','bring','swing','sling','route','tired','vault','fault','groin','train','close','crank','phone','crush','trash','brush','squid','solid','magic','drugs','quite','plead','guilt','field','yield','shave','brave','screw','glide','slide','poise','voice','speak','crude','break','while','black','block','swamp','hoist','eight','flair','organ','prick','panel','brick','shawl','light','power','shove','solve','fight','might','right','towel','camel','lower','knife','snail','ghost','roast','boast','shine','frock','frost','slime','swipe','swift','fruit','lunar','latin','wafer','shirt','urine','crown','round','prize','brown','crown','sugar','scion','joint','snack','cream','court','water','pulse','juice','sport','phone','beard','among','input','watch','hinge','thorn']
print("\n\t\tGuess the word".title(),'\n\n          ---no letter is repeated---\n\t---5 letterd words only---\n\t---all letters in lowercase---')
b=random.randint(0,len(list))                                                                # getting a random index number in the list
j=0
while j<6:                                                                                   # outer loop for continuation of the program until 6times
    n=str(input('\ninput  : '))                                                             # accepting input from the usr
    if len(n)==5 :
                                                                                   # condition for accepting 5 lettered words only           
        if n in list:                                                                        # assigning index values for the input
            i=0                                                                              # if the word is inthe defined list
            c=list[b]                                                                        # assigning random index value and respective word in the list to a variable 
            while i<5:                                                                       # inner loop for checking the letters
                if n[i] in c:                                                                # condition for checking if letters are present in both random and input word   
                    print(n[i],'True',end="")                                                # print statement if letter exists in both the words
                    if n[i]==c[i]:                                                           # condition checking the position of the letter if it exists in both
                        print('\tin correct position')                                       # print statement to specfy the correctness of the letter's position
                    else:
                        print('\tin wrong position')                                     # print statement to specfy the incorrectness of the letter's position 
                else:
                    print(n[i],'False')                                                      # print statement if the letter doesnt exist
                i=i+1                                                                        # iteration for inner loop
            if n==c:                                                                         # condition check if both random and input words are same
                print('\n\t\t *** YOU WIN ***')                                              # print statement if the input is correct
                print("another game???")
                a1=str(input('Yes/No : '))
                if a1.lower=='yes':
                    continue
                else:
                    print("\nGOOD BYE !!!")
                    break                                                                        # Termination of program 
        else:                                                                                # if input is not in the list
            print('word not in list')                                                        # print statement if out of the box input is given
            j=j-1                                                                            # iteration for inner loop if out of the box input is given
    else:                                                                                    # if input is other than 5 letterd words
        print('only 5 lettered words ')                                                      # print statement
        j=j-1                                                                                # iteration for inner loop
    j=j+1  
    print('\t\t\t{} chances left'.format(6-j))                                                                                  # iteration for outer loop
if n!=list[b]:                                                                               # if all 6 inputs are incorrect
    print("\n\t the word is ----> ",list[b].capitalize(),'\n\t\t*** You lost ***','\n','BETTER LUCK NEXT TIME'.center(46,'_'))
else:                                                                          # print statemnt printing the corect random word and ending the program
    print('')  #print statement to satisfy else condition
