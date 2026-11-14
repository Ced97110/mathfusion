import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'$g=y^3-y$ et $f=y^2+1$', 'encre', 'm')
x0, w, gap = 5, 14, 2
for i in range(5):
    x = x0 + i * (w + gap)
    if i < 3:
        box(ax, x, 22, w, 10, 'fixe', label=r'$f$')
    else:
        box(ax, x, 22, w, 10, 'autre', label=r'$g$')
xe = x0 + 2 * (w + gap) + w
brace(ax, x0, xe, 34, 'sujet', label=r'$m=3$ lignes de $f$', down=False)
brace(ax, xe + gap, x0 + 4 * (w + gap) + w, 34, 'fixe', label=r'$n=2$ lignes de $g$', down=False)
brace(ax, x0, x0 + 4 * (w + gap) + w, 20, 'resultat', label=r'$m+n=3+2=5$ lignes', down=True)
save(fig, '70-063')
