import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 53, 'commutateur $=e$ si $ab=ba$', 'encre', 'l')
for k, (cx, role, head, sign, res) in enumerate([(23, 'resultat', 'deux rotations', '=', r'commutateur $=e$'),
                                                  (65, 'limite', 'rotation et réflexion', r'$\neq$', r'commutateur $\neq e$')]):
    box(ax, cx - 20.5, 6, 41, 40, role, fill=False, lw=1.0)
    text(ax, cx, 41, head, role, 's')
    box(ax, cx - 16, 22, 12, 10, 'sujet', label=r'$ab$')
    box(ax, cx + 4, 22, 12, 10, 'autre', label=r'$ba$')
    text(ax, cx, 27, sign, role, 'xl')
    text(ax, cx, 13, res, role, 's')
save(fig, '50-210')
