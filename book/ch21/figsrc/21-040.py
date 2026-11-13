import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 58, r'$Q=x^2+1$ : valeur de $Q$', 'sujet', 'm')
f = numberline(ax, 8, 76, 12, 0, 10, 1, labels=False, arrow_right=False)
for xc, xv, qv in ((16, '0', 1), (44, '1', 2), (72, '-3', 10)):
    box(ax, xc - 9, 34, 18, 11, 'varie', label=rf'$x={xv}$', size='s')
    arrow(ax, (xc, 34), (f(qv), 15), 'resultat', curve=0.0)
    disc(ax, f(qv), 12, 1.4, 'resultat'); text(ax, f(qv), 6.5, f'{qv}', 'resultat', 's')
disc(ax, f(0), 12, 1.8, 'limite', fill=False, lw=1.0, ); text(ax, f(0), 6.5, '0', 'limite', 's')
text(ax, 26, 6.5, '← jamais atteint', 'limite', 's', ha='left')
save(fig, '21-040')
