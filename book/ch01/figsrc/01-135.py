import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
X = lambda n: 12 + 13.5 * n
Y = lambda v: 14 + 2.2 * v
ax.add_patch(Rectangle((12, 14), 36, 78, fc=FILL['limite'], ec='none', zorder=1))
ax.add_patch(Rectangle((48, 14), 37, 78, fc=FILL['resultat'], ec='none', zorder=1))
text(ax, 30, 94, 'faux', 'limite', 'm'); text(ax, 70, 94, 'vrai', 'resultat', 'm')
line(ax, [(8, 14), (85, 14)], 'fixe')
for n in range(6):
    line(ax, [(X(n), 13), (X(n), 15)], 'fixe')
    text(ax, X(n), 10, str(n), 'fixe', 's')
A = [2 ** n for n in range(6)]; B = [n + 4 for n in range(6)]
line(ax, [(X(n), Y(A[n])) for n in range(6)], 'sujet', lw=1.2)
line(ax, [(X(n), Y(B[n])) for n in range(6)], 'autre', lw=1.2)
for n in range(6):
    disc(ax, X(n), Y(A[n]), 1, 'sujet'); disc(ax, X(n), Y(B[n]), 1, 'autre')
text(ax, 72, 86, r'$2^n$', 'sujet', 'm'); text(ax, 75, 28.5, r'$n + 4$', 'autre', 'm')
line(ax, [(52.5, 14), (52.5, 96)], 'varie', dash=True)
text(ax, 52.5, 99, 'départ : 3', 'varie', 's')
for x, a, b, tx, ty, tt in [(55, 7, 8, 55, 26.5, '1'), (68.5, 8, 16, 71, 40.4, '8'), (82, 9, 32, 78.5, 59, '23')]:
    arrow(ax, (x, Y(a)), (x, Y(b)), 'resultat', both=True)
    text(ax, tx, ty, tt, 'resultat', 's')
save(fig, '01-135')
