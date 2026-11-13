import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
def nd(x, y, n, role, w=12, h=7): box(ax, x - w/2, y - h/2, w, h, role, label=n)
text(ax, 22, 76, r'$(4\vee6)\vee10$', 'encre', 's'); text(ax, 66, 76, r'$4\vee(6\vee10)$', 'encre', 's')
for dx, (a, b, c) in ((0, (9, 23, 37)), (44, (51, 65, 79))):
    nd(a, 60, '4', 'sujet'); nd(b, 60, '6', 'autre'); nd(c, 60, '10', 'sujet')
line(ax, [(9,56),(15,42)]); line(ax, [(23,56),(17,42)]); line(ax, [(16,34),(26,20)]); line(ax, [(37,56),(28,20)])
nd(16,38,'12','varie'); nd(26,16,'60','resultat')
line(ax, [(65,56),(71,42)]); line(ax, [(79,56),(75,42)]); line(ax, [(73,34),(65,20)]); line(ax, [(51,56),(60,20)])
nd(73,38,'30','varie'); nd(62,16,'60','resultat')
text(ax, 44, 6, 'même résultat, chemins différents', 'resultat', 's')
save(fig, '79-088')
