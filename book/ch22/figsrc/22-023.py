import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
rows = [('1,414', 'approché', 'fixe'), ('1,41421356', 'approché', 'fixe'), (r'$\sqrt{2}$', 'exact', 'resultat')]
for i, (v, t, r) in enumerate(rows):
    y = 44 - i * 14
    box(ax, 6, y, 40, 10, r, label=v, size='l')
    text(ax, 66, y + 5, t, r, 'm')
    arrow(ax, (47, y + 5), (56, y + 5), r) if False else None
box(ax, 14, 2, 60, 9, 'resultat', label=r'$\sqrt{2}\times\sqrt{2} = 2$')
save(fig, '22-023')
