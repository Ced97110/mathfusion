import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
o = (12, 8); s = 15
p = lambda a, b: (o[0] + a * s, o[1] + b * s)
arrow(ax, p(0, 0), p(3.3, 0), 'fixe', lw=0.8); arrow(ax, p(0, 0), p(0, 3.3), 'fixe', lw=0.8)
th = [math.radians(a) for a in range(0, 91, 3)]
r = math.sqrt(5)
line(ax, [p(r * math.cos(t), r * math.sin(t)) for t in th], 'fixe', dash=True)
arrow(ax, p(0, 0), p(1, 2), 'sujet', lw=1.6)
arrow(ax, p(0, 0), p(2, 1), 'autre', lw=1.6)
disc(ax, *p(1, 2), 1.2, 'sujet'); disc(ax, *p(2, 1), 1.2, 'autre')
text(ax, p(1, 2)[0] + 2.5, p(1, 2)[1] + 3, r'$1 + 2i$', 'sujet', 'm', ha='left')
text(ax, p(2, 1)[0] + 3, p(2, 1)[1] + 1, r'$2 + i$', 'autre', 'm', ha='left')
text(ax, 63, 3, 'réel', 'fixe', 's')
text(ax, 5, 56, 'imaginaire', 'fixe', 's', ha='left')
text(ax, p(1.7, 1.7)[0] + 4, p(1.7, 1.7)[1] + 9, r'distance $\sqrt{5}$ pour les deux', 'fixe', 's', ha='left') if False else None
text(ax, 62, 44, r'même distance $\sqrt{5}$', 'fixe', 's')
text(ax, p(1.3, 1.3)[0], p(1.3, 1.3)[1], '?', 'limite', 'xl', weight='bold')
text(ax, 66, 17, 'on ne peut pas dire', 'encre', 's')
text(ax, 66, 12, 'lequel est le plus grand', 'encre', 's')
save(fig, '78-027')
