import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, r'Groupe $\{1,\,2,\,4\}$ dans ℤ/7 : valeurs de $a^e$', 'sujet', 's')
cols = [1, 2, 4]
cx = [40, 58, 76]
text(ax, 10, 66, r'$a$ =', 'sujet', 'm')
for x, a in zip(cx, cols):
    text(ax, x, 66, str(a), 'sujet', 'm', weight='bold')
for r, e in enumerate([1, 2, 3]):
    y = 46 - r * 16 + 6
    text(ax, 10, y + 4, rf'$e={e}$', 'varie', 'm')
    for x, a in zip(cx, cols):
        v = pow(a, e, 7)
        box(ax, x - 7, y, 14, 9, 'resultat' if v == 1 else 'limite', label=str(v), size='m')
text(ax, 44, 8, r'$e=3$ : le plus petit pour tous', 'resultat', 's')
save(fig, '54-264')
