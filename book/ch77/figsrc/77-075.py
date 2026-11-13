import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
k = 0.8; Y = 8
def panel(x0, f, role, head, poly, note, deg):
    X = lambda l: x0 + l / 6 * 34
    line(ax, [(x0 - 2, Y), (x0 + 37, Y)], 'fixe')
    line(ax, [(X(i / 20 * 6), Y + f(i / 20 * 6) * k) for i in range(21)], role, lw=1.3)
    ax.plot([X(3)] * 2, [Y - 1.2, Y + 1.2], color=COL['fixe'], lw=0.8)
    text(ax, X(3), Y - 4, '3', 'fixe', 's')
    text(ax, x0 + 17, 59, head, role, 'm'); text(ax, x0 + 17, 53, poly, role, 's')
    text(ax, x0 + 17, 47.5, note, role, 's'); text(ax, x0 + 17, 42, deg, role, 's')
    return X
X1 = panel(4, lambda l: l * l - 6 * l + 25, 'resultat', r'$z=3+4i$', r'$\lambda^2-6\lambda+25$', r'$36-100<0$ : pas de racine', 'minimal : degré 2')
panel(48, lambda l: (l - 3) ** 2, 'varie', r'$z=3$ ($b=0$)', r'$(\lambda-3)^2$', 'racine 3', r'minimal $\lambda-3$ : degré 1')
line(ax, [(X1(3), Y), (X1(3), Y + 16 * k)], 'fixe', dash=True)
text(ax, X1(3) + 5, Y + 8 * k, '16', 'fixe', 's')
save(fig, '77-075')
