import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
c=13.38; x0,y0=20,12
MONO='DejaVu Sans Mono'
sp=' '*6
t=text(ax,x0+c*1.5,y0+3*c+4,sp.join('123'),'autre','l'); t.set_family(MONO)
for j in range(3):
    text(ax,x0-5,y0+(2-j)*c+c/2,str(j+1),'sujet','l')
    for k in range(3):
        box(ax,x0+k*c,y0+(2-j)*c,c,c,'resultat' if j==k else 'fixe')
    t=text(ax,x0+c*1.5,y0+(2-j)*c+c/2,sp.join('1' if j==k else '0' for k in range(3)),'encre','l'); t.set_family(MONO)
text(ax,x0-5,y0+3*c+4,r'$j\backslash k$','encre','s',ha='right') if False else None
text(ax,x0+c*1.5,y0-4,r'$\delta_{22}=1$','resultat','m')
text(ax,x0+c*3+17,y0+c*1.5,r'$\delta_{23}=0$','fixe','m')
arrow(ax,(x0+c*3+3,y0+c*1.5+3),(x0+c*2.5+3,y0+c*1.5+1),'fixe')
save(fig,'76-083')
