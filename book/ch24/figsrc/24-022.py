import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 30, 47, r'$x+y=5$', 'sujet', 's'); text(ax, 52, 47, r'$2x+y=8$', 'autre', 's')
text(ax, 75, 47, 'système', 'encre', 's')
rows = [(r'$(3,\,2)$', '5 ✓', '8 ✓', 'solution', 'resultat', 28),
        (r'$(4,\,1)$', '5 ✓', '9 ✗', 'pas solution', 'limite', 8)]
for lab, a, b, res, role, y in rows:
    box(ax, 2, y, 16, 13, 'fixe', label=lab, size='s')
    box(ax, 20, y, 20, 13, 'resultat', label=a, size='s')
    box(ax, 42, y, 20, 13, 'resultat' if '✓' in b else 'limite', label=b, size='s')
    box(ax, 64, y, 22, 13, role, label=res, size='s')
save(fig, '24-022')
