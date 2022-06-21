"""Nipon.py - A simple flashcard utility for learning Japanease kanas"""
import random
spell = [['a','i','u','e','o'],['ka','ki','ku','ke','ko'],['sa','shi','su','se','so'],['ta','chi','tsu','te','to'],['na','ni','nu','ne','no'],['ha','hi','fu','he','ho'], ['ma','mi','mu','me','mo'],['ya','yu','yo'],['ra','ri','ru','re','ro'],['wa','wo','n']]

while True:
    limit = random.randint(0, 6)
    kana = spell[limit][random.randint(0,len(spell[limit])-1)]
    input(kana)
    