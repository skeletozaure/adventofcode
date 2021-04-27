Si vous souhaitez passer au puzzle suivant, rafraichissez la page avec F5.

Si vous souhaitez que **votre solution** soit ajoutée, vous pouvez me l'envoyer par email et je l'ajouterai.

Une solution possible codée en *Python*. 

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

    return unary[:-1]

print(to_unary(message))
```

Une solution possible codée en *Natural* (**F.Simonnet**)

```
DEFINE DATA
LOCAL
1 #I         (N4)
1 #I2        (N4)
1 #LG-CHAINE (N4)
1 #CHAINE    (A1000)
1 #NB-REF    (N3) /* nombre de fois qu'on a le meme caractere
1 #A1-REF    (A1) /* le caract}re de r{f{rence,
1 #A1        (A1) /* le caract}re test{
1 #VAL1      (A2) INIT <'0'>
1 #VAL0      (A3) INIT <'00'>
1 #LET-ME-IN (A490) /* le code unaire @ saisir au clavier |
1 REDEFINE #LET-ME-IN
  2 #LET-ME-IN-70 (A70/1:7)
END-DEFINE
/* le resultat de LET-ME-IN en ASCII 7 bits (63 valeurs = 9 * 7 bits)
/* fait en externe car sur IBM = EBCDIC !
*
COMPRESS
  "100110010001011010100010110110011011000101010110110010011001110"
  INTO #CHAINE LEAVING NO
EXAMINE #CHAINE FOR ' ' GIVING LENGTH #LG-CHAINE
*
F1. FOR #I = 1 TO #LG-CHAINE
  #A1-REF := SUBSTR(#CHAINE,#I,1)
  #NB-REF := 0
  IF #A1-REF = '1'
    COMPRESS #LET-ME-IN #VAL1 '0' INTO #LET-ME-IN
  ELSE
    COMPRESS #LET-ME-IN #VAL0 '0' INTO #LET-ME-IN
  END-IF
  NEWPAGE(0)
  F2. FOR #I2 = (#I + 1) TO #LG-CHAINE
    #A1 := SUBSTR(#CHAINE,#I2,1)
    IF #A1-REF = #A1
      ADD 1 TO #NB-REF
      COMPRESS #LET-ME-IN #A1-REF INTO #LET-ME-IN LEAVING NO
    ELSE
      ESCAPE BOTTOM (F2.)
    END-IF
  END-FOR
  ADD #NB-REF TO #I /* on avance de ce qu'on a deja lu
END-FOR
WRITE '=' #LET-ME-IN-70(*)
END
```


