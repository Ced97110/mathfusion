import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
labs = [r'$\sqrt{12}+\sqrt{27}$', r'$2\sqrt{3}+3\sqrt{3}$', r'$(2+3)\sqrt{3}$', r'$5\sqrt{3}$']
acts = ['on simplifie', 'on regroupe', 'on additionne 2 et 3']
for i, l in enumerate(labs):
    y = 66 - i * 20
    box(ax, 4, y, 36, 9, 'resultat' if i == 3 else 'sujet', label=l)
    if i < 3:
        arrow(ax, (22, y), (22, y - 11), 'varie'); text(ax, 26, y - 5.5, acts[i], 'varie', 's', ha='left')
save(fig, '22-104')
