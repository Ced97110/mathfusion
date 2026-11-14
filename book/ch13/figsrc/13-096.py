import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 20, 44, 'avec soustraction', 'fixe', 's'); text(ax, 68, 44, 'addition seulement', 'resultat', 's')
box(ax, 3, 24, 34, 14, 'fixe', dash=True, label=r'$a - b = c - d$')
box(ax, 51, 24, 34, 14, 'resultat', label=r'$a + d = b + c$')
arrow(ax, (38, 31), (50, 31), 'varie', both=True)
text(ax, 44, 15, 'on ajoute b et d partout', 'varie', 's')
text(ax, 44, 6, 'même écart, deux écritures', 'encre', 's')
save(fig, '13-096')
