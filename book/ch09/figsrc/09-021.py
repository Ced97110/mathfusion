import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
ox, oy, u = 8, 8, 4.5
R = lambda a, b: (ox + a * u, oy + b * u)
for k in (3, 2, 1):
    a, b = 4 * k, 3 * k
    poly(ax, [R(0,0), R(a,0), R(a,b), R(0,b)], 'fixe', fill=False)
line(ax, [R(0,0), R(12,9)], 'resultat', lw=1.3)
disc(ax, *R(0,0), 1.2, 'fixe')
text(ax, ox - 3, oy - 1, r'$O$', 'fixe', 'l')
for k in (1, 2, 3):
    a, b = 4 * k, 3 * k
    disc(ax, *R(a, b), 1.3, 'sujet')
    text(ax, R(a, b)[0] - 1.8, R(a, b)[1] + 3.2, f'({a} ; {b})', 'sujet', 's', ha='right')
text(ax, 72, 14, r'$h \div l = 0{,}75$', 'resultat', 's')
text(ax, 72, 56, 'même droite', 'resultat', 's')
save(fig, '09-021')
