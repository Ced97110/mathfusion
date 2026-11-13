import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
rows=[('Repérer l’angle droit','$c$ en face de l’angle','fixe'),
('Carré de $a$ et de $b$','$3^2=9$ ; $4^2=16$','varie'),
('Additionner','$9+16=25$','varie'),
('Lire le total','$c^2=25$','resultat')]
h=11; g=4; y=78-4-h
for i,(a,r,role) in enumerate(rows):
    yy=y-i*(h+g)
    box(ax,3,yy,34,h,'varie' if role!='fixe' else 'fixe',label=a,size='s')
    arrow(ax,(37,yy+h/2),(45,yy+h/2),'varie')
    box(ax,45,yy,40,h,role if role!='varie' else 'sujet',label=r,size='s')
    if i<3: arrow(ax,(20,yy),(20,yy-g),'fixe')
text(ax,44,5,'$c$ reste à trouver','fixe','s')
save(fig,'22-131')
