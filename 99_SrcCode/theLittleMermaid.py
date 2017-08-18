# Many pretty Imports
# No but for real in theses Files is the bulk of the Text
# In hindsight this is mor of a boo adventure than a Text adventure
from Story import FirstChapter
from Story import SecondChapter
from Story import ThirdChapter
from Story import Endings
print("""Welcome to this little game : The diffrent paths of the little Mermaid.
\tI hope you enjoy it :) - Made by Nicole Sager\n""")
contin = """
----------------------------------------------------
Press any key to continue.
----------------------------------------------------\n
"""
# this is ASCII Art - pretty isn't it?
#                   Thats a knife VVV
print("""
----------------------------------------------------
                       __
        0      _o8o_o888888oo     /|           0
                 o88888888 ,|    / |
        \`.    /| `o88'88o _/    \_|
         \ `-.' |     __) \___   ,||
          `-. .-'    /         \ [_/    0
            | \     / /  _) _)\ Y /         
            |  \    \ \)  . (  \_/
  0         |   \    '/'- _-'\\       0  0
            \    `-._/       |
             \     _/       /           0
              \            /        0
               `-..___..-'                  0
----------------------------------------------------\n
""")
def loop(y):
    # Here we made a loop function with the loopfunction we can loop thoug the Text arrays
    for x in y:
        print(x)    
        # the contin input hase the sole purpose to make the reedinexerience easier
        input(contin)
    print(f"""----------------------------------------------------""")

# StoryF = FirstChapter.first()

input(contin)
loop(FirstChapter.first())


# dec --> decision
def decFirst():
    # First we ask the Question and with the given Value (0 or 1) we choose
    # If something else is given by the user the function is called again and agin until the user either gies us a correct Value
    seawitch = input(f"""Should She go to the Seawitch? 
    type 0 for no and 1 for yes\n->""")
    if(seawitch == '0'):
        print("""She decided it wasn't worth the risk asking her for she might hurt the prince.
        Therfore hartbreaking she let go of him. Over time her heart mended and she found a lovely merman.
        Still... even years later she sometimes looks to the surface and wonders what if?
------------------------The End----------------------""")
        pass
    elif (seawitch == '1'):
        chapterOne()
    else:
        print("No cheating!! Try agin.")
        decFirst()

def decSecond():    
    # First we ask the Question and with the given Value (0 or 1) we choose
    # If something else is given by the user the function is called again and agin until the user either gies us a correct Value
    seawitch = input(f"""Should She push the Princess to her doom? 
    type 0 for no and 1 for yes\n->""")
    if(seawitch == '0'):
        print("""'Oh my goodness what was I thinking?' The littel mermaid Asked herself in horror. 
The Prince soon returned but he wasnt carying any wood, no he was carrying a bouqet of red roses.
As soon as he was befor the Princess he knelt down and proposed, sumultainiously but not heard
by anyone but her the little mermaids heart broke.
        """)
        chapterTreeVOne()
    
    elif (seawitch == '1'):
        print("""The little mermaid looked one last time at the Princess took a step that hurt like hell
to stand behind her and pushed. The little mermaid thaught her ears must be bleeding the cry the princess
made was so grusome. She looked behind her as she saw the prince running in her direction. A bouqet of roses 
laid on the ground. The Prince cried her name but no awnser came. He sank to his knees, trembling, 
and then he told the little Mermaid that he had originallyy planned to propose to the lovely princess.
        """)
        chapterTreeVTwo()

    else:
        print("No cheating!! Try agin.")
        decSecond()

def decThirdVO():
    # First we ask the Question and with the given Value (0 or 1) we choose
    # If something else is given by the user the function is called again and agin until the user either gies us a correct Value
    seawitch = input(f"""Should She kill the Prince? 
    type 0 for no and 1 for yes\n->""")
    if(seawitch == '0'):
        loop(Endings.SecondEnd())
        pass
    elif (seawitch == '1'):
        loop(Endings.ThirdEnd())
        pass
        
    else:
        print("No cheating!! Try agin.")
        decThirdVO()

def decThirdVT():
    # First we ask the Question and with the given Value (0 or 1) we choose
    # If something else is given by the user the function is called again and agin until the user either gies us a correct Value
    seawitch = input(f"""Should She kill the Prince? 
    type 0 for no and 1 for yes\n->""")
    if(seawitch == '0'):
        loop(Endings.FifthEnd())
        pass
    elif (seawitch == '1'):
        loop(Endings.FourthEnd())
        pass
        
    else:
        print("No cheating!! Try agin.")
        decThirdVT()


def chapterOne():
    # Here We loop with the loopfunction trough the Text array that contains the bulk of the Story
    loop(SecondChapter.second())
    decSecond()

def chapterTreeVOne():
    # Here We loop with the loopfunction trough the Text array that contains the bulk of the Story
    loop(ThirdChapter.thirdVO())
    decThirdVO()

def chapterTreeVTwo():
    # Here We loop with the loopfunction trough the Text array that contains the bulk of the Story
    loop(ThirdChapter.thirdVT())
    decThirdVT()


decFirst()