import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 25, 72, 'R / ann x : 3 classes', 'autre', 's', weight='bold')
text(ax, 68, 72, 'Rx : 3 éléments', 'sujet', 's', weight='bold')
cls = ['0, 3, 6, 9 …', '1, 4, 7, 10 …', '2, 5, 8, 11 …']
els = ['0', '4 h', '8 h']
for i in range(3):
    y = 55 - i * 20
    box(ax, 3, y - 7, 44, 14, 'autre', label=cls[i], size='s')
    box(ax, 62, y - 7, 24, 14, 'sujet', label=els[i], size='m')
    arrow(ax, (47.5, y), (61.5, y), 'resultat', lw=1.3, both=True)
text(ax, 54.5, 63, '≅', 'resultat', 'l')
text(ax, 44, 3.5, 'classe de a  ↔  a × 4 h', 'varie', 's')
save(fig, '57-167')
