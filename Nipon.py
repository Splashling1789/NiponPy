"""Nipon.py - A simple flashcard utility for learning Japanease kanas 0.1"""

import random
import os
from platform import system
roma = [['a','i','u','e','o'],['ka','ki','ku','ke','ko'],['sa','shi','su','se','so'],['ta','chi','tsu','te','to'],['na','ni','nu','ne','no'],['ha','hi','fu','he','ho'], ['ma','mi','mu','me','mo'],['ya','yu','yo'],['ra','ri','ru','re','ro'],['wa','wo','n'],['ga','gi','gu','ge','go'],['za','ji','zu','ze','zo'],['da','di','du','de','do'],['ba','bi','bu','be','bo'],['pa','pi','pu','pe','po'],['kya','kyu','kyo'],['sha','shu','sho'],['cha','chu','cho'],['nya','nyu','nyo'],['hya','hyu','hyo'],['mya','myu','myo'],['rya','ryu','ryo'],['gya','gyu','gyo'],['ja','ju','jo'],['bya','byu','byo'],['pya','pyu','pyo']]
hira = [['あ','い','う','え','お'],['か','き','く','け','こ'],['さ','し','す','せ','そ'],['た','ち','つ','て','と'],['な','に','ぬ','ね','の'],['は','ひ','ふ','へ','ほ'], ['ま','み','む','め','も'],['や','ゆ','よ'],['ら','り','る','れ','ろ'],['わ','を','ん'],['が','ぎ','ぐ','げ','ご'],['ざ','じ','ず','ぜ','ぞ'],['だ','ぢ','づ','で','ど'],['ば','び','ぶ','べ','ぼ'],['ぱ','ぴ','ぷ','ぺ','ぽ'],['きゃ','きゅ','きょ'],['しゃ','しゅ','しょ'],['ちゃ','ちゅ','ちょ'],['にゃ','にゅ','にょ'],['ひゃ','ひゅ','ひょ'],['みゃ','みゅ','みょ'],['りゃ','りゅ','りょ'],['ぎゃ','ぎゅ','ぎょ'],['じゃ','じゅ','じょ'],['びゃ','びゅ','びょ'],['ぴゃ','ぴゅ','ぴょ']]
kata = [['ア','イ','ウ','エ','オ'],['カ','キ','ク','ケ','コ'],['サ','シ','ス','セ','ソ'],['タ','チ','ツ','テ','ト'],['ナ','ニ','ヌ','ネ','ノ'],['ハ','ヒ','フ','ヘ','ホ'], ['マ','ミ','ム','メ','モ'],['ヤ','ユ','ヨ'],['ラ','リ','ル','レ','ロ'],['ワ','ヲ','ン'],['ガ','ギ','グ','ゲ','ゴ'],['ザ','ジ','ズ','ゼ','ゾ'],['ダ','ヂ','ヅ','デ','ド'],['バ','ビ','ブ','ベ','ボ'],['パ','ピ','プ','ペ','ポ'],['キャ','キュ','キョ'],['シャ','シュ','ショ'],['チャ','チュ','チョ'],['ニャ','ニュ','ニョ'],['ヒャ','ヒュ','ヒョ'],['ミャ','ミュ','ミョ'],['リャ','リュ','リョ'],['ギャ','ギュ','ギョ'],['ジャ','ジュ','ギョ'],['ビャ','ビュ','ビョ'],['ピャ','ピュ','ピョ']]
sets= roma + hira + kata



"""
? The first lines of code I typed could be used for another version
while True:
    #0-9 regular kana. 10-14 subsonic. 15-25 yoon.
    limit = random.randint(0, 3)
    candidate= hira
    kana = candidate[limit][random.randint(0,len(candidate[limit])-1)]
    input(kana)
"""

def menu():
    global sets
    cls()
    e=input("Welcome to Nipon.py! How would you like to start? \n1.Select your kanas (all by default)\n2.Show kanas\n3. Random printing\n[else]. About")
    if(e=="1"):
        configure()
        menu()
    elif(e=="2"):
        show()
    elif(e=="3"):
        times = int(input("How many times do you want to have something printed? "))
        if(sets == []):
            sets += roma
            sets+= hira
            sets += kata
        rndprint(times)
    else:
        input("\nCreated by Javier Albero (Splashling)\nGithub: https://github.com/Splashling1789")
        menu()


def configure():
    global sets
    sets= []
    cls()
    print("This will ask you the range of the kanas you want to add to your set.\n0: nothing\n1: a i u e o\n2: ka ki ku ke ko\n...\n11.ga gi gu ge go\n...\n26.pya pyu pyo")
    rm=input("Select your romanji range (from): ")
    rm= int(rm)
    if rm>0 and rm<27:
        rM=input("Select your romanji range (to): ")
        rM=int(rM)
        if (rM > 26):
            rM =26
    else:
        print("Configured empty")
    
    hm=input("Select your hiragana range (from): ")
    hm=int(hm)
    
    if hm>0 and hm<27:
        hM=input("Select your hiragana range (to): ")
        hM=int(hM)
        if (hM > 26):
            hM=26
    else:
        print("Configured empty")
    
    km=input("Select your katakana range (from): ")
    km=int(km)
    if km>0 and km<27:
        kM=input("Select your katakana range (to): ")
        kM=int(kM)
        if (kM > 26):
            kM=26
    else:
        print("Configured empty")
    

    
    if(rm >0):
        for i in range(rm, rM+1):
            sets += [roma[i-1]]

    if(hm >0):
        for i in range(hm, hM+1):
            sets += [hira[i-1]]

    if(km>0):
        for i in range(km, kM+1):
            sets += [kata[i-1]]
    input()
def rndprint(times):
    cls()
    for i in range(times):
        sel= random.randint(0, len(sets)-1)
        kana = sets[sel][random.randint(0,len(sets[sel])-1)]
        input(kana)
    input("And that was the last one. Good job!")
    menu()

def show():
    global sets
    for o in sets:
        for k in o:
            if(len(o) == 3 and o in roma):
                print (k + "     ",end="")
            elif(len(o)==5 and o in roma):
                print(k + " ", end="")
            elif(len(o)== 3 and (o in kata or o in hira)):
                print(k + "   ", end="")
                if (len(k)==1):
                    print(" ", end="")
            elif(len(o)== 5 and (o in kata or o in hira)):
                print(k, end="")
            

            print(" " * (3-len(k)), end="")

        print("\n", end="")
    input()
    menu()

def cls():
    if(os.name== "posix"):
        os.system("clear")
    if(os.name=="nt"):
        os.system("cls")

if system() == "Windows":
    e=input("I have detected your OS is Windows. Would you like to change the characters code to the Japanese set? (y/n)")
    if e == "y":
        os.system("chcp 932")
        print("\n")
    else:
        print("The character code will be left as it is.\n")

menu()