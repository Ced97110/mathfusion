import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(44)
ox, oy, k = 12, 8, 10
Pt = lambda x, y: (ox + k * x, oy + k * y)
line(ax, [Pt(-0.5, 0), Pt(4.2, 0)], 'fixe', 0.5); line(ax, [Pt(0, -0.4), Pt(0, 3.1)], 'fixe', 0.5)
disc(ax, *Pt(1, 0), 1.1, 'sujet'); disc(ax, *Pt(0, 1), 1.1, 'varie'); disc(ax, *Pt(3, 2), 1.1, 'resultat')
arrow(ax, Pt(0.9, 0.1), Pt(0.1, 0.9), 'varie', 1.0, curve=-0.3)
arrow(ax, Pt(0.15, 1.05), Pt(2.85, 1.95), 'varie', 1.0)
text(ax, 24, 4, r'$v = (1, 0)$', 'sujet', 's', ha='left')
text(ax, 14, 24, r'$Av = (0, 1)$', 'varie', 's', ha='left')
text(ax, 44, 39, r'$Av + x = (3, 2)$', 'resultat', 's')
text(ax, 32, 17, r'$+\,x$', 'varie', 's')
text(ax, 70, 14, r'$v \mapsto Av + x$', 'encre', 'm')
save(fig, '73-144')
