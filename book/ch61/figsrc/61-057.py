import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for y, lab, r, rest in [(48, r'$m_1$', 'sujet', r'$-\,x$'), (34, r'$m_2$', 'autre', r'$+\,1$')]:
    text(ax, 8, y, lab, r, 'l'); box(ax, 18, y - 5, 16, 10, 'varie', label=r'$x^3$'); text(ax, 42, y, rest, r, 'l')
text(ax, 62, 48, 'degré 3', 'fixe', 's'); text(ax, 62, 34, 'degré 3', 'fixe', 's')
line(ax, [(4, 27), (84, 27)], 'fixe', lw=0.6)
text(ax, 8, 18, r'$m_1-m_2$', 'resultat', 'm', ha='left')
text(ax, 38, 18, r'$x^3-x^3=0$', 'varie', 's')
text(ax, 72, 18, r'$-x-1$', 'resultat', 'm')
text(ax, 62, 8, 'degré 1 < 3', 'resultat', 's')
text(ax, 44, 59, 'x³ disparaît en soustrayant', 'varie', 's')
save(fig, '61-057')
