import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cases = [  # (x0, polynomial, (a, b, c), roots, role, label)
    (2, r'$x^2-4x+4$', (1, -4, 4), (2, 2), 'sujet', 'racine double 2'),
    (46, r'$x^2-5x+6$', (1, -5, 6), (2, 3), 'autre', 'racines 2 et 3'),
]
for x0, poly, (a, b, c), roots, role, lab in cases:
    d = b * b - 4 * a * c
    assert (d == 0) == (roots[0] == roots[1])
    cx = x0 + 20
    box(ax, x0, 66, 40, 9, role, label=poly, size='m')
    arrow(ax, (cx, 66), (cx, 59.5), 'varie')
    box(ax, x0, 50, 40, 9, 'varie' if d == 0 else 'fixe', label=rf'$b^2-4ac={b*b}-{4*a*c}={d}$', size='s')
    arrow(ax, (cx, 50), (cx, 38.5), 'varie')
    f = numberline(ax, x0 + 4, x0 + 32, 32, 1, 4, arrow_right=False)
    seen = {}
    for r in roots:
        k = seen.get(r, 0); seen[r] = k + 1
        disc(ax, f(r), 32 + 3.4 * k, 1.4, 'resultat')
    text(ax, cx, 17, lab, 'resultat', 'm')
text(ax, 44, 8, r'$b^2-4ac=0$ : racine double', 'encre', 's')
save(fig, '55-132')
