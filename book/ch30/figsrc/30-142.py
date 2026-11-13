import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
L = 62
box(ax, 4, 50, L, 6, 'sujet', label=r'$2\pi\approx 6{,}28$', size='m')
text(ax, 4 + L + 2, 53, 'à atteindre', 'sujet', 's', ha='left')
rows = [(r'$0\times 2=0$', 'fixe'), (r'$0\times 6{,}28=0$', 'fixe'), (r'$0\times\ ?\ =2\pi$', 'limite')]
for i, (s, ro) in enumerate(rows):
    y = 36 - i * 11
    disc(ax, 4, y, 1.2, 'varie' if ro == 'fixe' else 'limite')
    text(ax, 8, y, s, ro, 'm', ha='left')
text(ax, 46, 14, 'aucun nombre ne convient', 'limite', 's', ha='left')
text(ax, 46, 36, 'on reste à 0', 'varie', 's', ha='left')
text(ax, 44, 4, r'$2\pi/0$ : pas de résultat', 'limite', 'm')
save(fig, '30-142')
