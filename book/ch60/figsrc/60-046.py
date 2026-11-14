import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx, cy, R = 24, 29, 18
text(ax, 44, 60, r'$M_2$ : les heures y avec 4 y = 0', 'sujet', 'm')
for n in range(12):
    a = math.radians(90 - 30 * n)
    x, y = cx + R * math.cos(a), cy + R * math.sin(a)
    if n in (0, 3, 6, 9):
        disc(ax, x, y, 3.2, 'sujet', label=str(n), size='s')
    elif n == 1:
        disc(ax, x, y, 3.2, 'limite', label='1', size='s')
    else:
        disc(ax, x, y, 2.0, 'fixe')
text(ax, 52, 44, '4 × 3 = 12 = 0', 'sujet', 'm', ha='left')
text(ax, 52, 36, '4 × 6 = 24 = 0', 'sujet', 'm', ha='left')
text(ax, 52, 28, '4 × 9 = 36 = 0', 'sujet', 'm', ha='left')
text(ax, 52, 16, '4 × 1 = 4 ≠ 0', 'limite', 'm', ha='left')
save(fig, '60-046')
