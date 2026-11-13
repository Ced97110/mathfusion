import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
xs = [13, 33, 53, 73]; s = 12
labs = ['1', r'$r$', r'$r^2$', r'$r^3$']; acts = ['rien', '¼ tour', '½ tour', '¾ tour']
for k, x in enumerate(xs):
    a = 90 * k; c = math.cos(math.radians(a)); sn = math.sin(math.radians(a))
    P = lambda dx, dy: (x + dx * c - dy * sn, 28 + dx * sn + dy * c)
    poly(ax, [P(-s/2, -s/2), P(s/2, -s/2), P(s/2, s/2), P(-s/2, s/2)], 'sujet')
    px, py = P(-s/2 + 2.4, s/2 - 2.4); disc(ax, px, py, 1.7, 'varie')
    text(ax, x, 47, labs[k], 'sujet', 'l'); text(ax, x, 15, acts[k], 'fixe', 's')
    line(ax, [(x, 44.5), (x, 36)], 'fixe', lw=0.6, dash=True)
text(ax, 4, 57, r'$R_4$ = {', 'sujet', 'l', ha='left'); text(ax, 84, 57, '}', 'sujet', 'l', ha='right')
brace(ax, 4, 82, 10, 'sujet', depth=1.6)
text(ax, 44, 3.5, r'$R$ : rotations, 4 : côtés', 'sujet', 's')
save(fig, '44-134')
