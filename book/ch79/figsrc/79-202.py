import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
ys = [8, 24, 40, 56]
for i in range(3):
    line(ax, [(30, ys[i] + 3.6), (30, ys[i + 1] - 3.6)], 'fixe')
for y, n in zip(ys, [1, 2, 4, 8]):
    disc(ax, 30, y, 3.6, 'sujet' if n in (2, 8) else 'fixe', label=str(n), size='s')
text(ax, 40, 56, r'$\sup(2,8)=8$' + '\n' + 'le plus grand', 'resultat', 's', ha='left')
text(ax, 40, 24, r'$\inf(2,8)=2$' + '\n' + 'le plus petit', 'resultat', 's', ha='left')
save(fig, '79-202')
