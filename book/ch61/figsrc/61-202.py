import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 2, 2, 84, 80, 'fixe')
text(ax, 9, 76, r'$\mathbb{R}$', 'fixe', 'l')
box(ax, 10, 8, 68, 58, 'sujet')
text(ax, 44, 60, 'réels constructibles', 'sujet', weight='bold')
text(ax, 44, 52, 'on part de 2 et de 3', 'fixe', 's')
text(ax, 44, 45, 'résultats, toujours dedans :', 'resultat', 's')
for lab, x, y in [(r'$2+3=5$', 14, 30), (r'$2-3=-1$', 46, 30), (r'$2\times3=6$', 14, 14), (r'$2\div3=2/3$', 46, 14)]:
    box(ax, x, y, 28, 10, 'resultat', label=lab)
save(fig, '61-202')
