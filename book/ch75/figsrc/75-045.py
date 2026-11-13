import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
u = 8
def base(ox, oy, a, b, ra, rb, la, lb):
    arrow(ax, (ox, oy), (ox + a[0]*u, oy + a[1]*u), ra, lw=1.4); arrow(ax, (ox, oy), (ox + b[0]*u, oy + b[1]*u), rb, lw=1.4)
    text(ax, ox + a[0]*u + 1, oy + a[1]*u - 3.2, la, ra, 's'); text(ax, ox + b[0]*u - 3.5, oy + b[1]*u + 1, lb, rb, 's')
base(8, 28, (1, 0), (0, 1), 'sujet', 'sujet', r'$e$', r'$f$')
text(ax, 14, 18, r'$B = 1$', 'sujet', 's')
base(56, 44, (1, 0), (2, 1), 'resultat', 'resultat', r'$\eta e$', r'$\eta f$')
text(ax, 72, 40, r'$B = 1$', 'resultat', 's')
base(56, 12, (2, 0), (0, 1), 'limite', 'limite', r'$\eta e$', r'$\eta f$')
text(ax, 72, 6, r'$B = 2$', 'limite', 's')
arrow(ax, (28, 36), (50, 48), 'resultat', lw=1.0); arrow(ax, (28, 26), (50, 14), 'limite', lw=1.0)
text(ax, 36, 52, r'$\eta$ symplectique', 'resultat', 's'); text(ax, 36, 8, r'$\eta$ double $e$', 'limite', 's')
save(fig, '75-045')
