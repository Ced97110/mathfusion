import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
fig, ax = canvas(60)
u = 22; c, s_ = math.cos(math.pi / 3), math.sin(math.pi / 3)
O1 = (6, 16); P1 = (O1[0] + u * c, 16 + u * s_); H1 = (P1[0], 16)
O2 = (42, 16); P2 = (O2[0] + 2 * u * c, 16 + 2 * u * s_); H2 = (P2[0], 16)
poly(ax, [O1, H1, P1], 'sujet'); poly(ax, [O2, H2, P2], 'limite')
line(ax, [O1, H1], 'resultat', lw=2.4); line(ax, [O2, H2], 'limite', lw=2.4)
for H_ in (H1, H2): line(ax, [(H_[0] - 3, 16), (H_[0] - 3, 19), (H_[0], 19)], 'fixe')
text(ax, 3, 12, r'$O$'); text(ax, H1[0], 12, r'$H$'); text(ax, P1[0] + 2.5, P1[1] + 2.5, r'$P$')
text(ax, 12.5, 20.5, '60°', 'varie', 's'); text(ax, 51, 21, '60°', 'varie', 's')
text(ax, 6, 31, 'OP = 1', 'sujet', 's'); text(ax, 47, 40, 'OP = 2', 'limite', 's')
text(ax, 14, 6, r'$OH = 0{,}5 = \cos 60°$', 'resultat', 's')
text(ax, 62, 6, r'$OH = 1 \neq \cos 60° = 0{,}5$', 'limite', 's')
save(fig, '29-109')
