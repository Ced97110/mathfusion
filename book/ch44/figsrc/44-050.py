import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def edge(p, q, r=4.8):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy)
    return (p[0]+dx/d*r, p[1]+dy/d*r), (q[0]-dx/d*r, q[1]-dy/d*r)
fig, ax = canvas(66)
xs = [20, 44, 68]; ny = {1: 38, 2: 24}
text(ax, 44, 59, r'α ∘ α = $1_S$', 'encre', 'l')
for c, x in enumerate(xs):
    for n in (1, 2):
        disc(ax, x, ny[n], 4, 'resultat' if c == 2 else ('sujet' if c == 0 else 'fixe'), label=str(n))
for s in (0, 1):
    for n in (1, 2):
        m = 3 - n
        p, q = edge((xs[s], ny[n]), (xs[s+1], ny[m]))
        arrow(ax, p, q, 'varie' if n == 1 else 'autre', lw=1.1)
    text(ax, (xs[s]+xs[s+1])/2, 47, 'α : échange', 'fixe', 's')
text(ax, 44, 10, 'tout revient en place', 'resultat', 'm')
save(fig, '44-050')
