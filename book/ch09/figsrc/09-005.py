import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for b, role, name, tot in [(28, 'sujet', 'Élève A', 100), (8, 'autre', 'Élève B', 50)]:
    box(ax, 24, b, tot * 0.6, 9, role, fill=False, r=0.4)
    box(ax, 24, b, 35 * 0.6, 9, role, label='35', size='s', r=0.4)
    text(ax, 2, b + 4.5, name, role, 'm', ha='left', weight='bold')
    text(ax, 24, b + 13, f'35 sur {tot}', role, 'm', ha='left')
text(ax, 44, 48, 'même 35, totaux différents', 'encre', 'm')
save(fig, '09-005')
