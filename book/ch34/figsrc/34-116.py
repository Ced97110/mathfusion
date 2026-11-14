import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 8, 42, 72, 11, 'sujet', label=r'$\cos 15°=\cos(45°-30°)$', size='m')
w, g, y0 = 23, 7.5, 14
xs = [2.5, 2.5 + w + g, 2.5 + 2 * (w + g)]
labs = [r'$\cos 45°\cos 30°$' + '\n0,6124', r'$\sin 45°\sin 30°$' + '\n0,3536', '0,9659']
roles = ['sujet', 'autre', 'resultat']
for x, l, r in zip(xs, labs, roles):
    box(ax, x, y0, w, 15, r, label=l, size='s')
text(ax, xs[0] + w + g / 2, y0 + 7.5, '+', 'varie', 'l')
text(ax, xs[1] + w + g / 2, y0 + 7.5, '=', 'varie', 'l')
arrow(ax, (44, 42), (44, 31), 'varie')
text(ax, 46, 36.5, 'on développe', 'varie', 's', ha='left')
text(ax, 44, 6, r'$=(\sqrt{6}+\sqrt{2})/4$', 'resultat', 'm')
save(fig, '34-116')
