import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ds = [(2, r'$\sqrt{2}$'), (4, r'$\sqrt[4]{2}$'), (8, r'$\sqrt[8]{2}$')]
for i, (d, n) in enumerate(ds):
    x = 8 + i * 22; h = d * 4.5
    box(ax, x, 12, 16, h, 'resultat', label=str(d), size='m')
    text(ax, x + 8, 7, n, 'encre', 'm')
text(ax, 77, 12 + 18, '…', 'varie', 'xl')
arrow(ax, (77, 36), (77, 56), 'varie', lw=1.2)
text(ax, 44, 66, 'degré de chaque élément', 'encre', 's')
text(ax, 30, 61, 'chacun : un polynôme', 'resultat', 's'); text(ax, 76, 60, 'sans borne', 'varie', 's')
save(fig, '61-119')
