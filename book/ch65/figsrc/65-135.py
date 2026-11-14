import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
box(ax, 4, 66, 24, 10, 'fixe', label=r'$\mathbb{Q}$')
box(ax, 4, 38, 24, 10, 'sujet', label=r'$\mathbb{Q}(r_1)$', size='s')
box(ax, 4, 10, 24, 10, 'autre', label=r'$E$')
arrow(ax, (16, 66), (16, 49), 'sujet')
arrow(ax, (16, 38), (16, 21), 'autre')
text(ax, 22, 57.5, '5', 'sujet', 'l', ha='left', weight='bold')
text(ax, 22, 29.5, '2', 'autre', 'l', ha='left', weight='bold')
# les 5 nombres de base de Q(r1) sur Q
text(ax, 62, 82, 'nombres de base', 'sujet', 's')
for i, lab in enumerate(['1', r'$r_1$', r'$r_1^2$', r'$r_1^3$', r'$r_1^4$']):
    box(ax, 36 + i * 10, 68, 9, 9, 'sujet', label=lab, size='s', r=0.5)
text(ax, 62, 42, 'supposé : 2 de plus', 'autre', 's')
box(ax, 34, 10, 52, 12, 'resultat', label=r'$5\times2=10$')
text(ax, 60, 4, 'multiple de 5', 'resultat', 's')
save(fig, '65-135')
