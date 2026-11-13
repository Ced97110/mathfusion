import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
def nd(x, y, n, role, w=12, h=7): box(ax, x - w/2, y - h/2, w, h, role, label=n)
nd(16,62,'60','varie'); nd(16,40,'12','sujet')
line(ax, [(16,44),(16,58)], 'fixe')
text(ax, 24, 62, r'$a\vee b$', 'varie', 's', ha='left'); text(ax, 24, 40, r'$a$', 'sujet', 's', ha='left')
text(ax, 62, 70, 'en dessous de 12 et 60', 'fixe', 's')
for i, n in enumerate([1, 2, 3, 4, 6, 12]):
    r, c = divmod(i, 3)
    nd(48 + 14*c, 56 - 11*r, str(n), 'resultat' if n == 12 else 'fixe')
text(ax, 62, 34, 'le plus grand : 12', 'resultat', 's', weight='bold')
save(fig, '79-083')
