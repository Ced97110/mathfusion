import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
pts = {'i': (44, 58), 'j': (68, 20), 'k': (20, 20)}
role = {'i': 'sujet', 'j': 'varie', 'k': 'resultat'}
for n, (x, y) in pts.items(): disc(ax, x, y, 5.5, role[n], label=r'$%s$' % n, size='l')
def link(a, b, lab, pos, ha):
    (x0, y0), (x1, y1) = pts[a], pts[b]
    d = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / d, (y1 - y0) / d
    arrow(ax, (x0 + ux * 6.5, y0 + uy * 6.5), (x1 - ux * 6.5, y1 - uy * 6.5), 'varie', lw=1.3)
    text(ax, pos[0], pos[1], lab, 'encre', 's', ha=ha)
link('i', 'j', r'$i \times j = k$', (62, 44), 'left')
link('j', 'k', r'$j \times k = i$', (44, 12), 'center')
link('k', 'i', r'$k \times i = j$', (26, 44), 'right')
text(ax, 44, 28, 'sens inverse : −', 'limite', 's')
save(fig, '78-023')
