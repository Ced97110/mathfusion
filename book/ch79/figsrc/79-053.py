import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def E(ax, p, q, r=3.4, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def N(ax, x, y, s, role='sujet', r=3.4, size='m'):
    disc(ax, x, y, r, role, label=s, size=size)

fig, ax = canvas(92)
def row(y, sizes, roles):
    x = 7.4; spans = []
    for n, role in zip(sizes, roles):
        x0 = x
        for i in range(n):
            box(ax, x, y, 5, 5, role); x += 5.8
        spans.append((x0, x - 0.8)); x += 2.2
    return spans
for (x0, x1) in row(72, (4, 4, 4), ('sujet',) * 3): brace(ax, x0, x1, 70.5, 'sujet', label='4')
box(ax, 14, 52, 60, 9, 'resultat', label=r'$4\mid12$ : $12=4\times3$')
sp = row(36, (5, 5, 2), ('sujet', 'sujet', 'limite'))
brace(ax, *sp[0], 34.5, 'sujet', label='5'); brace(ax, *sp[1], 34.5, 'sujet', label='5')
brace(ax, *sp[2], 34.5, 'limite', label='reste 2')
box(ax, 14, 14, 60, 9, 'limite', label=r'$5\nmid12$ : il reste 2')
save(fig, '79-053')
