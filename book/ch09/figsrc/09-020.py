import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
u = 4; oy = 20
def rect(ox, a, b, role, eq):
    R = lambda x, y: (ox + x * u, oy + y * u)
    poly(ax, [R(0,0), R(a,0), R(a,b), R(0,b)], role)
    line(ax, [R(0,0), R(a,b)], 'resultat', lw=1.4)
    text(ax, ox + a * u / 2, oy - 3.5, str(a), role, 's')
    text(ax, ox - 2.5, oy + b * u / 2, str(b), role, 's')
    text(ax, ox + a * u / 2, 9, eq, role, 's')
rect(10, 4, 3, 'sujet', r'$3/4 = 0{,}75$')
rect(46, 8, 6, 'autre', r'$6/8 = 0{,}75$')
text(ax, 44, 52, 'hauteur ÷ largeur', 'resultat', 'm', weight='bold')
text(ax, 34, 33, '=', 'resultat', 'xl')
save(fig, '09-020')
