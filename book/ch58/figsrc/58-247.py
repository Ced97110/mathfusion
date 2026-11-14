import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 9
def panel(ox, both):
    oy = 22
    P = lambda a, b: (ox + a * u, oy + b * u)
    arrow(ax, P(-0.5, 0), P(3.6, 0), 'sujet', lw=1.1)
    if both:
        arrow(ax, P(0, -0.5), P(0, 2.7), 'autre', lw=1.1)
    for a in range(4):
        for b in range(3):
            if both:
                disc(ax, *P(a, b), 1.3, 'resultat')
            elif b == 0:
                disc(ax, *P(a, b), 1.3, 'sujet')
            elif (a, b) == (0, 1):
                disc(ax, *P(a, b), 1.4, 'limite')
            else:
                disc(ax, *P(a, b), 1.1, 'fixe', fill=False)
    return P
P1 = panel(8, True)
P2 = panel(52, False)
text(ax, 22, 56, 'riz + lentilles', 'encre', 'm', weight='bold')
text(ax, 66, 56, 'riz seul', 'encre', 'm', weight='bold')
text(ax, 22, 8, 'tout couple est atteint', 'resultat', 's', weight='bold')
text(ax, 66, 8, '(0, 1) non atteint', 'limite', 's', weight='bold')
text(ax, P2(0, 1)[0] - 7.5, P2(0, 1)[1], '(0, 1)', 'limite', 's')
save(fig, '58-247')
