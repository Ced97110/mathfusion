import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
top, bot, mids = (44, 70), (44, 20), [(14, 45), (44, 45), (74, 45)]
def edge(p, q, rp, rq):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); u = ((q[0] - p[0]) / d, (q[1] - p[1]) / d)
    line(ax, [(p[0] + u[0] * rp, p[1] + u[1] * rp), (q[0] - u[0] * rq, q[1] - u[1] * rq)])
for m in mids:
    edge(bot, m, 5.5, 6); edge(m, top, 6, 5.5)
disc(ax, *top, 5.5, 'resultat', label=r'$E$'); disc(ax, *bot, 5.5, 'resultat', label=r'$0$')
for k, m in enumerate(mids):
    disc(ax, *m, 6, 'sujet', label=rf'$D_{k+1}$')
text(ax, 44, 75 + 6, 'plan entier', 'fixe', 's'); text(ax, 44, 6, 'trois droites, incomparables', 'sujet', 's'); text(ax, 70, 20, 'vecteur nul', 'fixe', 's')
save(fig, '79-153')
