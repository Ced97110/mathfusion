import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
line(ax, [(44, 10), (44, 68)], 'fixe', dash=True)
text(ax, 44, 6, 'miroir', 'fixe', 's')
text(ax, 20, 78, 'D2 (à droite)', 'autre', 's', weight='bold'); text(ax, 68, 78, 'D1 (à gauche)', 'sujet', 's', weight='bold')
arrow(ax, (33, 78), (55, 78), 'varie', lw=1.4, both=True)
text(ax, 44, 72.5, 'on échange', 'varie', 's')
L = [r'$0\cdot a=(0+0)\cdot a$', r'$=0\cdot a+0\cdot a$', r'on retranche $0\cdot a$', r'$0\cdot a=0$']
R = [r'$a\cdot 0=a\cdot(0+0)$', r'$=a\cdot 0+a\cdot 0$', r'on retranche $a\cdot 0$', r'$a\cdot 0=0$']
for i in range(4):
    y = 61 - i*14
    role = 'resultat' if i == 3 else ('fixe' if i == 2 else None)
    box(ax, 1.5, y - 6, 38, 12, role or 'autre', label=L[i], size='s')
    box(ax, 48.5, y - 6, 38, 12, role or 'sujet', label=R[i], size='s')
    if i < 3:
        arrow(ax, (20.5, y - 6.2), (20.5, y - 7.8), 'fixe', lw=0.8); arrow(ax, (67.5, y - 6.2), (67.5, y - 7.8), 'fixe', lw=0.8)
save(fig, '51-198')
