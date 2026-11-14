import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y = 24
items = [(3, 19, 'sujet', r'$2x+4$', r'$c(f)=2$'), (30, 19, 'autre', r'$3x+6$', r'$c(g)=3$'),
         (54, 31, 'resultat', r'$6x^2+24x+24$', r'$c(fg)=6$')]
for x, w, role, lab, c in items:
    box(ax, x, y, w, 10, role, label=lab)
    text(ax, x + w / 2, y - 5, c, role, 'm', weight='bold')
text(ax, 25.5, y + 5, r'$\times$', 'encre', 'l')
text(ax, 48.5, y + 5, '=', 'encre', 'l')
text(ax, 44, y + 18, 'f', 'encre', 's') if False else None
text(ax, 44, 8, r'$c(fg)=c(f)\,c(g)$ : $2\times 3=6$', 'encre', 's')
text(ax, 12.5, y + 14, r'$f$', 'sujet', 's')
text(ax, 39.5, y + 14, r'$g$', 'autre', 's')
text(ax, 69.5, y + 14, r'$fg$', 'resultat', 's')
save(fig, '56-142')
