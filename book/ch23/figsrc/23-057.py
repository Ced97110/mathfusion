import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 6.0
def sq(x0, n, role):
    for i in range(n):
        for j in range(n):
            ax.add_patch(Rectangle((x0 + i*u, 14 + j*u), u, u, ec=COL[role], fc=FILL[role], lw=0.6, zorder=2))
sq(8, 4, 'sujet'); sq(50, 3, 'sujet')
text(ax, 8 + 12, 8, r'$b=4$', 'sujet', 'm'); text(ax, 50 + 9, 8, r'$b=-3$', 'sujet', 'm')
text(ax, 20, 44, r'$b^2=16$', 'resultat', 'm'); text(ax, 59, 38, r'$b^2=9$', 'resultat', 'm')
text(ax, 44, 59, r'$b^2$ : jamais négatif', 'varie', 'm')
save(fig, '23-057')
