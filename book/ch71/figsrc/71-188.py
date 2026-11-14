import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rows = [(48, '$x^2+y^2$', '$x^2-y^2$', None, None),
        (30, '2', '2', 'rang', ('=', 'resultat')),
        (12, '(2, 0)', '(1, 1)', 'signature', ('$\\neq$', 'limite'))]
for y, a, b, lab, sg in rows:
    box(ax, 4, y, 26, 11, 'sujet', label=a, size='m')
    box(ax, 58, y, 26, 11, 'autre', label=b, size='m')
    if sg:
        text(ax, 44, y + 11.5, lab, 'encre', 's')
        box(ax, 36, y, 16, 9, sg[1], label=sg[0], size='l', weight='bold')
text(ax, 44, 4, 'pas congruentes sur $\\mathbb{R}$', 'limite', 's')
save(fig, '71-188')
