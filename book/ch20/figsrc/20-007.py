import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(56)
text(ax, 44, 51, r'$y$ entre 1 et 2, pour $x=3$', 'encre', 'm')
f = numberline(ax, 10, 70, 24, 1, 2, 0.25, True, 'fixe', True, 2)
for k in range(1, 16):
    if k % 4: ax.add_patch(Circle((f(1 + k / 16), 24), 0.6, ec=COL['sujet'], fc=COL['sujet'], zorder=3))
for v, s in [(1, '(3 ; 1)'), (1.25, '(3 ; 1,25)'), (1.5, '(3 ; 1,5)'), (2, '(3 ; 2)')]:
    disc(ax, f(v), 24, 1.5, 'resultat'); text(ax, f(v), 36, s, 'resultat', 's')
    line(ax, [(f(v), 33.2), (f(v), 26)], 'fixe', lw=0.6, dash=True)
text(ax, 44, 8, 'un autre couple entre deux', 'sujet', 'm')
save(fig, '20-007')
