from tqdm import tqdm
from time import sleep

def lower (word):
    sleep (1)
    print (f" Processing {word}")
    return word. lower()

words=[ "Hugo" "Estrada", "S."]

[lower (w) for w in tqdm (words) ]