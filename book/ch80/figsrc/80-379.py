import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 52, '2 couleurs : 2 coloriages', 'resultat', 'm')
for r, cols in enumerate([('sujet', 'varie', 'sujet'), ('varie', 'sujet', 'varie')]):
    for i, (L, c) in enumerate(zip('ABC', cols)):
        box(ax, 8 + i * 22, 28 - r * 18, 22, 12, c, label=f'{L} : ' + ('bleu' if c == 'sujet' else 'rouge'), size='m')
text(ax, 44, 4, 'A touche B, B touche C', 'fixe', 's')
save(fig, '80-379')
