import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 20, 85, 'les restes', 'sujet', 'm')
text(ax, 68, 85, 'les nombres', 'autre', 'm')
L = [r'$(1+x)^2$', r'$1+2x+x^2$', r'$3+2x$']
R = [r'$(1+\sqrt{2})^2$', r'$1+2\sqrt{2}+(\sqrt{2})^2$', r'$3+2\sqrt{2}$']
ys = [68, 44, 20]
for i in range(3):
    box(ax, 2, ys[i], 36, 12, 'resultat' if i == 2 else 'sujet', label=L[i], size='s')
    box(ax, 50, ys[i], 36, 12, 'resultat' if i == 2 else 'autre', label=R[i], size='s')
    arrow(ax, (39, ys[i] + 6), (49, ys[i] + 6), 'resultat', both=True)
for i in range(2):
    ytop = ys[i] - 1
    ybot = ys[i + 1] + 13
    arrow(ax, (10, ytop), (10, ybot), 'varie')
    arrow(ax, (58, ytop), (58, ybot), 'varie')
ym = (ys[0] + ys[1] + 12) / 2 - 6
text(ax, 13, ym + 6, 'développer', 'varie', 's', ha='left')
text(ax, 61, ym + 6, 'développer', 'varie', 's', ha='left')
text(ax, 13, ym - 18, r'$x^2=2$', 'varie', 's', ha='left')
text(ax, 61, ym - 18, r'$(\sqrt{2})^2=2$', 'varie', 's', ha='left')
save(fig, '62-061')
