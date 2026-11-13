import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
text(ax,44,76,r'$441 = 3^2 \times 7^2$ : un carré','encre','m')
x0=14; w=12; g=6
for i,(l,r) in enumerate(zip(['3','3','7','7'],['sujet','sujet','autre','autre'])):
    box(ax,x0+i*(w+g),56,w,10,r,label=l)
brace(ax,x0,x0+2*w+g,56,'sujet',label=r'$3^2$',down=True)
brace(ax,x0+2*(w+g),x0+4*w+3*g,56,'autre',label=r'$7^2$',down=True)
text(ax,44,40,r'$= 21 \times 21$ : deux facteurs égaux','resultat','m')
line(ax,[(4,33),(84,33)],'fixe',dash=True)
text(ax,44,28,'60 : exposants 2, 1, 1','encre','m')
for i,(l,r) in enumerate(zip(['2','2','3','5'],['varie','varie','sujet','resultat'])):
    box(ax,x0+i*(w+g),10,w,10,r,label=l)
text(ax,44,3,'ici, pas tous égaux','limite','s')
save(fig,'05-069')
