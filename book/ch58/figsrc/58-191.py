import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
# 1, x, x^2, x^3, ..., x^n : toujours une fonction de plus, sur [a, b]
text(ax, 44, 55, r'fonctions continues sur $[a, b]$', 'encre', 'm')
size, gap, x0 = 15.0, 2.5, 2.75
pows = [0, 1, 2, 3, 6]
labs = ['1', r'$x$', r'$x^2$', r'$x^3$', r'$x^n$']
for k, (p, lab) in enumerate(zip(pows, labs)):
    x = x0 + k * (size + gap)
    box(ax, x, 28, size, size, 'fixe', fill=False, r=0.4, lw=0.6)
    pts = [(x + 1 + 13 * t, 29 + 13 * (t ** p)) for t in [i / 40 for i in range(41)]]
    line(ax, pts, 'sujet', lw=1.3)
    text(ax, x + size / 2, 23.5, lab, 'sujet', 'm')
brace(ax, x0, x0 + 4 * (size + gap) + size, 19, 'resultat', label=r'$n + 1$ fonctions indépendantes', down=True, depth=2.4)
text(ax, 44, 5, 'pour tout $n$ : pas de dimension finie', 'encre', 's')
save(fig, '58-191')
