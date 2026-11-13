import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
def node(cx, cy, lab, role):
    box(ax, cx - 5.5, cy - 4, 11, 8, role, label=lab)
def down(a, b):
    arrow(ax, (a[0], a[1] - 4.2), (b[0], b[1] + 4.2), 'fixe')
text(ax, 3, 84, '(1) existence : on casse', 'sujet', 's', ha='left', weight='bold')
n12, n2a, n6, n2b, n3 = (36, 72), (20, 58), (52, 58), (42, 44), (62, 44)
node(*n12, '$12$', 'sujet'); node(*n6, '$6$', 'sujet')
node(*n2a, '$2$', 'resultat'); node(*n2b, '$2$', 'resultat'); node(*n3, '$3$', 'resultat')
down(n12, n2a); down(n12, n6); down(n6, n2b); down(n6, n3)
text(ax, 3, 33, '(2) unicité : on barre un 2', 'autre', 's', ha='left', weight='bold')
for i, (l, r) in enumerate(zip(['$2$', '$2$', '$3$'], ['varie', 'sujet', 'sujet'])):
    node(26 + i * 14, 24, l, r)
for i, (l, r) in enumerate(zip(['$3$', '$2$', '$2$'], ['sujet', 'varie', 'sujet'])):
    node(26 + i * 14, 8, l, r)
arrow(ax, (26, 19.5), (40, 12.5), 'varie', both=True)
text(ax, 54, 16, 'barrés des 2 côtés', 'varie', 's', ha='left')
save(fig, '56-074')
