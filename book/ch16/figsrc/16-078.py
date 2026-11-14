import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 4, 52, 'aller', 'varie', 'm', ha='left'); text(ax, 4, 28, 'retour', 'autre', 'm', ha='left')
for yc, role_a, labs, ops in ((40, 'varie', ('4', '16', '9'), ('× 4', '− 7')), (14, 'autre', ('9', '16', '4'), ('+ 7', '÷ 4'))):
    for cx, lab in zip((14, 44, 74), labs):
        box(ax, cx - 7, yc - 5, 14, 10, 'fixe' if lab == '16' else 'sujet', label=lab, size='l')
    for cx, op in zip((29, 59), ops):
        arrow(ax, (cx - 7, yc), (cx + 7, yc), role_a)
        text(ax, cx, yc + 6, op, role_a, 'm')
save(fig, '16-078')
