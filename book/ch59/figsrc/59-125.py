import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(76)
cx, cy, R = 22, 40, 14
for k in range(20):
    a = math.radians(90 - 18 * k)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 1.5, 'sujet')
for i in range(2):
    for j in range(10):
        disc(ax, 62 + 9 * i, 40 + (j - 4.5) * 4.2, 1.5, 'autre')
text(ax, cx, 63, 'ℤ/20', 'sujet', 'm', weight='bold')
text(ax, 66.5, 63, 'ℤ/2 ⊕ ℤ/10', 'autre', 'm', weight='bold')
text(ax, cx, 18, '20 éléments', 'sujet', 's')
text(ax, 66.5, 18, '20 éléments', 'autre', 's')
text(ax, 44, 40, '?', 'fixe', 'xl', weight='bold')
text(ax, 44, 6, 'est-ce le même module ?', 'fixe', 's')
save(fig, '59-125')
