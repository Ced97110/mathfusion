import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
def row(y,title,u):
    text(ax,44,y+18,title,'encre','m')
    w,g,x0=5.2,0.8,5.4
    for i in range(13): box(ax,x0+(w+g)*i,y,w,7,'sujet' if i<8 else 'autre',r=0.4)
    e=lambda i: x0+(w+g)*i-g/2
    brace(ax,x0,x0+13*(w+g)-g,y+8.5,'resultat',label=u%13,down=False)
    brace(ax,x0,e(8)-0.2,y-1,'sujet',label=u%8); brace(ax,e(8)+0.6,x0+13*(w+g)-g,y-1,'autre',label=u%5)
row(60,'unité : la barre $x$',r'$%dx$')
row(22,'unité : le mètre',r'$%d$ m')
save(fig,'15-045')
