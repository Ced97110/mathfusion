import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = lambda v: 24 + (v - 370000) / 30000 * 56
y = 34
line(ax, [(f(370000), y), (f(400000), y)], 'fixe')
disc(ax, f(374100), y, 1.4, 'varie'); disc(ax, f(375492), y, 1.4, 'sujet')
line(ax, [(f(400000), y - 1.5), (f(400000), y + 1.5)], 'fixe')
text(ax, f(374100) - 2, y + 12, 'estimé 374 100', 'varie', 's', ha='right')
text(ax, f(375492) + 1, y + 12, 'vrai 375 492', 'sujet', 's', ha='left')
text(ax, 82, y + 7, 'limite 400 000', 'fixe', 's', ha='right') if False else None
brace(ax, f(374100), f(375492), y - 3, 'varie', 'erreur 1 392', down=True)
brace(ax, f(375492), f(400000), y + 3, 'fixe', 'marge 25 900', down=False)
text(ax, f(400000), y - 5, 'limite 400 000', 'fixe', 's', ha='right')
text(ax, 44, 7, r'erreur $\ll$ marge : on s’arrête', 'resultat', 'm')
save(fig, '10-089')
