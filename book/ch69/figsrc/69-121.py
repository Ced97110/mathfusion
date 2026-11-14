import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 30, 70, r'$v_k^{\,e}\,F=QG-R$', 'sujet', 'm')
text(ax, 68, 70, r'$v_k^{\,e}=3^2=9$', 'sujet', 'm')
rows = [(52, 'sujet', r'$9F$', r'$9x^3-27x+9$'),
        (34, 'fixe', r'$QG$', r'$-(3x)(3x^2-3)=-(9x^3-9x)$'),
        (12, 'resultat', r'$-R$', r'$=-18x+9$')]
for y, role, lab, expr in rows:
    box(ax, 4, y, 20, 11, role, label=lab)
    text(ax, 30, y + 5.5, expr, 'encre', 'm', ha='left')
line(ax, [(4, 28), (84, 28)], 'fixe', lw=0.8)
text(ax, 44, 4, 'coefficients tous entiers', 'resultat', 's')
save(fig, '69-121')
