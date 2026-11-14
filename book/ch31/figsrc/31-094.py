import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
R = 30; O = (42, 37)
line(ax, [(O[0] + R * math.cos(a / 100 * 2 * math.pi), O[1] + R * math.sin(a / 100 * 2 * math.pi)) for a in range(101)], 'fixe', lw=1.0)
line(ax, [(O[0] - R - 2, O[1]), (O[0] + R + 2, O[1])], 'fixe', lw=0.7)
cx = O[0] + 0.6 * R; sy = 0.8 * R
P1 = (cx, O[1] + sy); P2 = (cx, O[1] - sy)
line(ax, [O, P1], 'fixe', lw=1.0); line(ax, [O, P2], 'fixe', lw=1.0)
line(ax, [(cx, O[1]), P1], 'resultat', lw=2.2); line(ax, [(cx, O[1]), P2], 'resultat', lw=2.2)
line(ax, [O, (cx, O[1])], 'sujet', lw=2.2)
disc(ax, *P1, 1.6, 'sujet'); disc(ax, *P2, 1.6, 'sujet')
arrow(ax, (cx + 6, O[1] + 4), (cx + 6, O[1] - 4), 'varie', both=True) if False else None
text(ax, O[0] + 0.3 * R, O[1] + 3, '0,6', 'sujet', 's')
text(ax, cx + 2.5, O[1] + sy / 2 + 3, '+0,8', 'resultat', 's', ha='left')
text(ax, cx + 2.5, O[1] - sy / 2 - 3, '−0,8', 'resultat', 's', ha='left')
text(ax, O[0] + 0.3 * R - 3, O[1] + sy / 2 + 1.5, '1', 'fixe', 's')
text(ax, O[0] + 0.3 * R - 3, O[1] - sy / 2 - 1.5, '1', 'fixe', 's')
text(ax, 44, 4, 'deux points symétriques, même 0,6', 'varie', 'm')
save(fig, '31-094')
