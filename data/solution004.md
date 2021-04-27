**Bravo**, grâce à vous le Le Père Noël a pu trouver le bon étage ! Avouez, c'était plus facile que les précédents puzzle :wink: Encore un ou deux, et ça va se corser :grinning:.

A titre d'exemple, voilà une solution possible codée en Python. Si vous souhaitez que votre solution soit ajoutée, vous pouvez me l'envoyer par email et je l'ajouterai.

```python
# les données d'entrée du puzzle ont été sauvées dans le fichier
# santa2021_01.txt
f = open('inputs/santa2021_01.txt')
contents = f.read()
print("Floor:", contents.count('(') - contents.count(')'))
```

Si vous souhaitez passer au puzzle suivant, rafraichissez la page avec F5