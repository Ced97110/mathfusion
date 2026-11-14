import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for i in range(8):
    box(ax, 4 + i * 6, 46, 5, 8, 'sujet')
for i in range(5):
    box(ax, 4 + i * 6, 34, 5, 8, 'autre')
text(ax, 66, 50, '$a$ = 8', 'sujet', 'm')
text(ax, 66, 38, '$b$ = 5', 'autre', 'm')
box(ax, 4, 14, 36, 11, 'resultat', label='8 > 5 : vrai')
box(ax, 46, 14, 36, 11, 'limite', label='5 > 8 : faux')
text(ax, 22, 8, 'gauche plus grand', 'resultat', 's')
text(ax, 64, 8, 'gauche plus petit', 'limite', 's')
save(fig, '12-032')
