import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *

def sq(ax,x,y,s,role):
    poly(ax,[(x,y),(x+s,y),(x+s,y+s),(x,y+s)],role,lw=0.4)

def bar(ax,x0,yc,n,role,s=1.4):
    for i in range(n):
        sq(ax,x0+i*s,yc-s/2,s,role)

def plus(ax,x,y,r=1.2):
    line(ax,[(x-r,y),(x+r,y)],'encre',lw=0.8)
    line(ax,[(x,y-r),(x,y+r)],'encre',lw=0.8)

fig,ax=canvas(74)
text(ax,44,70.5,'une seule lettre','sujet','s')
# la forme b + b + b + b
for x in (22,34,46,58):
    box(ax,x,58,8,8,'sujet',label='b',size='l')
for x in (32,44,56):
    plus(ax,x,62)
# b = 6 : quatre barres de 6 carrés
text(ax,3,46,r'$b = 6$','varie','m',ha='left')
for x in (22,32.4,42.8,53.2):
    bar(ax,x,46,6,'varie')
# b = 9 : quatre barres de 9 carrés
text(ax,3,32,r'$b = 9$','varie','m',ha='left')
for x in (22,36.6,51.2,65.8):
    bar(ax,x,32,9,'varie')
# lettres différentes : longueurs 6, 9, 2, 5
text(ax,3,16,r'$p+q+r+s$','limite','m',ha='left')
for x,n in ((22,6),(32.4,9),(47,2),(51.8,5)):
    bar(ax,x,16,n,'limite')
text(ax,62,16,'peuvent différer','limite','s',ha='left')
save(fig,'03-017')
