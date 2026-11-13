import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
f = numberline(ax, 22, 66, 66, 0, 6, labels=False, role='autre')
for i in range(6):
    arrow(ax, (f(i) + 0.8, 68), (f(i + 1) - 0.8, 68), 'autre', lw=0.8, curve=-0.5)
text(ax, 44, 76, 'récurrence', 'autre', 'm')
g = numberline(ax, 22, 66, 30, 0, 6, labels=False, role='fixe')
for v in (2, 4, 5):
    disc(ax, g(v), 30, 1.4, 'sujet'); ax.patches[-1].set_zorder(4)
ax.add_patch(Circle((g(2), 30), 2.6, ec=COL['resultat'], fc='none', lw=0.9, zorder=3))
text(ax, g(2), 24, 'plus petit', 'resultat', 's')
text(ax, 44, 40, 'bon ordre', 'sujet', 'm')
arrow(ax, (13, 60), (13, 36), 'fixe')
text(ax, 7, 48, 'aller : déjà établi', 'fixe', 's', rot=90)
arrow(ax, (75, 36), (75, 60), 'varie', lw=1.6)
text(ax, 81, 48, 'retour : à établir', 'varie', 's', rot=90)
text(ax, 44, 10, 'deux chemins : équivalents', 'resultat', 'm')
save(fig, '01-163')
