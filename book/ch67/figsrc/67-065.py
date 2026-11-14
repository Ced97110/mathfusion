import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$q = p^m$ : un corps existe', 'sujet', 'm')
cases = [(r'$9$', r'$= 3^2$', 'corps à 9 éléments', 'resultat'),
         (r'$16$', r'$= 2^4$', 'corps à 16 éléments', 'resultat'),
         (r'$6$', r'$= 2 \times 3$', 'aucun corps', 'limite')]
for k, (q, dec, res, role) in enumerate(cases):
    y = 40 - k * 17 + 4
    box(ax, 3, y - 5, 14, 10, 'sujet' if role == 'resultat' else 'limite', label=q)
    text(ax, 30, y, dec, 'encre', 'm')
    arrow(ax, (44, y), (50, y), 'varie')
    box(ax, 51, y - 5, 35, 10, role, label=res, size='s')
save(fig, '67-065')
