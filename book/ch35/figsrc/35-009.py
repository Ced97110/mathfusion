import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 5; O = (30, 26); Hh = (45, 26); A = (45, 46)
nv = (-20, 15)
def grid(p, v1, v2, n1, n2, role):
    for i in range(1, n1):
        a = (p[0] + v1[0] * i / n1, p[1] + v1[1] * i / n1)
        line(ax, [a, (a[0] + v2[0], a[1] + v2[1])], role, 0.35)
    for j in range(1, n2):
        a = (p[0] + v2[0] * j / n2, p[1] + v2[1] * j / n2)
        line(ax, [a, (a[0] + v1[0], a[1] + v1[1])], role, 0.35)
def sq(p, v1, v2, role):
    poly(ax, [p, (p[0] + v1[0], p[1] + v1[1]), (p[0] + v1[0] + v2[0], p[1] + v1[1] + v2[1]), (p[0] + v2[0], p[1] + v2[1])], role)
sq(O, (15, 0), (0, -15), 'sujet'); grid(O, (15, 0), (0, -15), 3, 3, 'sujet')
sq(Hh, (0, 20), (20, 0), 'varie'); grid(Hh, (0, 20), (20, 0), 4, 4, 'varie')
sq(O, (15, 20), nv, 'resultat'); grid(O, (15, 20), nv, 5, 5, 'resultat')
poly(ax, [O, Hh, A], 'fixe')
line(ax, [O, Hh], 'sujet', 1.6); line(ax, [Hh, A], 'varie', 1.6); line(ax, [O, A], 'resultat', 1.6)
text(ax, 37.5, 18.5, r'$a^2=9$', 'sujet', 's', weight='bold'); text(ax, 55, 36, r'$b^2=16$', 'varie', 's', weight='bold')
text(ax, 27.5, 43.5, r'$R^2=25$', 'resultat', 's', weight='bold')
text(ax, 44, 4.5, r'$9+16=25$', 'encre', 'l')
save(fig, '35-009')
