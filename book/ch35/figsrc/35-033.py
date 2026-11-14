import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 51, 47, 'à 45°', 'encre', 'm'); text(ax, 75, 47, 'à 0°', 'encre', 'm')
rows = [(r'$3\sin x+4\cos x$', 'sujet', 28), (r'$4\sin x+3\cos x$', 'autre', 14)]
vals = [('≈ 4,95', '4'), ('≈ 4,95', '3')]
for (lab, role, y), (v1, v2) in zip(rows, vals):
    box(ax, 2, y, 36, 11, role, label=lab, size='s')
    box(ax, 40, y, 22, 11, 'resultat', label=v1, size='s')
    box(ax, 64, y, 22, 11, 'limite', label=v2, size='s')
text(ax, 51, 8, 'égales', 'resultat', 's'); text(ax, 75, 8, 'différentes', 'limite', 's')
text(ax, 20, 8, 'pourtant 3 ≠ 4', 'limite', 's')
save(fig, '35-033')
