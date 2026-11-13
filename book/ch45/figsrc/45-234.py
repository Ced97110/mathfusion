import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def grp(y, name, els, role):
    text(ax, 3, y + 14, name, role, 'm', ha='left', weight='bold')
    for i, e in enumerate(els):
        box(ax, 22 + i * 16, y + 8, 13, 12, 'fixe' if i == 0 else role, label=str(e), size='l')
    text(ax, 28.5, y + 3, 'ordre 1', 'fixe', 's')
    brace(ax, 38, 82, y + 6.5, role, down=False, depth=1.4) if False else None
    line(ax, [(38, y + 6), (82, y + 6)], role)
    text(ax, 60, y + 2, 'ordre 2 : carré = 1', role, 's')
grp(40, r'$U(8)$', [1, 3, 5, 7], 'sujet')
grp(8, r'$U(12)$', [1, 5, 7, 11], 'autre')
text(ax, 44, 66, 'ordre = nombre de pas pour revenir à 1', 'encre', 's')
save(fig, '45-234')
