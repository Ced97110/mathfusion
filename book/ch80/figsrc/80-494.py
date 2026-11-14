import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cols = [(15, 8, '8', 'entiers sans\nfacteur commun\navec 30'), (44, 2, '2', 'façons de\nredistribuer\n3 chapeaux'), (73, 3, '3', 'polynômes\nirréductibles\ndegré 4 modulo 2')]
for cx, n, t, lab in cols:
    box(ax, cx - 13, 22, 26, 44, 'fixe', fill=False)
    text(ax, cx, 58, t, 'sujet', 'xl', weight='bold')
    for i in range(n):
        disc(ax, cx + ((i % 4) - (min(n, 4) - 1) / 2) * 4.5, 47 - (i // 4) * 4.5, 1.6, 'sujet')
    text(ax, cx, 29, lab, 'encre', 's')
    arrow(ax, (cx, 21), (cx, 16.5), 'varie')
box(ax, 8, 4, 72, 11, 'varie', label='un outil : défaire une somme')
save(fig, '80-494')
