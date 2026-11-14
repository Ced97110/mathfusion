import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def edge(ax, p, q, r=0.0, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def nd(ax, p, l, role='fixe', r=3.4):
    disc(ax, p[0], p[1], r, role, label=l)
fig, ax = canvas(96)
box(ax, 2, 80, 28, 12, 'sujet', label='distributif', size='s')
box(ax, 58, 80, 28, 12, 'resultat', label='modulaire', size='s')
arrow(ax, (31, 86), (57, 86), 'resultat', lw=1.3)
text(ax, 44, 91, r'$D$ donne $M$', 'resultat', 's')
line(ax, [(2, 74), (86, 74)], 'fixe', dash=True)
text(ax, 2, 69, "sans l'hypothèse :", 'limite', 's', ha='left')
P = {'0': (26, 12), 'b': (14, 28), 'c': (14, 46), 'a': (38, 34), '1': (26, 60)}
for a, b in [('0','b'),('c','1'),('0','a'),('a','1')]: edge(ax, P[a], P[b], 3.4)
edge(ax, P['b'], P['c'], 3.4, 'varie', 1.6)
for k, p in P.items(): nd(ax, p, '$'+k+'$', 'sujet' if k in 'bc' else ('autre' if k == 'a' else 'fixe'))
text(ax, 0.5, 37, r'$b \leq c$', 'varie', 's', ha='left')
box(ax, 46, 42, 40, 17, 'resultat', label='$c \\wedge (b \\vee a)$\n$= c \\wedge 1 = c$')
box(ax, 46, 14, 40, 17, 'limite', label='$b \\vee (c \\wedge a)$\n$= b \\vee 0 = b$')
text(ax, 66, 36.5, r'$c \neq b$ : $M$ échoue', 'limite', 's')
save(fig, '79-127')
