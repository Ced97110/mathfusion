import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 17, 70, 'ancien nom', 'sujet', 's')
text(ax, 71, 70, 'nouveau nom', 'varie', 's')
old = [r'$1+\sqrt{2}$', r'$2+\sqrt{2}$', r'$4+3\sqrt{2}$']
new = [r'$1-\sqrt{2}$', r'$2-\sqrt{2}$', r'$4-3\sqrt{2}$']
for i in range(3):
    c = 58 - 14 * i
    box(ax, 4, c - 5, 26, 10, 'sujet', label=old[i])
    box(ax, 58, c - 5, 26, 10, 'varie', label=new[i])
    arrow(ax, (31, c), (57, c), 'varie')
text(ax, 44, 62, r'$\eta$', 'varie', 'm')
text(ax, 44, 23, 'égalité toujours vraie', 'resultat', 's')
box(ax, 2, 4, 42, 14, 'sujet', label=r'$(1+\sqrt{2})(2+\sqrt{2})=4+3\sqrt{2}$', size='s')
box(ax, 46, 4, 40, 14, 'varie', label=r'$(1-\sqrt{2})(2-\sqrt{2})=4-3\sqrt{2}$', size='s')
save(fig, '63-028')
