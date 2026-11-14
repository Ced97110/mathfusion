import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 2, 58, 84, 14, 'sujet', label='pour quels $n$ : somme de $n$ carrés\n× somme de $n$ carrés = somme de $n$ carrés ?')
rows = [(40, '$n=2$', '$5\\times13=65$', 'resultat', 'somme de\n2 carrés'),
        (24, '$n=4$', '$4\\times7=28$', 'resultat', 'somme de\n4 carrés'),
        (8, '$n=3$', '$3\\times5=15$', 'limite', 'pas une somme\nde 3 carrés')]
for y, n, e, r, s in rows:
    box(ax, 2, y, 16, 12, 'sujet', label=n)
    box(ax, 22, y, 34, 12, 'fixe', label=e)
    arrow(ax, (56, y + 6), (60, y + 6), 'fixe')
    box(ax, 60, y, 26, 12, r, label=s, size='s')
save(fig, '78-071')
