import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
data = [(66, r'$1_S\,\circ$', 'α', 'resultat', 'neutre : α reste α'),
        (42, 'α ∘', r'$1_S$', 'autre', 'inverse : défait α seulement'),
        (18, 'β ∘', 'β', 'limite', 'β remplace : pas neutre')]
for y, lab, out, role, com in data:
    box(ax, 6, y - 4.5, 14, 9, 'sujet', label='α', size='l')
    arrow(ax, (23, y), (45, y), 'varie')
    text(ax, 34, y + 3.8, lab, 'varie', 'm')
    box(ax, 48, y - 4.5, 14, 9, role, label=out, size='l')
    text(ax, 44, y - 9.5, com, role, 'm')
save(fig, '44-054')
