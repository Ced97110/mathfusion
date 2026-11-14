import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
box(ax, 14, 4, 60, 62, 'fixe', label=None)
text(ax, 20, 61, r'$V$', 'fixe', 'l')
o = (44, 35)
line(ax, [(o[0] - 26, o[1] - 13), (o[0] + 26, o[1] + 13)], 'sujet', lw=1.6)
line(ax, [(o[0] + 13, o[1] - 26), (o[0] - 13, o[1] + 26)], 'resultat', lw=1.6)
text(ax, 68, 46, r'$U$', 'sujet', 'l'); text(ax, 30, 61, r'$U^\perp$', 'resultat', 'l')
text(ax, 70, 30, 'droite de flèches', 'sujet', 's', ha='right')
text(ax, 70, 11, r'orthogonales à $U$', 'resultat', 's', ha='right')
save(fig, '71-140')
