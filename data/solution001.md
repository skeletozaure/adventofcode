A titre d'exemple, voilà une solution possible codée en Python. Si vous souhaitez que votre solution soit ajoutée, vous pouvez me l'envoyer par email et je l'ajouterai.

```python
instructions = '52554437147555553177771524418267843219182859995942215316362429449983637161192948458385799435625432472399695557917723926815678834498379821192395363253412635244153971238243584678919637629487233277745457'
digits = [int(nb) for nb in instructions]
solution = sum(n for i, n in  enumerate(digits) if n == digits[i-1])
print(solution)
```

Si vous souhaitez passer au puzzle suivant, rafraichissez la page avec F5