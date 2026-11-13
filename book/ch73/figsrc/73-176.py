import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
s = 66 / 480; x0 = 3
bars = [(54, 480, 'fixe', 'GL₂ : 480'), (33, 120, 'sujet', '120'), (12, 60, 'resultat', '60')]
for y, n, r, l in bars:
    box(ax, x0, y, n * s, 9, r, label=l, size='s')
text(ax, x0 + 120 * s + 2.5, 37.5, 'SL₂', 'sujet', 's', ha='left')
text(ax, x0 + 60 * s + 2.5, 16.5, 'PSL₂', 'resultat', 's', ha='left')
arrow(ax, (10, 53.5), (10, 42.8), 'varie'); arrow(ax, (10, 32.5), (10, 21.8), 'varie')
text(ax, 14, 48, r'$\div\,(q-1)=\div\,4$', 'varie', 's', ha='left')
text(ax, 14, 27, 'puis ÷ pgcd de 2 et 4 = ÷ 2', 'varie', 's', ha='left')
text(ax, 14, 3.5, 'pgcd : plus grand diviseur commun', 'fixe', 's', ha='left')
save(fig, '73-176')
