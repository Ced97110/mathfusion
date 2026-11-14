import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 64, 'refaire la preuve ?', 'varie', 'l', weight='bold')
box(ax, 2, 22, 30, 28, 'sujet')
text(ax, 17, 43, 'preuve du', 'sujet', 's')
text(ax, 17, 39, 'chapitre 13', 'sujet', 's')
text(ax, 17, 30, r'$(-a)(-b)=ab$', 'sujet', 's')
for i, nom in enumerate(['nombres', 'expressions', 'heures', 'tableaux']):
    y = 46 - 14 * i
    box(ax, 52, y, 34, 10, 'autre')
    text(ax, 55, y + 5, nom, 'autre', 's', ha='left')
    text(ax, 83, y + 5, '?', 'varie', 'l', ha='right', weight='bold')
    arrow(ax, (32, 36), (52, y + 5), 'varie')
save(fig, '51-004')
