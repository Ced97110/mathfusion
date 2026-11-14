import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# left : galoisian case, square n x n grid
gx, gy, cs = 10, 22, 8
for k in range(4):
    line(ax, [(gx, gy + k * cs), (gx + 3 * cs, gy + k * cs)], 'sujet')
    line(ax, [(gx + k * cs, gy), (gx + k * cs, gy + 3 * cs)], 'sujet')
text(ax, 22, 64, 'extension galoisienne', 'sujet', 's')
text(ax, gx + 12, 52, r'$\eta_j$ (colonnes)', 'sujet', 's')
text(ax, 5.5, gy + 12, r'$u_i$', 'sujet', 's')
text(ax, 22, 15, r'$n\times n$ : $\det\neq 0\Leftrightarrow$ base', 'resultat', 's')
# right : Q(cube root 2), one column
hx = 62
for k in range(4):
    line(ax, [(hx, gy + k * cs), (hx + cs, gy + k * cs)], 'limite', dash=True)
for k in range(2):
    line(ax, [(hx + k * cs, gy), (hx + k * cs, gy + 3 * cs)], 'limite', dash=True)
text(ax, 66, 64, r'$\mathbb{Q}(\sqrt[3]{2})$, degré 3', 'limite', 's')
text(ax, hx + 4, 52, r'$\eta_1$', 'limite', 's')
text(ax, hx - 4, gy + 12, r'$u_i$', 'limite', 's')
text(ax, 68, 15, r'$3\times1$ : pas carrée', 'limite', 's')
text(ax, 68, 9, 'pas de déterminant', 'limite', 's')
save(fig, '67-133')
