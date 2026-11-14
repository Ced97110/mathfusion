import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 15, 73, 'blocs', 'fixe', 'm', weight='bold')
text(ax, 68, 73, 'mots envoyés', 'sujet', 'm', weight='bold')
# panneau 1 : injectif
for y, b, w in [(58, '0', '000'), (46, '1', '111')]:
    box(ax, 8, y, 14, 7, 'fixe', label=b)
    box(ax, 56, y, 24, 7, 'sujet', label=w)
    arrow(ax, (23.5, y + 3.5), (54.5, y + 3.5), 'varie')
text(ax, 39, 62.5, r'$E$', 'varie', 'm')
text(ax, 44, 38.5, 'deux blocs, deux mots', 'resultat', 'm', weight='bold')
line(ax, [(3, 33), (85, 33)], 'fixe', lw=0.5, dash=True)
# panneau 2 : non injectif
box(ax, 8, 21, 14, 7, 'fixe', label='0')
box(ax, 8, 9, 14, 7, 'fixe', label='1')
box(ax, 56, 15, 24, 7, 'limite', label='000')
arrow(ax, (23.5, 24.5), (54.5, 19.5), 'limite')
arrow(ax, (23.5, 12.5), (54.5, 17.5), 'limite')
text(ax, 44, 3.5, 'même mot : 0 ou 1 ? interdit', 'limite', 'm', weight='bold')
save(fig, '68-032')
