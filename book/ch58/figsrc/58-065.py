import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 52, 'une seule taille convient', 'encre', 'm')
cols = [(2, 'limite', '(3, 1)\nne suffit pas', '1 élément'),
        (31, 'resultat', '(1, 0), (0, 1)\nune base', '2 éléments'),
        (60, 'limite', '(1,0)+(0,1)−(1,1)\n= (0, 0)\npas de base', '3 éléments')]
for x, role, lab, cnt in cols:
    box(ax, x, 16, 26, 24, role, label=lab, size='s')
    text(ax, x + 13, 44, cnt, role, 's')
brace(ax, 4, 84, 12, 'sujet', label='$m = n$ : même nombre', size='m')
save(fig, '58-065')
