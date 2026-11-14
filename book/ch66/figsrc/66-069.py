import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
rows = [(r'$n=15$', [('3', 'resultat'), ('5', 'resultat')], 'resultat', 'Fermat, distincts : constructible'),
        (r'$n=9$', [('3', 'limite'), ('3', 'limite')], 'limite', 'même facteur deux fois : non'),
        (r'$n=7$', [('7', 'limite')], 'limite', '7 n’est pas de Fermat : non')]
for k, (lab, facs, role, tag) in enumerate(rows):
    y = 58 - k * 25
    text(ax, 2, y + 6, lab, 'encre', 'm', ha='left')
    x = 26
    for i, (f, r) in enumerate(facs):
        if i:
            text(ax, x - 3, y + 6, r'$\times$', 'encre', 'm')
        box(ax, x, y, 14, 12, r, label=f, size='l')
        x += 20
    text(ax, 2, y - 5, tag, role, 's', ha='left')
save(fig, '66-069')
