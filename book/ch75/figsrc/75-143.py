import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 22, 56, r'sur $\mathbb{R}$', 'sujet', 'l'); text(ax, 66, 56, r'sur $\mathbb{C}$', 'autre', 'l')
B = 34
line(ax, [(4, B), (40, B)], 'fixe'); line(ax, [(48, B), (84, B)], 'fixe')
for x, h, lab in [(10, 10, r'$x_1^2$'), (26, 6, r'$x_2^2$')]:
    box(ax, x, B, 8, h, 'sujet', r=0.3); text(ax, x + 4, B + h + 3, lab, 'sujet', 's')
box(ax, 54, B, 8, 10, 'sujet', r=0.3); text(ax, 58, B + 13, r'$1^2=1$', 'sujet', 's')
box(ax, 70, B - 10, 8, 10, 'limite', r=0.3); text(ax, 74, B - 14, r'$i^2=-1$', 'limite', 's')
text(ax, 22, 12, 'somme positive', 'resultat', 's')
text(ax, 66, 12, 'somme = 0', 'limite', 's'); text(ax, 66, 6, r'flèche $(1,\,i)\neq0$', 'limite', 's')
save(fig, '75-143')
