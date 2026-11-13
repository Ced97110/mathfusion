import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(c, r, a0, a1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, color=COL[role], lw=0.9, zorder=3))
def pt(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def square(c, d1, d2, s=2.2, role='fixe'):
    u = (math.cos(math.radians(d1)), math.sin(math.radians(d1))); v = (math.cos(math.radians(d2)), math.sin(math.radians(d2)))
    line(ax, [(c[0]+s*u[0], c[1]+s*u[1]), (c[0]+s*(u[0]+v[0]), c[1]+s*(u[1]+v[1])), (c[0]+s*v[0], c[1]+s*v[1])], role, lw=0.7)

fig, ax = canvas(62)
Ls = 34
for x0, th, lab, val, pl in [(5, 60, r'$\cos 60° = 0{,}5$', '5 m sur 10 m', 'AB = 10 m'), (50, 30, r'$\cos 30° \approx 0{,}87$', '8,66 m sur 10 m', 'AB = 10 m')]:
    A = (x0, 18); B = pt(A, Ls, th); Fp = (B[0], A[1])
    line(ax, [(x0 - 1, 18), (x0 + 36, 18)], 'fixe')
    line(ax, [B, Fp], 'fixe', dash=True)
    line(ax, [A, Fp], 'resultat', lw=2.6)
    line(ax, [A, B], 'sujet', lw=1.6)
    disc(ax, *A, 0.9, 'sujet'); disc(ax, *B, 0.9, 'sujet')
    arc(A, 8, 0, th); text(ax, x0 + 11.5, 18 + (3.2 if th == 30 else 6.5), r'%d°' % th, 'varie', size='s')
    text(ax, (A[0] + Fp[0]) / 2, 13.5, pl.replace('AB = 10 m', '') or '', 'resultat', size='s') if False else None
    text(ax, x0 + 18, 11.5, val, 'resultat', size='s')
    text(ax, x0 + 18, 4.5, lab, 'encre', size='s')
    text(ax, x0 + 18 - (8 if th == 60 else 0), 52 if th == 60 else 52, 'AB = 10 m', 'sujet', size='s')
save(fig, '26-097')
