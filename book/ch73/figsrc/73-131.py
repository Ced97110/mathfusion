import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
P = [(4, 1), (14, 1), (4, 8)]
rot = lambda p: (-p[1], p[0]); mir = lambda p: (-p[0], p[1])
for cx, f, role, t1, t2, t3 in [(22, rot, 'resultat', 'quart de tour', r'$\det = 1$', 'dans $SO$'),
                                (66, mir, 'limite', 'miroir', r'$\det = -1$', 'pas dans $SO$')]:
    cy = 40
    line(ax, [(cx - 19, cy), (cx + 19, cy)], 'fixe', 0.6); line(ax, [(cx, cy - 17), (cx, cy + 17)], 'fixe', 0.6)
    poly(ax, [(cx + p[0], cy + p[1]) for p in P], 'sujet')
    poly(ax, [(cx + f(p)[0], cy + f(p)[1]) for p in P], role)
    text(ax, cx, 66, t1, role, 'm'); text(ax, cx, 14, t2, role, 'm'); text(ax, cx, 6, t3, role, 's')
text(ax, 22, 22, 'départ en bleu', 'sujet', 's'); text(ax, 66, 22, 'départ en bleu', 'sujet', 's')
save(fig, '73-131')
