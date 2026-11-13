import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
s, g = 5.6, 0.6
x0, y0 = 12, 8
for k in range(16):
    gi, gj = k % 4, 3 - k // 4
    bx = x0 + gi * 17; by = y0 + gj * 15
    for p in range(4):
        on = (k >> p) & 1
        box(ax, bx + (p % 2) * (s + g), by + (p // 2) * (s + g), s, s, 'sujet' if on else 'fixe', fill=bool(on), dash=not on, lw=0.6, r=0.5)
text(ax, 44, 74, '16 parties de 4 positions', 'sujet', 'm')
text(ax, 2.5, y0 + 3 * 15 + 6, 'vide', 'fixe', 's', ha='left')
text(ax, 86, y0 + 6, 'toutes', 'sujet', 's', ha='right')
text(ax, 44, 3, 'chaque partie : un circuit', 'resultat', 'm')
save(fig, '80-194')
