import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ox, oy = 44, 36
line(ax, [(6, oy), (82, oy)], 'sujet', lw=2.2)
line(ax, [(ox, 6), (ox, 66)], 'autre', lw=2.2)
text(ax, 70, oy + 4.5, r'$M_1$ : $(x,\,0)$', 'sujet', 's')
text(ax, ox + 3, 62, r'$M_2$ : $(0,\,y)$', 'autre', 's', ha='left')
disc(ax, ox, oy, 2.2, 'resultat')
text(ax, ox - 4, oy - 5.5, '(0, 0)', 'resultat', 's', ha='right')
text(ax, 44, 2.5, r'$M_1\cap M_2=\{0\}$', 'resultat', 'm')
save(fig, '58-058')
