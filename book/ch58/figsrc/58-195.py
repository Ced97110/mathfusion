import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
# η envoie les vecteurs de base e_i de R^m vers des vecteurs de R^n
box(ax, 2, 6, 32, 46, 'sujet')
text(ax, 18, 47, r'départ $R^m$', 'sujet', 's', weight='bold')
box(ax, 54, 6, 32, 46, 'autre')
text(ax, 70, 47, r'arrivée $R^n$', 'autre', 's', weight='bold')
for k, (e, img) in enumerate([(r'$e_1$', '(2, 1)'), (r'$e_2$', '(1, 3)')]):
    y = 29 - k * 15
    box(ax, 7, y, 22, 10, 'sujet', label=e, size='m', r=0.6, fill=False)
    box(ax, 59, y, 22, 10, 'autre', label=img, size='m', r=0.6, fill=False)
    arrow(ax, (29.5, y + 5), (58.5, y + 5), 'varie', lw=1.4)
text(ax, 44, 58, r'$\eta$ : homomorphisme', 'varie', 'm', weight='bold')
save(fig, '58-195')
