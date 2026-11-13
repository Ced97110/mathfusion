import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, 'S = les nombres pairs', 'sujet', 'm')
f = numberline(ax, 6, 76, 56, 0, 7)
for v in range(8):
    if v % 2 == 0: disc(ax, f(v), 62, 3.4, 'sujet')
    elif v != 1: disc(ax, f(v), 62, 1.2, 'fixe')
    else: disc(ax, f(v), 62, 3.4, 'limite', fill=False, lw=1.2)
text(ax, f(1), 69, 'manque', 'limite', 's')
box(ax, 6, 28, 76, 9, 'resultat', label='différence de deux pairs : paire', size='s')
box(ax, 6, 17, 76, 9, 'resultat', label='produit de deux pairs : pair', size='s')
box(ax, 6, 6, 76, 9, 'limite', label='1 est dans S ? non', size='s')
save(fig, '51-088')
