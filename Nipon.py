"""Nipon.py - A simple flashcard utility for learning Japanease kanas"""
import random
roma = [['a','i','u','e','o'],['ka','ki','ku','ke','ko'],['sa','shi','su','se','so'],['ta','chi','tsu','te','to'],['na','ni','nu','ne','no'],['ha','hi','fu','he','ho'], ['ma','mi','mu','me','mo'],['ya','yu','yo'],['ra','ri','ru','re','ro'],['wa','wo','n']]
hira = [['あ','い','う','え','お'],['か','き','く','け','こ'],['さ','し','す','せ','そ'],['た','ち','つ','て','と'],['な','に','ぬ','ね','の'],['は','ひ','ふ','へ','ほ'], ['ま','み','む','め','も'],['や','ゆ','よ'],['ら','り','る','れ','ろ'],['わ','を','ん']]
while True:
    limit = random.randint(0, 9)
    candidate= hira
    kana = candidate[limit][random.randint(0,len(candidate[limit])-1)]
    input(kana)
    