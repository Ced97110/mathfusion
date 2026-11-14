import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
P = [('0 et 6', r'$0K$'), ('2 et 8', r'$2K$'), ('4 et 10', r'$4K$')]
W3 = 26; gap = (W - 4 - 3 * W3) / 2
bx = box(ax, 2, 8, 84, 12, 'resultat')
text(ax, 44, 14, r'$H$ = 0, 2, 4, 6, 8, 10', 'resultat', 'm')
for i, (s, c) in enumerate(P):
    x = 2 + i * (W3 + gap)
    box(ax, x, 36, W3, 11, 'sujet', label=s, size='s')
    text(ax, x + W3 / 2, 52, c, 'sujet', 's')
    arrow(ax, (x + W3 / 2, 36), (x + W3 / 2, 20.5), 'varie')
text(ax, 44, 61, r'paquets $hK$ de $h$ dans $H$', 'sujet', 's')
text(ax, 44, 28, 'réunion', 'varie', 's', ha='center')
save(fig, '48-100')
