import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
c = (22, 33); h = 14
poly(ax, [(c[0]-h, c[1]-h), (c[0]+h, c[1]-h), (c[0]+h, c[1]+h), (c[0]-h, c[1]+h)], 'sujet')
for a in (0, 45, 90, 135):
    t = math.radians(a); d = 19
    line(ax, [(c[0]-d*math.cos(t), c[1]-d*math.sin(t)), (c[0]+d*math.cos(t), c[1]+d*math.sin(t))], 'varie', dash=True)
text(ax, c[0], c[1], r'$X$', 'sujet', 'l')
text(ax, c[0], 8, 'carré', 'sujet', 's')
box(ax, 50, 40, 36, 12, 'varie', label='4 rotations', size='m')
box(ax, 50, 22, 36, 12, 'varie', label='4 réflexions', size='m')
arrow(ax, (68, 20), (68, 15), 'resultat')
box(ax, 44, 3, 42, 11, 'resultat', label=r'Sym($X$) : 8 éléments', size='s')
save(fig, '74-098')
