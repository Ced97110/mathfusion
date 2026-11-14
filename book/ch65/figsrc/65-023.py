import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# G : trois automorphismes de E
box(ax, 2, 10, 28, 50, 'autre')
text(ax, 16, 64, r'$G$ : sur $E$', 'autre', 's')
labs = ['1', r'$\sigma$', r'$\sigma^2$']
ys = [48, 35, 22]
for lab, y in zip(labs, ys):
    disc(ax, 16, y, 4.5, 'autre', label=lab, size='m')
# S_3 : six rangements, trois viennent de G
box(ax, 48, 10, 38, 50, 'fixe')
text(ax, 67, 64, r'$S_3$ : 6 rangements', 'fixe', 's')
pos = [(57, 48), (77, 48), (57, 35), (77, 35), (57, 22), (77, 22)]
inside = [0, 2, 4]
for k, (x, y) in enumerate(pos):
    disc(ax, x, y, 4.5, 'sujet' if k in inside else 'fixe')
for y, (x, yy) in zip(ys, [pos[0], pos[2], pos[4]]):
    arrow(ax, (20.5, y), (x - 4.8, yy), 'varie')
text(ax, 67, 14, r'$G_f$ : 3 rangements', 'sujet', 's')
text(ax, 38, 4, 'chaque élément donne un rangement', 'varie', 's')
save(fig, '65-023')
