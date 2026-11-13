import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = lambda v: 6 + (v + 8) / 20 * 74
for v in range(-8, 12, 4):
    line(ax, [(f(v) + 3.0, 54), (f(v + 4) - 3.0, 54)], 'fixe')
    for u in range(v + 1, v + 4): ax.plot([f(u)] * 2, [52.8, 55.2], color=COL['fixe'], lw=0.8)
for v in range(-8, 13):
    if v % 4 == 0:
        disc(ax, f(v), 54, 3.0, 'sujet', label=str(v).replace('-', '−'), size='s')
text(ax, 40, 40, r'$4$', 'sujet', 'xl'); text(ax, 48, 40, r'$\mathbb{Z}$', 'varie', 'xl')
arrow(ax, (39, 35), (24, 27), 'sujet'); arrow(ax, (49, 35), (60, 27), 'varie')
text(ax, 22, 21, 'le nombre\nqu’on multiplie', 'sujet', 's')
text(ax, 58, 21, 'les entiers\npar lesquels on multiplie', 'varie', 's')
text(ax, 44, 8, r'$12\in4\mathbb{Z}$ : 12 est un multiple de 4', 'resultat', 's')
save(fig, '52-027')
