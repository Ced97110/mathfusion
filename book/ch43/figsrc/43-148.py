import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, r'$b=p\,a\,p^{-1}$', 'encre', 'xl')
for x, lab, role, w in [(2, r'$a$', 'sujet', 12), (38, r'$p\,a$', 'varie', 12), (72, r'$b$', 'autre', 14)]:
    box(ax, x, 56, w, 11, role, label=lab, size='l')
arrow(ax, (14.5, 61.5), (37.5, 61.5), 'varie'); text(ax, 26, 66, r'$p$ à gauche', 'varie', 's')
arrow(ax, (50.5, 61.5), (71.5, 61.5), 'varie'); text(ax, 61, 66, r'$p^{-1}$ à droite', 'varie', 's')
box(ax, 2, 8, 30, 36, 'fixe', dash=True); box(ax, 40, 8, 46, 36, 'fixe', dash=True)
disc(ax, 17, 26, 4.5, 'sujet', label=r'$e$')
for k, (dx, dy) in enumerate([(0, 8), (-7, -4), (7, -4)]):
    disc(ax, 63 + dx * 1.5, 24 + dy, 3.6, 'autre')
text(ax, 17, 48.5, '1 élément', 'sujet', 's') if False else None
text(ax, 17, 3.5, 'classe de l’identité', 'sujet', 's')
text(ax, 63, 3.5, 'une autre : plus grande', 'autre', 's')
save(fig, '43-148')
