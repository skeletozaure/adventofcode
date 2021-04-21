Vous pénétrez dans un couloir, et face à vous, se trouve une porte verrouillée à côté de laquelle vous distinguez un digicode un peu bizarre. 
Il n'y a que deux touches, **0** et **Espace** ! 
Un message, vous explique que pour ouvrir la porte il va falloir taper en code unaire le message ***LET-ME-IN*** sur le digicode !
Code unaire, mais qu'est ce que c'est que ce truc ? le binaire OK, mais le unaire ???

*Une note à côté du digicode précise :*
- Le message encodé en sortie est constitué de blocs de  **0**
- Un bloc est séparé d'un autre bloc par un **espace**
- Deux blocs consécutifs servent à produire une série de bits de même valeur (que des  **1**  ou que des  **0**) :    
    - *Premier bloc* : il vaut toujours  **0**  ou  **00**. S'il vaut  **0**  la série contient des  **1**, sinon elle contient des  **0**  
    - *Deuxième bloc* : le nombre de  **0**  dans ce bloc correspond au nombre de bits dans la série
   
Prenons un exemple simple avec un message constitué d'un seul caractère : **C** majuscule. Le code ASCII de **C** en binaire vaut  **1000011** ( Attention le codage ASCII est sur 7bits)  ce qui donne avec la technique unaire :
- **0 0**  (la première série composée d'un seul  1)
- **00 0000**  (la deuxième série composée de quatre  0)
- **0 00**  (la troisième série composée de deux  1)

**C**  en unaire vaut donc :  **0 0 00 0000 0 00**

Deuxième exemple, nous voulons encoder le message **CC** (soit les 14 bits **10000111000011**) :

- **0 0**  (un seul  1)
- **00 0000**  (quatre  0)
- **0 000**  (trois  1)
- **00 0000**  (quatre  0)
- **0 00**  (deux  1)

**CC** vaut donc :  **0 0 00 0000 0 000 00 0000 0 00** 

A vous de jouer pour **LET-ME-IN**