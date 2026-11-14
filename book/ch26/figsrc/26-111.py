import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(c, r, a0, a1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=0.9, zorder=3))
def pt(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def square(c, d1, d2, s=2.2, role='fixe'):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); v = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(c[0]+s*u[0], c[1]+s*u[1]), (c[0]+s*(u[0]+v[0]), c[1]+s*(u[1]+v[1])), (c[0]+s*v[0], c[1]+s*v[1])], role, lw=0.7)

fig, ax = canvas(82)
th = 62.4; Bt = (8, 14); Fp = (38, 14); T = (38, 14 + 30 * math.tan(math.radians(th)))
line(ax, [(4, 14), (46, 14)], 'fixe'); line(ax, [Fp, T], 'fixe', lw=1.4)
line(ax, [Bt, Fp], 'sujet', lw=1.6); line(ax, [Fp, T], 'resultat', lw=2.4); line(ax, [Bt, T], 'autre', lw=2.0)
disc(ax, *Bt, 1.0, 'sujet'); disc(ax, *T, 1.0, 'sujet')
square(Fp, 180, 90)
arc(Bt, 12, 0, th, 'varie'); text(ax, 25, 22, '62,4°', 'varie', 's')
text(ax, 23, 8.5, '300 m', 'sujet'); text(ax, 42, 44, r'$y$', 'resultat', ha='left'); text(ax, 15, 46, r'$r$', 'autre')
text(ax, 8, 19, 'bateau', 'sujet', 's', ha='left') if False else None
text(ax, 4, 78, 'bateau', 'sujet', 's', ha='left') if False else None
text(ax, 50, 70, r'$y = 300 \times \tan 62{,}4°$', 'resultat', ha='left', size='s'); text(ax, 50, 63, r'$y \approx 573{,}8$ m', 'resultat', ha='left')
text(ax, 50, 48, r'$r = 300 \, / \, \cos 62{,}4°$', 'autre', ha='left', size='s'); text(ax, 50, 41, r'$r \approx 647{,}5$ m', 'autre', ha='left')
text(ax, 50, 28, 'un angle, deux rapports', 'encre', ha='left', size='s')
save(fig, '26-111')
