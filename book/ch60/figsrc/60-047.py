import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx, cy, R = 24, 29, 18
text(ax, 44, 60, r'$M_3$ : les heures y avec 3 y = 0', 'sujet', 'm')
for n in range(12):
    a = math.radians(90 - 30 * n)
    x, y = cx + R * math.cos(a), cy + R * math.sin(a)
    if n == 0:
        disc(ax, x, y, 4.2, 'autre', fill=False)
        disc(ax, x, y, 3.2, 'sujet', label='0', size='s')
    elif n in (4, 8):
        disc(ax, x, y, 3.2, 'sujet', label=str(n), size='s')
    elif n in (3, 6, 9):
        disc(ax, x, y, 3.2, 'autre', label=str(n), size='s')
    elif n == 2:
        disc(ax, x, y, 3.2, 'limite', label='2', size='s')
    else:
        disc(ax, x, y, 2.0, 'fixe')
text(ax, 52, 46, '3 × 4 = 12 = 0', 'sujet', 'm', ha='left')
text(ax, 52, 38, '3 × 8 = 24 = 0', 'sujet', 'm', ha='left')
text(ax, 52, 30, '3 × 2 = 6 ≠ 0', 'limite', 'm', ha='left')
text(ax, 52, 18, r'$M_2$ : 0, 3, 6, 9', 'autre', 'm', ha='left')
text(ax, 52, 11, 'en commun : seul 0', 'autre', 's', ha='left')
save(fig, '60-047')
