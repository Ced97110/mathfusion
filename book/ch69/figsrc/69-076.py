import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
xs = [14, 32, 50, 68]
W = 13
r1 = [r'$-1$', r'$9$', r'$-5$', r'$9/4$']
r2 = [r'$-1$', r'$0$', r'$1$', r'$9/4$']
text(ax, 1, 57.5, r'$c=-2$', 'encre', 's', ha='left')
text(ax, 1, 19.5, r'$c=1$', 'encre', 's', ha='left')
for x, v in zip(xs, r1):
    box(ax, x, 52, W, 11, 'sujet', label=v)
for i in range(3):
    arrow(ax, (xs[i] + W / 2, 63.5), (xs[i + 1] + W / 2, 63.5), 'varie', curve=-0.6)
text(ax, 47, 44, r'$V(-2)=3$', 'resultat', 'm')
for i, (x, v) in enumerate(zip(xs, r2)):
    if i == 1:
        box(ax, x, 14, W, 11, 'fixe', label=v, dash=True)
    else:
        box(ax, x, 14, W, 11, 'sujet', label=v)
arrow(ax, (xs[0] + W / 2, 25.5), (xs[2] + W / 2, 25.5), 'varie', curve=-0.5)
text(ax, 47, 7, r'$V(1)=1$ ; le $0$ est effacé', 'resultat', 'm')
save(fig, '69-076')
