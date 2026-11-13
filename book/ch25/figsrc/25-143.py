import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
s70, s60, s50 = (math.sin(math.radians(v)) for v in (70, 60, 50))
Bp = (4, 14); Cp = (4 + 40, 14); d = 40 * s50 / s70
Ap = (Bp[0] + d * math.cos(math.radians(60)), Bp[1] + d * s60)
poly(ax, [Bp, Cp, Ap], 'limite', lw=1.1)
text(ax, Ap[0], Ap[1] - 5, '70°', 'limite', 's'); text(ax, Bp[0] + 6, 17.5, '60°', 'limite', 's'); text(ax, Cp[0] - 6, 17.5, '50°', 'limite', 's')
text(ax, 24, 8, 'aucun angle droit', 'limite', 's')
poly(ax, [(54, 14), (82, 14), (82, 40)], 'resultat', lw=1.1)
line(ax, [(82, 18), (78, 18), (78, 14)], 'resultat', lw=0.8)
text(ax, 66, 8, 'un angle droit', 'resultat', 's')
text(ax, 62, 30, 'hypoténuse', 'resultat', 's', rot=43)
text(ax, 25, 49, 'tan : seulement ici', 'resultat', 's', ha='left') if False else None
text(ax, 66, 47, r'$\tan$ : ici', 'resultat', 's'); text(ax, 24, 47, r'$\tan$ : pas tel quel', 'limite', 's')
save(fig, '25-143')
