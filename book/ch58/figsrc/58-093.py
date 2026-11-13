import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
rows = [(70, 'droite', 1), (42, 'plan', 2), (12, 'espace', 3)]
text(ax, 84, 83, r'$\dim V$', 'resultat', 's', ha='right', weight='bold')
# droite
y = 70
text(ax, 3, y, 'droite', 'encre', 's', ha='left')
arrow(ax, (34, y), (58, y), 'sujet', lw=1.8)
text(ax, 84, y, r'$=1$', 'resultat', 'l', ha='right', weight='bold')
# plan
y = 42
text(ax, 3, y, 'plan', 'encre', 's', ha='left')
arrow(ax, (34, y - 8), (58, y - 8), 'sujet', lw=1.8)
arrow(ax, (34, y - 8), (46, y + 10), 'sujet', lw=1.8)
text(ax, 84, y, r'$=2$', 'resultat', 'l', ha='right', weight='bold')
# espace (iso)
o = (46, 8)
u = 15
text(ax, 3, 24, 'espace', 'encre', 's', ha='left')
for p in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
    arrow(ax, o, iso(*p, origin=o, u=u), 'sujet', lw=1.8)
text(ax, 84, 24, r'$=3$', 'resultat', 'l', ha='right', weight='bold')
save(fig, '58-093')
