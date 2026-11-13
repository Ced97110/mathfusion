import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
rows = [(r'$u^2\approx3{,}732$', 'sujet', "d'abord"),
        (r'$u^4\approx13{,}93$', 'sujet', 'carré du résultat'),
        (r'$4u^2\approx14{,}93$', 'varie', 'on retranche'),
        (r'$+\,1$', 'varie', 'on ajoute')]
ys = [78, 62, 46, 30]
for y, (s, role, a) in zip(ys, rows):
    box(ax, 4, y, 38, 11, role, label=s, size='m')
    text(ax, 46, y + 5.5, a, role, 's', ha='left')
for y in ys:
    arrow(ax, (23, y), (23, y - 5), 'fixe')
box(ax, 4, 14, 80, 11, 'resultat', label=r'$13{,}93-14{,}93+1=0$', size='l')
save(fig, '61-096')
