import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
def frac(x, y, n, d, role, w, size='s'):
    text(ax, x, y + 3.2, n, role, size); line(ax, [(x - w / 2, y), (x + w / 2, y)], role, lw=0.8); text(ax, x, y - 3.2, d, role, size)
text(ax, 15, 80, r'$\tan(A+B)=$', 'sujet', 'm')
frac(56, 80, r'$\sin(A+B)$', r'$\cos(A+B)$', 'sujet', 26, 'm')
arrow(ax, (44, 70), (44, 58), 'varie')
text(ax, 48, 64, 'formules d’addition', 'varie', 's', ha='left')
frac(44, 48, r'$\sin A\cos B+\cos A\sin B$', r'$\cos A\cos B-\sin A\sin B$', 'sujet', 56, 's')
arrow(ax, (44, 38), (44, 26), 'varie')
text(ax, 48, 32, 'diviser (45° et 30°)', 'varie', 's', ha='left')
frac(30, 14, '0,9659', '0,2588', 'resultat', 18, 'm')
text(ax, 60, 14, r'$=\ 3{,}732$', 'resultat', 'l')
save(fig, '34-066')
