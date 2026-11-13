import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# θ -> π - θ : r = 1 + cos θ devient 1 - cos θ (échec) ; r = 1 + sin θ reste la même (réussite)
fig, ax = canvas(98)
u = 9
def card(o, f, role, dash=False):
    pts = [(o[0] + u * f(t) * math.cos(t), o[1] + u * f(t) * math.sin(t)) for t in [i * 2 * math.pi / 300 for i in range(301)]]
    line(ax, pts, role, lw=1.3, dash=dash)
text(ax, 44, 94, r'on remplace $\theta$ par $\pi - \theta$', 'varie', 'm')
# cosinus
box(ax, 2, 70, 36, 11, 'sujet', label=r'$r = 1 + \cos\theta$', size='s')
arrow(ax, (20, 69.5), (20, 62.5), 'varie')
box(ax, 2, 51, 36, 11, 'limite', label=r'$r = 1 - \cos\theta$', size='s')
text(ax, 20, 46, '≠ : échec', 'limite', 's')
o1 = (62, 62)
line(ax, [(o1[0] - 8, o1[1]), (o1[0] + 22, o1[1])], 'fixe', lw=0.7)
card(o1, lambda t: 1 + math.cos(t), 'sujet')
card(o1, lambda t: 1 - math.cos(t), 'limite', dash=True)
# sinus
box(ax, 2, 28, 36, 11, 'sujet', label=r'$r = 1 + \sin\theta$', size='s')
arrow(ax, (20, 27.5), (20, 20.5), 'varie')
box(ax, 2, 9, 36, 11, 'resultat', label=r'$r = 1 + \sin\theta$', size='s')
text(ax, 20, 4, '= : réussite', 'resultat', 's')
o2 = (62, 16)
line(ax, [(o2[0], o2[1] - 4), (o2[0], o2[1] + 24)], 'fixe', lw=0.7)
card(o2, lambda t: 1 + math.sin(t), 'resultat')
text(ax, 71, 39, 'axe $y$', 'fixe', 's')
save(fig, '40-041')
