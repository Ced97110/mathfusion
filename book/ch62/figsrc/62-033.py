import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 22, 58, '(i) seule', 'encre', 'm')
text(ax, 66, 58, '(i) et (ii)', 'encre', 'm')
line(ax, [(44, 6), (44, 62)], 'fixe', lw=0.6, dash=True)
for i, nm in enumerate(['ℚ(√2)', 'ℝ', 'ℂ']):
    y = 38 - i * 15
    box(ax, 4, y, 36, 11, 'resultat', label=f'{nm} convient', size='s')
    role = 'resultat' if i == 0 else 'limite'
    box(ax, 48, y, 36, 11, role, label=f'{nm} ' + ('convient' if i == 0 else 'exclu'), size='s')
text(ax, 22, 4, 'trop de corps', 'resultat', 's')
text(ax, 66, 4, 'le plus petit seul', 'resultat', 's')
save(fig, '62-033')
