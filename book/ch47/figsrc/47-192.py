import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'puissance 4, car $\varphi(10)=4$', 'sujet', 'm')
rows = [(3, 1, r'$3^4=81$', 'reste 1', 'resultat'), (9, 1, r'$9^4=6561$', 'reste 1', 'resultat'),
        (2, 2, r'$2^4=16$', 'reste 6', 'limite')]
for k, (a, g, c, r, role) in enumerate(rows):
    y = 42 - k * 15
    disc(ax, 9, y, 5.5, 'sujet', label=rf'$a={a}$', size='s')
    text(ax, 27, y, f'PGCD : {g}', role, 's')
    text(ax, 49, y, c, 'encre', 'm')
    box(ax, 64, y - 5, 22, 10, role, label=r)
save(fig, '47-192')
