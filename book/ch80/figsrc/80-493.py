import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cop = [1, 7, 11, 13, 17, 19, 23, 29]
f = numberline(ax, 6, 82, 26, 1, 30, labels=False, arrow_right=False, tick=0.8)
for v in range(1, 31):
    if v in cop:
        disc(ax, f(v), 26, 1.5, 'resultat'); text(ax, f(v), 31, str(v), 'resultat', 's')
    else: disc(ax, f(v), 26, 0.9, 'fixe')
text(ax, f(30), 21, '30', 'fixe', 's')
text(ax, 44, 46, '8 entiers sans facteur\ncommun avec 30', 'resultat', 'm')
text(ax, 44, 9, '30 − 15 − 10 − 6\n+ 5 + 3 + 2 − 1 = 8', 'sujet', 'm')
save(fig, '80-493')
