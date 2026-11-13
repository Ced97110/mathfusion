import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
PW, G, X0, Y = 15, 1.6, 11.6, 44
for i in range(4):
    x = X0 + i * (PW + G)
    role = 'resultat' if i == 0 else 'varie'
    box(ax, x, Y, PW, 8, role)
    ax.plot([x + PW / 2] * 2, [Y + 1.2, Y + 6.8], color=COL[role], lw=0.6, zorder=3)
brace(ax, X0, X0 + 4 * PW + 3 * G, Y + 8, 'sujet', label=r'$|G|=8$', down=False)
text(ax, X0 + PW / 2, Y - 4, r'$|C|=2$', 'resultat', 's')
brace(ax, X0 + PW + G, X0 + 4 * PW + 3 * G, Y - 1, 'varie', label=r'indices $2+2+2=6$')
box(ax, 9, 8, 70, 11, 'resultat', label=r'$|C|=8-6=2$ : multiple de $2$', size='s')
save(fig, '50-124')
