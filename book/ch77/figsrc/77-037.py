import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, cx, cy, v, role="sujet", cw=8, ch=6, size="m", roles=None):
    for r in range(2):
        for c in range(2):
            text(ax, cx + (c - 0.5) * cw, cy + (0.5 - r) * ch, v[r][c], roles[r][c] if roles else role, size)
    for s, e in ((cx - cw, 1.6), (cx + cw, -1.6)):
        line(ax, [(s + e, cy + ch), (s, cy + ch), (s, cy - ch), (s + e, cy - ch)], role)

fig, ax = canvas(72)
mat(ax, 18, 50, [['2', '$-1$'], ['1', '2']], 'sujet', 8)
text(ax, 18, 62, r'$\rho(a)$', 'sujet')
arrow(ax, (31, 50), (54, 50), 'varie')
mat(ax, 69, 50, [[r'$\lambda-2$', '1'], ['$-1$', r'$\lambda-2$']], 'varie', 11)
text(ax, 69, 62, r'$\lambda 1-\rho(a)$', 'varie')
arrow(ax, (69, 40), (69, 23), 'resultat')
text(ax, 76, 32, 'det', 'resultat', 's')
box(ax, 10, 6, 68, 16, 'resultat', label=r'$f_a(\lambda)=\lambda^2-4\lambda+5$')
save(fig, '77-037')
