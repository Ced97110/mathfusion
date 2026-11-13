import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
for i, lab in enumerate([r'$v_1$ = (3, 2, 1)', r'$v_2$ = (3, 2, 0)', r'$v_3$ = (1, 1, 1)']):
    box(ax, 2 + i * 28.5, 84, 27, 10, 'sujet', label=lab, size='s')
rows = [(66, r'$v_1 - v_2$', '(0, 0, 1) = $e_3$', 'resultat'),
        (50, r'$v_3 - e_3$', '(1, 1, 0)', 'varie'),
        (34, r'$v_2 - 2\cdot(1, 1, 0)$', '(1, 0, 0) = $e_1$', 'resultat'),
        (18, r'$(1, 1, 0) - e_1$', '(0, 1, 0) = $e_2$', 'resultat')]
for y, left, right, r in rows:
    box(ax, 3, y, 38, 10, 'sujet', label=left, size='s')
    arrow(ax, (42.5, y + 5), (49.5, y + 5), 'varie', lw=1.1)
    box(ax, 51, y, 35, 10, r, label=right, size='s')
text(ax, 44, 11, '$e_1$, $e_2$, $e_3$ retrouvés', 'resultat', 's')
text(ax, 44, 5, '3 vecteurs, dimension 3 : base', 'fixe', 's')
save(fig, '58-299')
