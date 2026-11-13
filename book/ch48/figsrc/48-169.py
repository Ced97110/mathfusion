import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 87, r'$G$ : 7 éléments', 'sujet', 'm')
def row(y, packets, t_ker, t_res, n_res):
    text(ax, 44, y + 20, t_ker, 'varie', 's')
    i = 0
    for size in packets:
        w = size * 8.4 + (size - 1) * 0.0
        x = 14.6 + i * 8.4
        box(ax, x, y + 6, w - 0.8, 9, 'sujet', fill=True)
        i += size
    text(ax, 44, y - 2, t_res, 'resultat', 's')
    for k in range(n_res):
        disc(ax, 44 + (k - (n_res - 1) / 2) * 6, y - 9, 2.2, 'resultat')
row(56, [1] * 7, r'noyau : 1 élément', r'image : $7 \div 1 = 7$ éléments', 7)
row(18, [7], r'noyau : 7 éléments', r'image : $7 \div 7 = 1$ élément', 1)
save(fig, '48-169')
