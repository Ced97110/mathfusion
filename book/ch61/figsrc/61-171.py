import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
rows = ['départ : 0 et 1', 'tracé 1', 'tracé 2', 'tracé 3']
flab = [r'$F_0=\mathbb{Q}$', r'$F_1=F_0(\sqrt{\ })$', r'$F_2=F_1(\sqrt{\ })$', r'$F_3=F_2(\sqrt{\ })$']
text(ax, 44, 70, 'tour quadratique', 'sujet', 'm', weight='bold')
for i in range(4):
    y = 4 + 16 * i
    box(ax, 4, y, 26, 10, 'fixe' if i == 0 else 'varie', label=rows[i], size='s')
    box(ax, 56, y, 28, 10, 'fixe' if i == 0 else 'sujet', label=flab[i], size='s')
    if i:
        arrow(ax, (30, y + 5), (56, y + 5), 'varie', lw=1.3)
        text(ax, 43, y + 9, 'au plus une $\\sqrt{\\ }$', 'varie', 's')
        arrow(ax, (70, y - 6), (70, y), 'resultat', lw=1.3)
save(fig, '61-171')
