#coding: utf-8
import os
import random
import sys

def get_platform():
	platforms = {
		'linux1' : 'Linux',
		'linux2' : 'Linux',
		'darwin' : 'OS X',
		'win32' : 'Windows'
	}
	if sys.platform not in platforms:
		return sys.platform
	return platforms[sys.platform]


def clear_console(opSys):
    if opSys == 'Linux':
        os.system('clear')
    else
        os.system('cls')



def alea_tableau(*n):
	tableau = []
	try:
		n = int(n[0])
		taille = n
		for i in range(taille):
			tableau.append(random.randint(-999, 1000))
		tableau.append(max(tableau)+(random.randint(0, 413)))
		return tableau
	except:
		taille = random.randint(1, 1000)
		for i in range(taille):
			tableau.append(random.randint(-999, 1000))
		tableau.append(max(tableau)+(random.randint(0, 413)))
		return tableau

def tabDisplay(datTab):
	theTab = datTab
	print ""
	for i in theTab:
		if i is theTab[0]:
			print "["+str(i)+",",
			continue
		if i is theTab[len(theTab)-1]:
			print str(i)+"]"
			break
		print str(i)+",",



clear_console()







