import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, r'polygone à $p$ côtés', 'fixe', 's')
text(ax, 7, 41, r'$p$', 'sujet'); text(ax, 7, 19, r'$p-1$', 'encre')
for i, p in enumerate([5, 7, 11, 13, 17]):
    x = 16 + i * 14; d = p - 1; ok = (d & (d - 1)) == 0
    box(ax, x, 36, 12.5, 10, 'sujet', label=str(p))
    box(ax, x, 14, 12.5, 10, 'resultat' if ok else 'limite', label=str(d))
    arrow(ax, (x + 6.25, 36), (x + 6.25, 25), 'varie')
text(ax, 2, 6, 'vert : puissance de 2', 'resultat', 's', ha='left')
text(ax, 46, 6, 'rouge : pas puissance de 2', 'limite', 's', ha='left')
save(fig, '61-196')
