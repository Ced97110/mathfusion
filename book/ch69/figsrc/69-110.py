import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
w, g, x0 = 16.0, 3.0, 22.0
xs = [x0 + i * (w + g) for i in range(3)]
top = [r'$-16$', r'$24$', r'$-8$']
bot = [r'$2$', r'$-3$', r'$1$']
text(ax, 11, 47, r'$h_j(-3)$', 'sujet', 'm')
text(ax, 11, 23, r'$g_j=h_j/h_2$', 'resultat', 's')
for i in range(3):
    box(ax, xs[i], 42, w, 10, 'sujet', label=top[i], size='m')
    box(ax, xs[i], 18, w, 10, 'resultat', label=bot[i], size='m')
    arrow(ax, (xs[i] + w / 2, 41.5), (xs[i] + w / 2, 28.5), 'varie')
text(ax, 11, 35, r'$\div\,(-8)$', 'varie', 'm')
text(ax, 82, 47, r'$V=2$', 'sujet', 'm')
text(ax, 82, 23, r'$V=2$', 'resultat', 'm')
box(ax, 10, 3, 68, 9, 'resultat', label='même nombre de changements', size='m')
save(fig, '69-110')
