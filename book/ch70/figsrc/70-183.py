import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u, oy = 6, 26
def axes(cx):
    line(ax, [(cx - 18, oy), (cx + 18, oy)], 'fixe', lw=0.7); line(ax, [(cx, oy - 18), (cx, oy + 18)], 'fixe', lw=0.7)
axes(22); axes(66)
text(ax, 22, 56, r'$b=0,\ c=1$ : $x^2+y^2$', 'resultat', 's', weight='bold')
disc(ax, 22, oy, 1.3, 'resultat'); text(ax, 17.5, oy - 3.2, '0', 'resultat', 's')
disc(ax, 22 + u, oy, 1.3, 'sujet'); text(ax, 22 + u + 3, oy - 3, '1', 'sujet', 's')
disc(ax, 22 + u, oy + u, 1.3, 'sujet'); text(ax, 22 + u + 3, oy + u + 2.5, '2', 'sujet', 's')
text(ax, 22, 5, 'nul seulement en O', 'resultat', 's')
text(ax, 66, 56, r'$b=2,\ c=1$ : $x^2+2xy+y^2$', 'limite', 's', weight='bold')
line(ax, [(66 - 18, oy + 18), (66 + 18, oy - 18)], 'limite', lw=1.5)
disc(ax, 66 + u, oy - u, 1.4, 'limite'); text(ax, 66 + u + 3, oy - u - 3, '0', 'limite', 's')
text(ax, 66, 5, 'nul aussi en (1 ; −1)', 'limite', 's')
save(fig, '70-183')
