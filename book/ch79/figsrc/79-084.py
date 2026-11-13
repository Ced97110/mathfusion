import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
def nd(x, y, n, role, w=11, h=7): box(ax, x - w/2, y - h/2, w, h, role, label=n)
# left: lattice case
nd(10,20,'4','sujet'); nd(34,20,'6','autre'); nd(22,50,'12','resultat')
line(ax, [(10,24),(20,46)]); line(ax, [(34,24),(24,46)])
text(ax, 22, 68, 'treillis : le sup existe', 'resultat', 's')
# right: poset case
nd(58,20,'2','sujet'); nd(82,20,'3','autre'); nd(58,50,'12','limite'); nd(82,50,'18','limite')
for a, b in [(58,58),(58,82),(82,58),(82,82)]: line(ax, [(a,24),(b,46)])
text(ax, 70, 68, 'pas de sup de 2 et 3', 'limite', 's')
text(ax, 70, 58, '12 et 18 incomparables', 'limite', 's')
line(ax, [(44,10),(44,70)], 'fixe', dash=True)
text(ax, 22, 8, r'$\vee$ défini', 'resultat', 's'); text(ax, 70, 8, r'$\vee$ non défini', 'limite', 's')
save(fig, '79-084')
