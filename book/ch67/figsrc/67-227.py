import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
vals = ['00', '10', '01', '11']
xs = [6, 26, 46, 66]
text(ax, 6, 74, '1re colonne (2 bits)', 'encre', 'm', ha='left')
for x, v in zip(xs, vals):
    box(ax, x, 60, 16, 9, 'fixe' if v == '00' else 'sujet', label=v)
brace(ax, 26, 82, 59, 'sujet', label='3 choix')
text(ax, 6, 46, '2e colonne si la 1re est 10', 'encre', 'm', ha='left')
for x, v in zip(xs, vals):
    box(ax, x, 32, 16, 9, 'fixe' if v in ('00', '10') else 'resultat', label=v)
brace(ax, 6, 42, 31, 'fixe', label='sur la droite')
brace(ax, 46, 82, 31, 'resultat', label='2 choix')
text(ax, 44, 10, r'$3\times2=6$ matrices', 'resultat', 'l')
save(fig, '67-227')
