import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
c = (44, 46); R = 30
pol = lambda r, a: (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
line(ax, [pol(R+2, 90), pol(R+2, -90)], 'fixe', dash=True)
line(ax, [pol(R+2, 45), pol(R+2, 225)], 'fixe', dash=True)
text(ax, 44, 82, 'axe 90°', 'fixe', 's')
text(ax, pol(R+3, 45)[0]+1, pol(R+3, 45)[1]+3, 'axe 45°', 'fixe', 's', ha='left')
for a, role in [(30, 'sujet'), (150, 'varie'), (-60, 'resultat')]:
    line(ax, [c, pol(R, a)], role, lw=1.2); disc(ax, *pol(R, a), 1.7, role)
text(ax, *pol(R+6, 30), '30°', 'sujet', 's')
text(ax, *pol(R+6, 150), '150°', 'varie', 's')
text(ax, *pol(R+6, -60), '-60°', 'resultat', 's')
arrow(ax, pol(R-3, 30)[:1]+(pol(R, 30)[1]-2,), (pol(R, 150)[0]+2, pol(R, 150)[1]-2), 'varie', lw=1.2)
arrow(ax, (pol(R, 150)[0]+1, pol(R, 150)[1]-2), (pol(R, -60)[0]-1, pol(R, -60)[1]+2), 'varie', lw=1.2)
text(ax, 44, pol(R, 30)[1]+3, 'pli 1', 'varie', 's')
text(ax, 25, 33, 'pli 2', 'varie', 's')
arcp = [pol(13, a) for a in range(30, -61, -3)]
line(ax, arcp[:-2], 'resultat', lw=1.6); arrow(ax, arcp[-3], arcp[-1], 'resultat', lw=1.6)
text(ax, pol(20, -15)[0], pol(20, -15)[1], '-90°', 'resultat', 's')
text(ax, 44, 4, r'$2\times(45-90)=-90°$', 'resultat', 'm')
save(fig, '74-112')
