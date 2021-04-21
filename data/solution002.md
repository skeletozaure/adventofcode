A titre d'exemple, voilà une solution possible codée en Python. Si vous souhaitez que votre solution soit ajoutée, vous pouvez me l'envoyer par email et je l'ajouterai.

```python
import re
message = "LET-ME-IN"

def to_unary(my_string):
    bin_conv=''
    unary = ''

    for c in my_string:
        #formattage en binaire sur 7 positions
        bin_conv += f'{ord(c):07b}'

    for group in re.findall("(0+|1+)", bin_conv):
        if '0' in group:
            unary+= '00 ' + '0' * len(group) + ' '
        else:
            unary+= '0 ' + '0' * len(group) + ' '

    return unary[0:len(unary)-1]

print(to_unary(message))
```

Si vous souhaitez passer au puzzle suivant, rafraichissez la page avec F5