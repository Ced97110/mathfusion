import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="fixe", lw=0.9, n=60):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role, lw)
fig, ax = canvas(66)
text(ax, 44, 61, r'$\theta = 30°$ : $\cos 2\theta = \cos 60° = 0{,}5$', 'sujet', 's')
rows = [('si on connaît les deux', r'$\cos^2\theta - \sin^2\theta$', '0,75 − 0,25'),
        ('si on connaît le sinus', r'$1 - 2\sin^2\theta$', '1 − 2 × 0,25'),
        ('si on connaît le cosinus', r'$2\cos^2\theta - 1$', '2 × 0,75 − 1')]
for i, (h, e, n) in enumerate(rows):
    y = 44 - i * 18
    text(ax, 3, y + 6, h, 'fixe', 's', ha='left'); text(ax, 3, y, e, 'sujet', 'm', ha='left'); text(ax, 3, y - 5, n, 'varie', 's', ha='left')
    ax.add_patch(Rectangle((50, y - 2), 32, 4, fc='none', ec=COL['fixe'], lw=0.7, zorder=2))
    ax.add_patch(Rectangle((50, y - 2), 16, 4, fc=FILL['resultat'], ec=COL['resultat'], lw=0.8, zorder=3))
    text(ax, 74, y + 5, '= 0,5', 'resultat', 's')
text(ax, 66, 4, 'cadre = 1', 'fixe', 's')
save(fig, '31-148')
