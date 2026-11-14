import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
ox, oy, s = 8, 10, 12.0
Pt = lambda x, y: (ox + x * s, oy + y * s)
line(ax, [(ox - 4, oy), (ox + 6.4 * s, oy)], 'fixe', lw=0.6)
line(ax, [(ox, oy - 3), (ox, oy + 3.6 * s)], 'fixe', lw=0.6)
for y in (1, 3):
    line(ax, [Pt(0, y), Pt(6.2, y)], 'fixe', lw=0.5, dash=True)
# (1;0) ne bouge pas
disc(ax, *Pt(1, 0), 2.0, 'fixe')
text(ax, Pt(1, 0)[0], Pt(1, 0)[1] - 5, '(1 ; 0) reste', 'fixe', 's')
# (0;1) -> (1;1)
disc(ax, *Pt(0, 1), 2.0, 'sujet'); disc(ax, *Pt(1, 1), 2.0, 'resultat')
arrow(ax, (Pt(0, 1)[0] + 2.4, Pt(0, 1)[1]), (Pt(1, 1)[0] - 2.4, Pt(1, 1)[1]), 'varie', lw=1.2)
text(ax, Pt(1.9, 1)[0], Pt(1, 1)[1] + 3.2, '(0;1) ↦ (1;1)', 'encre', 's')
# (2;3) -> (5;3)
disc(ax, *Pt(2, 3), 2.0, 'sujet'); disc(ax, *Pt(5, 3), 2.0, 'resultat')
arrow(ax, (Pt(2, 3)[0] + 2.4, Pt(2, 3)[1]), (Pt(5, 3)[0] - 2.4, Pt(5, 3)[1]), 'varie', lw=1.2)
text(ax, Pt(3.5, 3)[0], Pt(3, 3)[1] + 3.5, '(2;3) ↦ (5;3)', 'encre', 's')
text(ax, 44, 61, r'$S(x\,;\,y)=(x+y\,;\,y)$', 'encre', 'm')
text(ax, 58, 23, 'décalage = y', 'varie', 's')
text(ax, 58, 19, 'la hauteur ne change pas', 'fixe', 's')
save(fig, '57-199')
