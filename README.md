# hangman
1 Rules of the game

The object of the game is to guess all the letters in a hidden word. The player guesses
at the missing letters.
1. If they guess a letter that has already been guess, they are prompted to try again.
2. If then enter something other than a single letter, they are prompted to try again.
3. If they guess a letter that appears in the word, then all instances of the letter in the
word are revealed. This will require updating and redrawing the board.
4. If they guess a letter that does not appear in the word, then another part of the
dangling figure is drawn. This will require updating and redrawing the board.
When all six parts of the figure are drawn, the game ends in a loss for the player and the
entire word is exposed for their edification. If the entire word has been guessed, the game
ends in a win for the player.
2 Implementation details
Implement hangman as a Hangman class. The class constructor init () should include
arguments that allow the user to specify
1. level, the difficulty of the game, in terms of the minimum number of letters in the
words,
2. non ascii, which is True if non-ASCII characters are allowed, and
1
3. dictionary, which specifies a default dictionary file to read.
All of these should have default values assigned to them.
For instance, in my implementation, init () starts like this:
c l a s s Hangman ( object ) :
def i n i t ( s e l f , l e v e l =5, n o n a s c i i=Fal se ,
d i c t i o n a r y=’ / u s r / s ha r e / d i c t / american ’ ) :
This sets the default difficulty to words of length five and longer, causes words with nonASCII characters to be ignored, and sets the default dictionary to a value appropriate for
the machines in the CS lab. You are free to add other options for your game (e.g., you might
allow proper nouns or contractions). Be sure to comment what options your game
has in your code.
The presence of the default values makes it easy to create a default instance of hangman:
hangman = Hangman ( ) # Use t h e d e f a u l t v a l u e s .
hangman . pla y ( ) # Loop u n t i l t h e p l a y e r no l o n g e r wan ts t o p l a y .
Besides init (), the only other required method is play(). This is the method the
player will call to play the game. Once a game is completed, play() should include a
prompt asking whether the player wants to play the game again. If so, a new game is
started; otherwise play() exits.
You are otherwise free to include any methods you need. For this assignment you may
ignore information hiding and make all your methods and class variables publicly accessible.
