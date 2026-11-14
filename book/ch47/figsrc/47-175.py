import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$H=\{1,\ s\}$ dans $D_4$ : 8 éléments', 'encre', 'm')
for g in range(4):
    x = 4 + g * 21
    role = 'sujet' if g == 0 else 'fixe'
    for k in range(2):
        box(ax, x, 36 - k * 11, 17, 9, role, label=(['1', r'$s$'][k] if g == 0 else None), size='m')
    box(ax, x - 1.5, 23.5, 20, 22.5, role, fill=False, dash=True, lw=0.7)
text(ax, 13.5, 51, r'$H$', 'sujet', 'm')
text(ax, 55, 51, '3 autres classes de 2', 'fixe', 's')
text(ax, 44, 15, r'$s\cdot s=1$ : sous-groupe', 'sujet', 's')
text(ax, 44, 7, r'indice $8\div2=4$ classes', 'resultat', 's')
save(fig, '47-175')
