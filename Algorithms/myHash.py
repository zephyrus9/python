# -*-coding: utf-8 -*-
# Author: 


voted = {}
def check_voter(name):
    if voted.get(name):
        print('Kick ' + name + ' out')
    else:
        voted[name] = True
        print("let them vote!")


check_voter('tom')
check_voter('jane')
check_voter('tom')