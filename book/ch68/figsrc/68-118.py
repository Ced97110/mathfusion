import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 47, r'3 lignes : $2^3 = 8$ colonnes', 'sujet', 'm')
for k in range(8):
    x = 5 + 20 * (k % 4); y = 28 - 14 * (k // 4) + 4
    w = format(k, '03b')
    box(ax, x, y, 18, 9, 'limite' if k == 0 else 'sujet', label=w, dash=(k == 0), fill=(k != 0))
text(ax, 44, 8, 'sans la nulle (000) : 7', 'resultat', 'm')
save(fig, '68-118')
