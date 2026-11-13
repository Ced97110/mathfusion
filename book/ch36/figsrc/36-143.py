import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(80)
s = 7; x0, y0 = 7, 30
def sq(a, b, c, d, role):
    poly(ax, [(x0 + a*s, y0 + b*s), (x0 + c*s, y0 + b*s), (x0 + c*s, y0 + d*s), (x0 + a*s, y0 + d*s)], role)
sq(0, 0, 2, 2, 'resultat'); sq(2, 0, 5, 2, 'varie'); sq(0, 2, 2, 5, 'varie'); sq(2, 2, 5, 5, 'autre')
line(ax, [(x0, y0), (x0 + 5*s, y0), (x0 + 5*s, y0 + 5*s), (x0, y0 + 5*s), (x0, y0)], 'sujet', lw=1.5)
text(ax, x0 + s, y0 + s, '4', 'resultat', 'm'); text(ax, x0 + 3.5*s, y0 + s, '6', 'varie', 'm')
text(ax, x0 + s, y0 + 3.5*s, '6', 'varie', 'm'); text(ax, x0 + 3.5*s, y0 + 3.5*s, '9', 'autre', 'm')
text(ax, x0 - 3, y0 + 2.5*s, '5', 'sujet', 's'); brace(ax, x0 + 2*s, x0 + 5*s, y0 - 1.5, 'autre', down=True, label='3')
text(ax, 48, 64, '25 : le carré de 5', 'sujet', 's', ha='left')
text(ax, 48, 54, '− 15 − 15 : deux bandes', 'varie', 's', ha='left')
text(ax, 48, 44, '+ 9 : le recouvrement', 'autre', 's', ha='left')
text(ax, 48, 34, '= 4', 'resultat', 'm', ha='left')
text(ax, 44, 12, r'$(5-3)^2=25-30+9=4$', 'encre', 'm')
text(ax, 44, 4, 'trois termes, comme la loi des cosinus', 'encre', 's')
save(fig, '36-143')
