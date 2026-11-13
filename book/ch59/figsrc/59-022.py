import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
su, sv, ox, oy = 6.5, 3.0, 12, 10
P = lambda u, v: (ox + u * su, oy + v * sv)
poly(ax, [P(0, 0), P(2, 0), P(2, 10), P(0, 10)], 'sujet')
for u in range(0, 7):
    for v in range(0, 21):
        if u % 2 == 0 and v % 10 == 0:
            ax.plot([P(u, v)[0]], [P(u, v)[1]], 'o', color=COL['sujet'], ms=4, zorder=4)
        else:
            ax.plot([P(u, v)[0]], [P(u, v)[1]], '.', color=COL['fixe'], ms=1.8, zorder=3)
arrow(ax, P(0, 0), P(6.8, 0), 'fixe', lw=0.8); arrow(ax, P(0, 0), P(0, 21.5), 'fixe', lw=0.8)
text(ax, 86, 6, r"coordonnée sur $e'_1$", 'fixe', 's', ha='right')
text(ax, 3, 78, r"sur $e'_2$", 'fixe', 's', ha='left')
text(ax, P(1, 5)[0], P(1, 5)[1] + 2.5, 'aire', 'sujet', 's')
text(ax, P(1, 5)[0], P(1, 5)[1] - 2.5, r'$2\times10=20$', 'sujet', 's')
text(ax, P(1, 0)[0], P(1, 0)[1] - 3.2, '2', 'sujet', 's')
text(ax, P(0, 5)[0] - 3.5, P(0, 5)[1], '10', 'sujet', 's')
text(ax, 86, 70, r'$K=\{2a\,e_1^{\prime}+10b\,e_2^{\prime}\}$', 'sujet', 's', ha='right')
text(ax, 86, 63, 'points bleus : un par maille', 'sujet', 's', ha='right')
save(fig, '59-022')
