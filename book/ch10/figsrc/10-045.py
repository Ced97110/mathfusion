import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
f = numberline(ax, 6, 80, 36, 0, 100, 10, labels=False, arrow_right=False)
c = f(50)
for v, y, up in ((20, 41, True), (12, 45, True), (95, 31, False), (98, 27, False)):
    disc(ax, f(v), 36, 1.0, 'sujet'); line(ax, [(f(v), 36), (f(v), y)], 'fixe', dash=True)
    d = abs(v - 50); sg = '+' if up else '−'
    if up:
        arrow(ax, (f(v), y), (c - 1.5, y), 'varie', lw=0.9); text(ax, f(v) - 1.5, y, str(v), 'sujet', 's', ha='right')
    else:
        arrow(ax, (f(v), y), (c + 1.5, y), 'varie', lw=0.9); text(ax, f(v) + 1.5, y, str(v), 'sujet', 's', ha='left')
    text(ax, (f(v) + c) / 2 + (2 if up else -2), y + 2.2, sg + str(d), 'varie', 's')
disc(ax, c, 36, 1.8, 'varie')
line(ax, [(c, 34), (c, 22)], 'varie', dash=True); text(ax, c, 20, 'c = 50', 'varie', 'm')
text(ax, 44, 12, '+ : le nombre monte jusqu\'à 50', 'varie', 's')
text(ax, 44, 8, '− : le nombre descend jusqu\'à 50', 'varie', 's')
box(ax, 8, 54, 36, 8, 'varie', label=r'estimé 4 $\times$ 50 = 200', size='s')
box(ax, 46, 54, 36, 8, 'resultat', label='vrai 12+20+95+98 = 225', size='s')
text(ax, 44, 68, 'les nombres sont loin de 50', 'encre', 'm')
save(fig, '10-045')
