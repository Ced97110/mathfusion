import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(86)
o = (44, 40); u = 11
poly(ax, [iso(-1.4, -1.4, 0, o, u), iso(1.4, -1.4, 0, o, u), iso(1.4, 1.4, 0, o, u), iso(-1.4, 1.4, 0, o, u)], 'fixe')
arrow(ax, iso(0, 0, 0, o, u), iso(1.9, 0, 0, o, u), 'sujet', lw=1.3)
arrow(ax, iso(0, 0, 0, o, u), iso(0, 1.9, 0, o, u), 'sujet', lw=1.3)
arrow(ax, iso(0, 0, 0, o, u), iso(0, 0, 3.0, o, u), 'resultat', lw=2.6)
text(ax, 2, 83, r'$V$ : tout l’espace, 3 axes', 'sujet', 's', ha='left')
q = iso(0, 0, 1.6, o, u)
text(ax, q[0] + 3, q[1], r'$(0\ ;\ 0\ ;\ 1)$', 'resultat', 'm', ha='left')
q2 = iso(0, 0, 3.0, o, u)
text(ax, q2[0], q2[1] + 5, r'$\mathrm{rad}\ V=V^{\perp}$', 'resultat', 'l')
text(ax, 44, 17, 'rad V : orthogonal à tous', 'resultat', 's')
text(ax, 44, 11.5, 'les vecteurs de V', 'resultat', 's')
text(ax, 44, 4.5, 'la mesure ignore le 3e nombre', 'fixe', 's')
save(fig, '72-083')
