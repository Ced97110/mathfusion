import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
U = 20.0
X0 = 3.0
def cell(i, w, y, role, lab):
    box(ax, X0 + i * U + 0.5, y, w * U - 1, 12, role, label=lab, size='s')
box(ax, 3, 77, 4, 4, 'sujet'); text(ax, 9, 79, 'degré > 1 : se casse', 'sujet', 's', ha='left')
box(ax, 50, 77, 4, 4, 'varie'); text(ax, 56, 79, 'degré 1 : fini', 'varie', 's', ha='left')
cell(0, 3, 58, 'sujet', r'$x^3-2$ : degré 3')
cell(0, 1, 34, 'varie', 'degré 1')
cell(1, 2, 34, 'sujet', 'degré 2')
cell(0, 1, 10, 'varie', 'degré 1')
cell(1, 1, 10, 'varie', 'degré 1')
cell(2, 1, 10, 'varie', 'degré 1')
text(ax, 66, 64, '1 facteur', 'sujet', 's', ha='left')
text(ax, 66, 40, '2 facteurs', 'sujet', 's', ha='left')
text(ax, 66, 16, '3 facteurs $=n$', 'resultat', 's', ha='left', weight='bold')
arrow(ax, (33, 57), (33, 47.5), 'varie')
text(ax, 36, 52.5, 'Kronecker', 'varie', 's', ha='left')
arrow(ax, (43, 33), (43, 23.5), 'varie')
text(ax, 46, 28.5, 'Kronecker', 'varie', 's', ha='left')
text(ax, 44, 3.5, r'jamais plus de $n=3$ facteurs : on s’arrête', 'resultat', 's')
save(fig, '62-063')
