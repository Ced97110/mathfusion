import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
w, g = 14.0, 2.0
top = [r'$-16$', r'$24$', r'$-8$']
tx0 = 44 - (3 * w + 2 * g) / 2
for i in range(3):
    box(ax, tx0 + i * (w + g), 42, w, 10, 'sujet', label=top[i], size='m')
text(ax, 77, 47, r'$V=2$', 'sujet', 'm')
lists = [(4, [r'$-4$', r'$6$', r'$-2$']), (46, [r'$2$', r'$-3$', r'$1$'])]
for x0, vals in lists:
    for i in range(3):
        box(ax, x0 + i * 13.6, 20, 12, 10, 'resultat', label=vals[i], size='m')
    text(ax, x0 + 19.6, 14, r'$V=2$', 'resultat', 'm')
arrow(ax, (36, 41), (24, 32), 'varie')
arrow(ax, (52, 41), (64, 32), 'varie')
text(ax, 16, 38, r'$\div\,4$', 'varie', 'm')
text(ax, 76, 37, r'$\div\,(-8)$', 'varie', 'm')
text(ax, 44, 4, 'même nombre de changements', 'resultat', 'm')
save(fig, '69-111')
