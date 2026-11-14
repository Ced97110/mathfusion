import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
def ligne(y, titre, role, tip, zero_label, lab_u, lab_res):
    f = numberline(ax, 8, 56, y, -1, 1, labels=False, arrow_right=False)
    text(ax, 32, y + 17, titre, role, 'm')
    arrow(ax, (f(0), y + 5), (f(1), y + 5), 'sujet', lw=1.5)
    text(ax, f(1) + 1, y + 9, lab_u, 'sujet', 's')
    arrow(ax, (f(0), y - 5), (f(tip), y - 5), role, lw=1.5)
    text(ax, f(tip) + (1 if tip > 0 else 0), y - 9, lab_res, role, 's', ha='left')
    box(ax, 62, y - 6, 24, 12, role, label=zero_label, size='s')
ligne(52, r'$1$ : ne change rien', 'resultat', 1, '0 réflexion', r'$u$', r'image : $u$')
ligne(16, r'$-1 = S_u$ : renverse', 'varie', -1, '1 réflexion', r'$u$', r'image : $-u$')
save(fig, '72-143')
