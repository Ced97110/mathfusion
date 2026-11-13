import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
x0,y0,c=30,10,16
for i in range(2):
    for j in range(2):
        hot=(i==1 and j==0)
        box(ax,x0+j*c,y0+(1-i)*c,c,c,'varie' if hot else 'fixe',label='1' if hot else '0',size='l')
for j in range(2): text(ax,x0+j*c+c/2,y0+2*c+4,f'colonne {j+1}','autre','s')
for i in range(2): text(ax,x0-3,y0+(1-i)*c+c/2,f'ligne {i+1}','sujet','s',ha='right')
text(ax,x0+c,y0-5,r'$e_{21}$','varie','xl')
save(fig,'76-082')
