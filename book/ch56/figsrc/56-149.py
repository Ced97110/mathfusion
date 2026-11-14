import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 4, 75, r'$f=2+3x+x^2$', 'sujet', 's', ha='left')
a = [(15, r'$a_0=2$', 'fixe'), (36, r'$a_1=3$', 'varie'), (57, r'$a_2=1$', 'fixe')]
b = [(36, r'$b_2=5$', 'varie'), (57, r'$b_1=2$', 'fixe'), (78, r'$b_0=4$', 'fixe')]
for cx, lab, role in a:
    box(ax, cx - 9, 56, 18, 9, role, label=lab, size='s')
for cx, lab, role in b:
    box(ax, cx - 9, 28, 18, 9, role, label=lab, size='s')
text(ax, 36, 68.5, r'$r=1$', 'varie', 's')
text(ax, 36, 23.5, r'$s=2$', 'varie', 's')
text(ax, 4, 23.5, r'$g=4+2x+5x^2$', 'sujet', 's', ha='left')
line(ax, [(36, 55), (36, 38)], 'varie', lw=1.2)
line(ax, [(57, 55), (57, 38)], 'fixe', lw=1.0)
text(ax, 37.5, 46.5, r'$3\times5=15$', 'varie', 's', ha='left')
text(ax, 58.5, 46.5, r'$1\times2=2$', 'fixe', 's', ha='left')
text(ax, 44, 14, r'$c_3=a_1b_2+a_2b_1=15+2=17$', 'resultat', 's')
text(ax, 44, 7, r'$p=2$ ne divise ni $a_1$ ni $b_2$', 'varie', 's')
save(fig, '56-149')
