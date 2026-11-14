import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 62, 64, 'diviseurs élémentaires', 'resultat', 's')
labs = [r'$\mathbb{Z}/8$', r'$\mathbb{Z}/4\oplus\mathbb{Z}/2$', r'$\mathbb{Z}/2\oplus\mathbb{Z}/2\oplus\mathbb{Z}/2$']
lists = [['8'], ['4', '2'], ['2', '2', '2']]
for r, (lab, ls) in enumerate(zip(labs, lists)):
    y = 46 - r * 20
    text(ax, 2, y + 5, lab, 'sujet', 's', ha='left')
    for k, v in enumerate(ls):
        box(ax, 46 + k * 13, y, 11, 10, 'resultat', label=v, size='l')
for y in (38, 18):
    text(ax, 52, y, '≠', 'limite', 'xl', weight='bold')
save(fig, '60-106')
