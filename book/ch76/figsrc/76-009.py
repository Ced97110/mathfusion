import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
items = ['3 devant un produit ?', 'de 12 cm² à 60 cm² ?', 'prix du café : 3 € ?']
subs = ['les tableaux', 'la surface', 'le café']
for i, (t, s) in enumerate(zip(items, subs)):
    y = 56 - i * 22
    box(ax, 3, y - 7, 36, 14, 'fixe', label=t, size='s')
    arrow(ax, (40, y), (50, 38 + (y - 38) * 0.45), 'varie', lw=0.9)
    text(ax, 21, y - 10.5, s, 'fixe', 's')
box(ax, 51, 24, 34, 28, 'sujet', label='un seul objet :\nalgèbre\nextérieure', size='m')
save(fig, '76-009')
