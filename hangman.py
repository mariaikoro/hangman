import random
import sys


class Hangman(object):
    def __init__(self, level=5, non_ascii=False, dictionary='american'):
        #self, level=5, non_ascii=False, dictionary= 'american'
        #removed bc it said no variable?
        #level=self.level
        file=open(dictionary)
        text=file.read()
        low=text.split('\n')
        dict=[]
        self.h_dict=[]
        if non_ascii==False:
            self.non_ascii=False
            for k in range (0, len(low)):
                word=low[k]
                ok_word=True
                if "'" in word:
                    ok_word=False
                for l in range(0, len(word)):
                    if ord(word[l]) not in range(97,123):
                        ok_word=False
                if ok_word==True:
                    dict.append(word)#dictionary of a-z characters
            for n in range(0,len(dict)):
                if len(dict[n])>=level:
                    self.h_dict.append(dict[n])
        if non_ascii==True:#in the case of non_ascii being allowed, i also allowed uppercase letters because I cannot change the unicode characters in another dictionary to all lowercase
            #although non_ascii I leave out symbols from the words like ? , / etc
            self.non_ascii=True
            for k in range (0, len(low)):
                word=low[k]
                ok_word=True
                if "'" in word:
                    ok_word=False
                for l in range(0, len(word)):
                    if ord(word[l])<65:
                        ok_word=False
                    if ord(word[l]) in range(92,97):
                        ok_word=False
                    if ord(word[l]) in range(123,127):
                        ok_word=False
                if ok_word==True:
                    dict.append(word)
            for n in range(0,len(dict)):
                if len(dict[n])>=level:
                    self.h_dict.append(dict[n])



    def valid_letter(self, letter):
        if self.non_ascii==False:
            if len(letter)!=1:
                valid=False
                return valid
            if ord(letter) not in range(97,123):
                valid=False
            else:
                valid=True
        if self.non_ascii==True:
            if len(letter)!=1:
                valid=False
                return valid
            elif ord(letter) in range (92,97):
                valid=False
            elif ord(letter)<65 or ord(letter) in range(123,127):
                valid=False
            else:
                valid=True
        return valid

    def play(self):
        y=random.randint(0,len(self.h_dict))#randint or rand range
        used_letters=[]
        wrong_letters=[]
        word_length=[]
        fix='   '
        #fix="    "
        h1= " -----"
        h2= '\n |'
        hstart= h1 + 6*h2
        board1= h1 + h2 + "   |" + 5*h2
        board2= h1+h2+ "   |"+h2+ "   O" +4*h2
        board3= h1+h2+ "   |"+h2+ "   O" +h2+"   |"+3*h2
        board4= h1+h2+ "   |"+h2+ "   O" +h2+"  /|"+3*h2
        board5= h1+h2+ "   |"+h2+ "   O" +h2+"  /|"+chr(92)+3*h2
        board6= h1+h2+ "   |"+h2+ "   O" +h2+"  /|"+chr(92)+h2+"  /"+2*h2
        board7= h1+h2+ "   |"+h2+ "   O" +h2+"  /|"+chr(92)+h2+"  / "+chr(92)+2*h2
        boards=[board1, board2, board3, board4, board5, board6, board7]
        #word="dictionary"
        word=self.h_dict[y]#fix when fix dictionary
        h_word= "   "+" _"* len(word) + "\n"
        #print(self.h_dict)
        print (hstart)
        print(h_word)
        letter=input("Guess a letter:")
        while len(word_length)<len(word):
            while self.valid_letter(letter)==False:
                print("Not a valid letter")
                letter=input("Guess a letter:")
            # while len(letter)!=1:
            #     #print("Not a valid letter")
            #     #letter=input("Guess a letter:")
            if len(wrong_letters)==0:
                board=hstart
            else:
                for k in range (0,len(wrong_letters)):
                    board=boards[k]
            if letter in used_letters:
                print("You have already guessed '"+letter+"'.")
                print(board)
                print(fix)
                print(h_word)
                letter=input("Guess a letter:")
            elif letter not in used_letters:
                if letter not in word:
                    used_letters.append(letter)
                    wrong_letters.append(letter)
                    print("Wrong!")
                    for k in range (0,len(wrong_letters)):
                        board=boards[k]
                    print(board)
                    print(fix)
                    print(h_word)
                    if board==boards[6]:
                        print("You lose!")
                        print("Correct word is: \n")
                        correct_word='   '
                        for k in range(0,len(word)):
                            correct_word=correct_word+" "+word[k]
                        print(correct_word)
                        print(h_word)
                        newgame=input("Another game? (y/n):")
                        if newgame=="y":
                            print("New Game \n")
                            hangman.play()

                        else:
                            print("Game over.")
                            exit()
                    else:
                        letter=input("Guess a letter:")
                if letter in word:
                    if letter in used_letters:
                        print("You have already guessed '"+letter+"'.")
                    else:
                        print ("Correct!")
                        used_letters.append(letter)
                        for k in range (0,len(word)):
                            if letter==word[k]:
                                word_length.append(letter)
                            else:
                                pass
                    # if len(word_length)==len(word):
                    #     print("You win!")
                    fix='   '
                    for k in range (0,len(word)):
                        if word[k] not in word_length:
                            #print(hstart)
                            fix=fix+ "  "
                        elif word[k] in word_length:
                            fix= fix+" "+ word[k]
                    print(board)
                    print(fix)
                    print(h_word)
                    if len(word_length)==len(word):
                        print("You win!")
                        newgame=input("Another game? (y/n):")
                        if newgame=="y":
                            print("New Game \n")
                            hangman.play()
                        else:
                            print("Game over.")
                            exit()
                    else:
                        letter=input("Guess a letter:")


#print(chr(126))
#print(h_dict)
#print(word)
# word='word'
# for k in range (0, len(word)):
#     print (word[k])
hangman=Hangman()
hangman.play()
