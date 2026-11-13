import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
D = math.sqrt(984375); k = 0.2
rows = [(D/75, 'sujet', r'$r$ × $s$ = 13,23 × 75'), (D/35, 'autre', r'$r_a$ × ($s-a$) = 28,35 × 35'),
        (D/25, 'autre', r'$r_b$ × ($s-b$) = 39,69 × 25'), (D/15, 'autre', r'$r_c$ × ($s-c$) = 66,14 × 15')]
fig, ax = canvas(80)
y = 76
for r, role, lab in rows:
    rr = r*k; y -= rr
    disc(ax, 20, y, rr, role)
    text(ax, 38, y, lab, role, 'm', ha='left')
    y -= rr + 4
text(ax, 38, 4, 'chaque produit ≈ 992,2', 'resultat', 'm', ha='left', weight='bold')
save(fig, '37-090')
