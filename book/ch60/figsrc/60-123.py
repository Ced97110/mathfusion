import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
cx, cy, R = 44, 54, 22
two = {3, 6, 9}
three = {4, 8}
for h in range(12):
    a = math.radians(90 - 30 * h)
    x, y = cx + R * math.cos(a), cy + R * math.sin(a)
    if h == 0:
        disc(ax, x, y, 4.6, 'autre', fill=False, lw=0.9)
        disc(ax, x, y, 3.4, 'sujet', label='0', size='s')
    elif h in two:
        disc(ax, x, y, 3.4, 'sujet', label=str(h), size='s')
    elif h in three:
        disc(ax, x, y, 3.4, 'autre', label=str(h), size='s')
    else:
        disc(ax, x, y, 3.4, 'fixe', label=str(h), size='s')
disc(ax, 9, 17, 2.4, 'sujet'); text(ax, 14, 17, 'composante de 2 : 0, 3, 6, 9', 'sujet', 's', ha='left')
disc(ax, 9, 8, 2.4, 'autre'); text(ax, 14, 8, 'composante de 3 : 0, 4, 8', 'autre', 's', ha='left')
text(ax, cx, cy, 'ℤ/12', 'fixe', 'm')
save(fig, '60-123')
