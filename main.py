import itertools
import random
import sys
import os
import platform
from os import system
import string
import random
import sys
import os
import subprocess
import operator


def get_response_system(mot_passe):
    cmd = "fitness.exe 2 " + mot_passe
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
    out1 = output.split()
    out1 = out1[1].decode().split("'")
    return  ''.join(out1)



characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','6','7','8','9','0']
e_characher = ['_']





char_options= characters+numbers+e_characher


population = {}

def generate_population( num_indiv ):
    for i in range(num_indiv):
        mot_passe = []
        j=0
        for j in range(10):
            mot_passe.append( char_options[random.randint(0,len(char_options)-1)])
        mot = ''.join(mot_passe)
        result = get_response_system(mot)
        population.__setitem__(mot,result)



def gen_select (number_select ):
    for i in population:
        print(i +" : "+ str(population.get(i)))















