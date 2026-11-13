import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 60, 'pourquoi ces signes ?', 'varie', 'm')
terms = ['30', '− 15', '− 10', '− 6', '+ 5', '+ 3', '+ 2', '− 1']
for i, t in enumerate(terms):
    r = 'sujet' if i == 0 else ('resultat' if t.startswith('+') else 'fixe')
    box(ax, 3 + (i % 4) * 21.5, 44 - (i // 4) * 13, 19, 9, r, label=t)
text(ax, 44, 25, '= 8', 'resultat', 'l', weight='bold')
arrow(ax, (44, 21), (44, 16), 'varie')
box(ax, 6, 3, 76, 12, 'autre', label='signes donnés par la\nfonction de Möbius')
save(fig, '80-497')
