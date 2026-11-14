import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'conjugué par la réflexion $s$', 'varie', 'm')
rows = [(r'$r$', r'$r^3$', 'varie', 'déplacé'), (r'$r^2$', r'$r^2$', 'fixe', 'en place')]
y = 40
for a, b, role, lab in rows:
    box(ax, 6, y - 6, 16, 12, 'sujet', label=a, size='m')
    arrow(ax, (24, y), (44, y), role)
    text(ax, 34, y + 3.2, r'$sxs^{-1}$', role, 's')
    box(ax, 46, y - 6, 16, 12, 'resultat' if role == 'fixe' else 'varie', label=b, size='m')
    text(ax, 75, y, lab, role, 's')
    y -= 22
save(fig, '49-115')
