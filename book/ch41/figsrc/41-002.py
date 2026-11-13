import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Droite des vitesses au sol, de 0 à 300 km/h. Écarts : 280 - 245,8 = 34,2 ; 245,8 - 80 = 165,8.
fig, ax = canvas(62)
f = numberline(ax, 6, 80, 22, 0, 300, 50)
for v, role, lab, ty, ha, tx in [(80, 'limite', 'soustraire : 80', 50, 'center', f(80)),
                                 (245.8, 'resultat', 'le livre : 245,8', 40, 'center', f(245.8) - 4),
                                 (280, 'limite', 'additionner : 280', 50, 'right', 85)]:
    disc(ax, f(v), 22, 1.5, role)
    line(ax, [(f(v), 23.5), (f(v), ty - 2.5)], role, lw=0.7, dash=True)
    text(ax, tx, ty, lab, role, 's', ha=ha)
brace(ax, f(80), f(245.8), 12, 'fixe', label='écart 165,8')
brace(ax, f(245.8), f(280), 12, 'fixe', label='34')
text(ax, 44, 58, 'vent à 60° de l’est', 'encre', 'm')
save(fig, '41-002')
