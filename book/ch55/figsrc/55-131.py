import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
import itertools
sq = lambda n: str(n)

def panel(top, roots, role, delta_role, title):
    """One panel: roots on a line, squared differences of the 3 pairs, their product."""
    text(ax, 44, top, title, role, 'm', weight='bold')
    f = numberline(ax, 14, 70, top - 9, 1, 5, arrow_right=False)
    seen = {}
    for r in roots:
        k = seen.get(r, 0); seen[r] = k + 1
        disc(ax, f(r), top - 9 + 3.4 * k, 1.4, role)
    pairs = list(itertools.combinations(range(3), 2))
    vals = [(roots[i] - roots[j]) ** 2 for i, j in pairs]
    for n, ((i, j), v) in enumerate(zip(pairs, vals)):
        bx = 3 + n * 28.5
        lab = rf'$({roots[i]}-{roots[j]})^2={v}$'
        box(ax, bx, top - 31, 26, 8, 'varie' if v == 0 else 'fixe', label=lab, size='s')
    prod = vals[0] * vals[1] * vals[2]
    box(ax, 22, top - 45, 44, 9, delta_role, label=rf'$\Delta={vals[0]}\times{vals[1]}\times{vals[2]}={prod}$', size='m')
    return prod

p1 = panel(98, (2, 3, 4), 'sujet', 'sujet', 'racines 2, 3, 4')
p2 = panel(46, (2, 2, 3), 'autre', 'varie', 'racines 2, 2, 3')
assert p1 == 4 and p2 == 0
line(ax, [(3, 50), (85, 50)], 'fixe', lw=0.5, dash=True)
text(ax, 77, 88, r'$\neq 0$', 'sujet', 'm')
text(ax, 77, 36, r'$=0$', 'varie', 'm')
save(fig, '55-131')
