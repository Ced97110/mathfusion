import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
rows=[('Isoler un radical','$\\sqrt{2m+3}=\\sqrt{m-8}$','fixe'),('Élever au carré','$2m+3=m-8$','fixe'),('Résoudre','$m=-11$','sujet')]
h=12; g=7; y=66-4-h
for i,(a,e,role) in enumerate(rows):
    yy=y-i*(h+g)
    text(ax,17,yy+h/2,a,'varie','s')
    box(ax,34,yy,50,h,role,label=e,size='m')
    if i<2: arrow(ax,(59,yy),(59,yy-g),'varie')
text(ax,59,6,'candidat : pas encore vérifié','fixe','s')
save(fig,'22-139')
