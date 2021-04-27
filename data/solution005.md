**Bravo**, grâce à vous le Le Père Noël a pu trouver le sous sol ! Oui, c'était encore facile cette fois, les difficultés arrivent :grinning:.

A titre d'exemple, voilà une solution possible codée en Python. Si vous souhaitez que votre solution soit ajoutée, vous pouvez me l'envoyer par email et je l'ajouterai.

```python
# les données d'entrée du puzzle ont été sauvées dans le fichier
# santa2021_01.txt
f = open('inputs/santa2021_01.txt')
contents = f.read()

change = {'(': 1, ')': -1}

floor = 0
position = 1
for c in contents:
    if c in change:
        floor += change[c]
    if floor == -1:
        print("Basement entered at position:", position)
        break
    position += 1
```

Si vous souhaitez passer au puzzle suivant, rafraichissez la page avec F5