import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 64, 'un constat sur 12', 'fixe', 'm')
for y, name, seq in [(50, 'vous', ['2', '2', '3']), (38, 'camarade', ['3', '2', '2'])]:
    text(ax, 3, y + 4, name, 'fixe', 's', ha='left')
    for i, s in enumerate(seq):
        box(ax, 24 + i * 14, y, 12, 8, 'sujet', label=s)
text(ax, 76, 46, 'mêmes nombres,\nautre ordre', 'resultat', 's')
box(ax, 14, 20, 60, 9, 'sujet', label='Théorème : unicité')
box(ax, 14, 3, 60, 9, 'autre', label='division avec reste')
arrow(ax, (44, 12), (44, 20), 'varie')
text(ax, 48, 16, 'repose sur', 'varie', 's', ha='left')
save(fig, '56-001')
