print("""Welcome to this little game : The diffrent paths of the little Mermaid.
\tI hope you enjoy it :) - Made by Nicole Sager\n""")
URName = input("But bevore we begin this adventure. What's your name?\n->")
MeanGirl = input("Also please write a name for a lovely girl\n->")
contin = """
----------------------------------------------------
Press any key to continue.
----------------------------------------------------\n
"""
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

print(f"""Once upon a time . . . in a splendid palace on the bed of the bluest ocean, lived a little Mermaid.
{URName}, the youngest and loveliest of them all, had a beautiful voice, 
and when she sang, the fishes flocked from all over the sea to listen to her. 
The shells gaped wide, showing their pearls and even the jellyfish stopped to listen. 
The young mermaid often sang, and each time, she would gaze upwards, 
seeking the faint sunlight that scarcely managed to filter down into the depths.
""")
input(contin)
print("""However the young mermaid always wanted to live above water. 
This came to be because everytime she went to the surface she saw a handsome and kind prince.
After quite some time she had to admit that she had secretly fallen in love with him.
But to be with him she had to become a human. To get some help she startet to sing 
and when she was surrounded by her fish friends she asked for their help.
One of them told and warnd her about the Seawitch.
----------------------------------------------------""")


# dec --> decision
def decFirst():
    seawitch = input(f"""Should {URName} go to the Seawitch? 
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

decFirst()

def chapterOne():

