import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 3.6
def R(x, y, w, h, r, lab=None, d=False): box(ax, x, y, w * u, h * u, r, label=lab, r=0.3, dash=d, fill=not d)
x0, y0 = 4, 14
poly(ax, [(x0 + a * u, y0 + b * u) for a, b in ((0,0),(6,0),(6,2),(2,2),(2,6),(0,6))], 'sujet')
R(x0 + 2 * u, y0 + 2 * u, 4, 4, 'fixe', '16', d=True)
text(ax, x0 + 3 * u, y0 - 3, r'$x^2-16$ = 20', 'sujet', 's')
text(ax, 38, y0 + 3 * u, '=', 'encre', 'l')
x1 = 46
R(x1, y0 + 1.5 * u, 10, 2, 'resultat')
text(ax, x1 + 5 * u, y0 + 2.5 * u, '10 × 2 = 20', 'resultat', 'm')
text(ax, x1 + 5 * u, y0 + 4.2 * u, r'$(x+4)(x-4)$', 'resultat', 's')
text(ax, 44, 46, r'$x$ = 6 : 36 − 16', 'encre', 'm', weight='bold')
save(fig, '18-054')
