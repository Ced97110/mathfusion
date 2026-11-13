import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = numberline(ax, 6, 80, 34, 0.30, 0.40, step=0.02, arrow_right=False)
for v, role, lab, y in [(2/6, 'sujet', 'n = 3\n2/6 ≈ 0,333', 50), (9/24, 'autre', 'n = 4\n9/24 = 0,375', 50)]:
    line(ax, [(f(v), 34), (f(v), y - 4)], role, dash=True); disc(ax, f(v), 34, 1.8, role); text(ax, f(v), y, lab, role, 's')
line(ax, [(f(0.368), 34), (f(0.368), 20)], 'resultat', dash=True); disc(ax, f(0.368), 34, 1.8, 'resultat', fill=False)
text(ax, f(0.368), 15, '1/e ≈ 0,368', 'resultat', 's')
text(ax, 44, 61, 'proportion de dérangements', 'fixe', 's')
save(fig, '80-378')
