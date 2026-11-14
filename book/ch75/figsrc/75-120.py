import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
sp = 22; ox, oy = 18, 14
arrow(ax, (ox, oy), (ox + 2.4 * sp, oy), 'fixe', lw=0.7); arrow(ax, (ox, oy), (ox, oy + 2.4 * sp), 'fixe', lw=0.7)
arrow(ax, (ox, oy), (ox + sp - 3, oy), 'sujet', lw=1.5)
text(ax, ox + sp - 1, oy - 4, r'$e=(1,0)$', 'sujet', 's')
for a in (0, 1):
    for b in (0, 1):
        ok = b == 1
        disc(ax, ox + a * sp, oy + b * sp, 2.6, 'resultat' if ok else 'limite')
        text(ax, ox + a * sp + (8 if a else -7), oy + b * sp + (0 if b else 5), f'({a},{b})', 'resultat' if ok else 'limite', 's')
text(ax, 72, 44, r'$B(e,y)=b$', 'varie', 'm')
text(ax, 72, 34, r'$b=1$ : 2 choix', 'resultat', 's')
text(ax, 72, 24, r'$q^{2n-1}=2^{1}$', 'sujet', 's')
save(fig, '75-120')
