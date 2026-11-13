import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
k, x0, h = 1.8, 6, 6.5          # 1 unité = 1,8 mm
def bar(x, y, w, role, label=None, dash=False):
    box(ax, x, y, w, h, role, label=label, size='s', dash=dash, r=0.6)
# légende
text(ax, 20, 82, r'$\|u\|^2$', 'sujet', 's')
text(ax, 38, 82, r'$\|v\|^2$', 'autre', 's')
text(ax, 62, 82, r'$2\|u\|\|v\|\cos\theta$', 'fixe', 's')
text(ax, 80, 82, r'$\|u-v\|^2$', 'varie', 's')
# angle droit : 9 + 16, correction 0
text(ax, 44, 72, r'$\theta=90^\circ$ : correction $=0$', 'encre', 's')
bar(x0, 62, 9 * k, 'sujet', '9')
bar(x0 + 9 * k, 62, 16 * k, 'autre', '16')
bar(x0, 52, 25 * k, 'varie', '25')
# angle de 45° : 10 + 20, correction 20
text(ax, 44, 41, r'$\theta=45^\circ$ : correction $=20$', 'encre', 's')
bar(x0, 31, 10 * k, 'sujet', '10')
bar(x0 + 10 * k, 31, 20 * k, 'autre', '20')
bar(x0 + 10 * k, 21, 20 * k, 'fixe', '20', dash=True)
bar(x0, 11, 10 * k, 'varie', '10')
arrow(ax, (x0 + 20 * k, 30), (x0 + 20 * k, 28), 'fixe', lw=0.6)
text(ax, 44, 3, 'on retire la barre grise', 'fixe', 's')
save(fig, '41-083')
