import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(100)
text(ax, 44, 95, '+2 à chaque pas, dans ℤ', 'varie', 's', weight='bold')
f = numberline(ax, 8, 72, 82, 0, 8, 1, labels=False, arrow_right=True, tick=0.8)
for v in range(0, 9, 2):
    disc(ax, f(v), 82, 1.8, 'sujet'); text(ax, f(v), 76, str(v), 'sujet', 's')
for v in (0, 2, 4, 6):
    arrow(ax, (f(v), 85), (f(v + 2), 85), 'varie', curve=-0.5, lw=0.8)
text(ax, 44, 68, 'noyau {0} : ⟨2⟩ ≅ ℤ', 'resultat', 's', weight='bold')
text(ax, 44, 55, '+3 dans l’horloge à 12', 'varie', 's', weight='bold')
c, r = (44, 30), 15
for k in range(12):
    a = math.pi / 2 - 2 * math.pi * k / 12; x, y = c[0] + r * math.cos(a), c[1] + r * math.sin(a)
    on = k % 3 == 0
    disc(ax, x, y, 2.6 if on else 1.2, 'varie' if on else 'fixe', label=str(k) if on else None, size='s')
text(ax, 44, 30, 'revient à 0\nen 4 pas', 'varie', 's')
text(ax, 44, 6, 'le noyau contient 4 : pas ≅ ℤ', 'varie', 's')
save(fig, '48-190')
