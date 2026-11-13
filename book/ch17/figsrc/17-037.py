import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, role, full=True, r=1.7):
    ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role] if full else FILL['encre'], lw=1.0, zorder=4))

fig, ax = canvas(72)
heads = (r'$a<b$', r'$a=b$', r'$a\leq b$'); xs = (36, 54)
for x, h in zip(xs, heads[:2]): text(ax, x, 62, h, 'sujet', 'm')
text(ax, 77, 62, heads[2], 'sujet', 'm')
rows = ((46, r'$2$ et $3$', True, False), (30, r'$3$ et $3$', False, True), (14, r'$4$ et $3$', False, False))
for y, lab, p, q in rows:
    text(ax, 13, y, lab, 'encre', 'm')
    for x, ok in zip(xs, (p, q)):
        if ok: dot(ax, x, y, 'resultat', r=2.6)
        else: line(ax, [(x - 2, y - 2), (x + 2, y + 2)], 'limite', lw=1.3); line(ax, [(x - 2, y + 2), (x + 2, y - 2)], 'limite', lw=1.3)
    res = p or q
    box(ax, 68, y - 5, 18, 10, 'resultat' if res else 'limite', label='oui' if res else 'non')
text(ax, 45, 62, 'ou', 'varie', 's')
save(fig, '17-037')
