import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
cols = [(16, '16', '$c=\\frac{1}{4}$', '1'), (4, '4', '$c=\\frac{1}{2}$', '1'), (-9, '−9', '$c=\\frac{1}{3}$', '−1')]
for i, (v, b, c, r) in enumerate(cols):
    x = 4 + i * 28
    box(ax, x, 38, 24, 11, 'sujet', label=b, size='l')
    arrow(ax, (x + 12, 38), (x + 12, 17), 'varie')
    text(ax, x + 12, 28, c, 'varie', 's')
    box(ax, x, 6, 24, 11, 'resultat', label=r, size='l')
save(fig, '71-184')
