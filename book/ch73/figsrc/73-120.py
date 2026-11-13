import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
u = 12; oy = 12
def P(o, pts): return [(o + a * u, oy + b * u) for a, b in pts]
sq = [(0, 0), (1, 0), (1, 1), (0, 1)]; c, s = math.cos(math.radians(30)), math.sin(math.radians(30))
rot = [(c * a - s * b, s * a + c * b) for a, b in sq]; she = [(a + b, b) for a, b in sq]
for o in (11, 36, 68): poly(ax, P(o, sq), 'fixe', fill=False)
poly(ax, P(11, rot), 'resultat'); poly(ax, P(36, she), 'resultat'); line(ax, P(68, [(0, 0), (1, 0)]), 'limite', lw=2)
text(ax, 16, 6, 'rotation 30°', 'resultat', 's'); text(ax, 46, 6, 'cisaillement', 'resultat', 's'); text(ax, 74, 6, 'écrasement', 'limite', 's')
brace(ax, 5, 60, 35, 'resultat', label=r'dans $GL_2(\mathbb{R})$', down=False)
text(ax, 74, 39, "n'y est pas", 'limite', 's')
save(fig, '73-120')
