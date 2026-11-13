import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 2, 18, 32, 46, 'sujet', r=1.2)
text(ax, 18, 59, '6 objets', 'sujet', 's')
for i in range(6):
    disc(ax, 8 + (i % 3)*10, 48 - (i // 3)*10, 2.6, 'sujet')
text(ax, 18, 30, r'$6! = 720$', 'sujet', 'm')
text(ax, 18, 23, 'permutations', 'sujet', 's')
box(ax, 54, 18, 32, 46, 'autre', r=1.2)
text(ax, 70, 59, '15 vecteurs', 'autre', 's')
for i in range(15):
    disc(ax, 60 + (i % 3)*10, 52 - (i // 3)*6, 1.6, 'autre')
text(ax, 70, 23, r'$|Sp_4(\mathbb{F}_2)| = 720$', 'autre', 's', 'center')
text(ax, 44, 44, '?', 'varie', 'xl', weight='bold')
text(ax, 44, 36, '=', 'resultat', 'xl')
text(ax, 44, 8, 'hasard ou lien ?', 'varie', 'm')
save(fig, '75-186')
