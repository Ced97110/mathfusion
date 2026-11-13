import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
D = math.sqrt(984375); k = 0.18
data = [(14, D/75, 'sujet', r'$r$' + '\n13,23'), (32, D/35, 'sujet', r'$r_a$' + '\n28,35'),
        (52, D/25, 'autre', r'$r_b$' + '\n39,69'), (73, D/15, 'autre', r'$r_c$' + '\n66,14')]
fig, ax = canvas(98)
for x, r, role, lab in data:
    disc(ax, x, 84, r*k, role)
    text(ax, x, 68, lab, role, 'm')
brace(ax, 8, 38, 62, 'sujet', label='375', down=True)
brace(ax, 50, 80, 62, 'autre', label='2 625', down=True)
arrow(ax, (23, 55), (30, 44.5), 'varie'); arrow(ax, (65, 55), (58, 44.5), 'varie')
box(ax, 16, 34, 56, 10, 'varie', label='375 × 2 625 = 984 375', size='m')
arrow(ax, (44, 34), (44, 20.5), 'varie')
text(ax, 48, 27, 'racine carrée', 'varie', 'm', ha='left')
box(ax, 16, 10, 56, 10, 'resultat', label='aire = 992,2 m²', size='m', weight='bold')
save(fig, '37-092')
