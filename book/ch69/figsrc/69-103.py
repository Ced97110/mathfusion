import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 8, 72, 22, -6, 6, 1, labels=False)
for v in (-5, 5):
    line(ax, [(f(v), 22), (f(v), 27)], 'resultat', dash=True)
box(ax, f(-5), 27, f(5) - f(-5), 9, 'resultat', label=r'$(-\mu,\mu)$', size='m')
for r in (-1.8794, 0.3473, 1.5321):
    disc(ax, f(r), 22, 1.4, 'sujet')
text(ax, f(-5), 17, r'$-\mu=-5$', 'resultat', 'm')
text(ax, f(0), 17, '0', 'fixe', 's')
text(ax, f(5), 17, r'$\mu=5$', 'resultat', 'm')
text(ax, f(0), 10, r'les 3 racines de $x^3-3x+1$', 'sujet', 'm')
text(ax, 44, 45, r'$\mu=1+0+3+1=5$', 'encre', 'l')
save(fig, '69-103')
