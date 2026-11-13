import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(c, r, a0, a1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=0.9, zorder=3))
def pt(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def square(c, d1, d2, s=2.2, role='fixe'):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); v = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(c[0]+s*u[0], c[1]+s*u[1]), (c[0]+s*(u[0]+v[0]), c[1]+s*(u[1]+v[1])), (c[0]+s*v[0], c[1]+s*v[1])], role, lw=0.7)

fig, ax = canvas(100)
P = (20, 90); Fp = (20, 10); G = (45, 10)
th = math.degrees(math.atan2(80, 25))
line(ax, [(4, 10), (60, 10)], 'fixe'); line(ax, [P, Fp], 'fixe', dash=True); line(ax, [P, (60, 90)], 'fixe', dash=True)
line(ax, [P, G], 'sujet', lw=1.6)
disc(ax, *P, 1.2, 'sujet'); disc(ax, *G, 1.2, 'sujet')
arc(P, 24, -th, 0, 'resultat'); arc(P, 34, -90, -th, 'limite')
text(ax, 33, 80, '72,5°', 'resultat', 's'); text(ax, 14, 58, '17,5°', 'limite', 's', ha='right')
text(ax, 20, 96, 'regard', 'sujet', 's') if False else None
text(ax, 14, 32, '190 m', 'fixe', 's', ha='right'); text(ax, 32.5, 5, '60 m', 'fixe', 's')
text(ax, 50, 40, 'à partir de', 'resultat', 's', ha='left'); text(ax, 50, 34, 'l’horizontale :', 'resultat', 's', ha='left'); text(ax, 50, 28, '72,5° (bon)', 'resultat', ha='left')
text(ax, 50, 20, 'à partir de la', 'limite', 's', ha='left'); text(ax, 50, 14.5, 'verticale : faux', 'limite', 's', ha='left')
save(fig, '26-108')
