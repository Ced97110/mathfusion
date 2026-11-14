import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 70, "plus grand nombre d'additions", 'varie', 's')
labs = [r'$\mathbb{Z}/8$', r'$\mathbb{Z}/4\oplus\mathbb{Z}/2$', r'$\mathbb{Z}/2\oplus\mathbb{Z}/2\oplus\mathbb{Z}/2$']
nums = [8, 4, 2]
c = 6.0
for r, (lab, n) in enumerate(zip(labs, nums)):
    y = 52 - r * 22
    text(ax, 2, y + 3, lab, 'sujet', 's', ha='left')
    for k in range(n):
        box(ax, 34 + k * c, y - 3 if False else y, c, 6, 'resultat', r=0.3, lw=0.6)
    brace(ax, 34, 34 + n * c, y - 1, 'resultat', label=f'{n} additions')
save(fig, '60-104')
