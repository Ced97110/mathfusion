import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# le signe découpé : parenthèses + générateur
text(ax, 26, 66, r'$($', 'varie', 'xl')
box(ax, 32, 59, 14, 14, 'sujet', label=r'$6$', size='xl')
text(ax, 52, 66, r'$)$', 'varie', 'xl')
text(ax, 22, 51, 'parenthèses :', 'varie', 's', ha='center')
text(ax, 22, 46, 'tous les multiples', 'varie', 's', ha='center')
text(ax, 65, 51, 'générateur :', 'sujet', 's', ha='center')
text(ax, 65, 46, 'le nombre 6', 'sujet', 's', ha='center')
# liste des multiples
f = numberline(ax, 6, 76, 28, -12, 12, step=6, arrow_right=False, size='s')
for v in range(-12, 13, 6):
    disc(ax, f(v), 28, 1.8, 'sujet')
text(ax, 44, 36, r'$(6)=\{\ldots,-12,-6,0,6,12,\ldots\}$', 'sujet', 's')
text(ax, 44, 12, r'$(x^2)$ contient $x^2q$ pour tout $q$', 'autre', 's')
text(ax, 44, 5, 'une infinité d’éléments, un seul signe', 'fixe', 's')
save(fig, '54-174')
