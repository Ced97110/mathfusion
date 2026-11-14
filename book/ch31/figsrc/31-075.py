import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
w, g, x0 = 23, 7, 2.5
xs = [x0 + i * (w + g) for i in range(3)]
top = [(r'$\sin^2\theta$' + '\n0,3290', 'sujet'), (r'$\cos^2\theta$' + '\n0,6710', 'sujet'), ('1', 'sujet')]
bot = [(r'$\tan^2\theta$' + '\n0,4903', 'resultat'), ('1', 'resultat'), (r'$\sec^2\theta$' + '\n1,4903', 'resultat')]
text(ax, 4, 67, 'départ : 1re identité', 'sujet', 's', ha='left')
for i in range(3):
    box(ax, xs[i], 48, w, 13, top[i][1], label=top[i][0], size='s')
    box(ax, xs[i], 12, w, 13, bot[i][1], label=bot[i][0], size='s')
    arrow(ax, (xs[i] + w / 2, 47.5), (xs[i] + w / 2, 41.5), 'varie')
    arrow(ax, (xs[i] + w / 2, 33.5), (xs[i] + w / 2, 25.5), 'varie')
for i, sg in enumerate(['+', '=']):
    text(ax, xs[i] + w + g / 2, 54.5, sg, 'sujet', 'm'); text(ax, xs[i] + w + g / 2, 18.5, sg, 'resultat', 'm')
box(ax, 4, 34, 80, 7, 'varie', label=r'on divise chaque terme par $\cos^2\theta$ = 0,6710', size='s')
text(ax, 4, 6, 'arrivée : 2e identité', 'resultat', 's', ha='left')
save(fig, '31-075')
