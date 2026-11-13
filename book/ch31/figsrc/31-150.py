import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="fixe", lw=0.9, n=60):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role, lw)
fig, ax = canvas(66)
u = 3.4; A0 = (6, 26); C = (A0[0] + 10 * u, A0[1])
ca, sa = math.cos(math.radians(30)), math.sin(math.radians(30))
line(ax, [A0, C], 'sujet', lw=1.4)
line(ax, [A0, (A0[0] + 14 * u * ca, A0[1] + 14 * u * sa)], 'fixe', lw=1.0)
for a, role in ((4, 'limite'), (5, 'resultat'), (7, 'autre')):
    arc(ax, C, a * u, 0, 180, role, 1.1)
    text(ax, C[0] + a * u, A0[1] - 3.5, str(a), role, 's')
    if a == 7:
        for sgn in (-1, 1):
            c = 10 * ca + sgn * math.sqrt(a * a - 25)
            disc(ax, A0[0] + c * u * ca, A0[1] + c * u * sa, 1.0, role)
disc(ax, A0[0] + 10 * ca * u * ca, A0[1] + 10 * ca * u * sa, 1.0, 'resultat')
arc(ax, A0, 7, 0, 30, 'varie')
text(ax, A0[0] + 4.5, A0[1] + 8, r'$A = 30°$', 'varie', 's')
text(ax, A0[0] + 5 * u, A0[1] - 3.5, r'$b = 10$', 'sujet', 's')
F = (A0[0] + 10 * ca * u * ca, A0[1] + 10 * ca * u * sa)
line(ax, [C, F], 'resultat', 0.9, dash=True)
text(ax, C[0] + 5, C[1] + 6, 'hauteur 5', 'resultat', 's')
text(ax, C[0] - 2, A0[1] + 20.5, r'$a$ : rayon de l\'arc', 'fixe', 's', ha='left') if False else None
text(ax, 44, 61, r'$a$ = rayon de chaque arc', 'fixe', 's')
text(ax, 26, 14, r'$a = 4$ : 0 triangle', 'limite', 's')
text(ax, 26, 9, r'$a = 5$ : 1 triangle', 'resultat', 's')
text(ax, 26, 4, r'$a = 7$ : 2 triangles', 'autre', 's')
save(fig, '31-150')
