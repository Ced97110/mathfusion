import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
k, x0 = 24, 5
a, b = 0.3290, 0.6710
text(ax, 4, 67, 'départ : 1re identité', 'sujet', 's', ha='left')
box(ax, x0, 50, a * k, 8, 'varie', r=0.5); box(ax, x0 + a * k, 50, b * k, 8, 'autre', r=0.5)
text(ax, x0 + a * k / 2 - 1, 61.5, r'$\sin^2\theta$', 'varie', 's'); text(ax, x0 + a * k + b * k / 2 + 4, 61.5, r'$\cos^2\theta$', 'autre', 's')
brace(ax, x0, x0 + k, 48.5, 'sujet', label='1', depth=1.4)
arrow(ax, (x0 + 40, 41), (x0 + 40, 30), 'varie', lw=1.6)
text(ax, x0 + 43, 36, r'on divise par $\sin^2\theta$ = 0,3290', 'varie', 's', ha='left')
c2 = b / a
box(ax, x0, 12, 1 * k, 8, 'varie', r=0.5); box(ax, x0 + k, 12, c2 * k, 8, 'autre', r=0.5)
text(ax, x0 + k / 2, 12 + 11.5, '1', 'varie', 's')
text(ax, x0 + k + c2 * k / 2, 12 + 11.5, r'$\mathrm{cotan}^2\theta$ = 2,04', 'autre', 's')
brace(ax, x0, x0 + k + c2 * k, 10.5, 'resultat', label=r'$\mathrm{cosec}^2\theta$ = 3,04', depth=1.4)
save(fig, '31-078')
