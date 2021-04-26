Si vous souhaitez passer au puzzle suivant, rafraichissez la page avec F5

Si vous souhaitez que **votre solution** soit ajoutée, vous pouvez me l'envoyer par email et je l'ajouterai.

Une solution possible codée en *Python*. 

```python
instructions = '52554437147555553177771524418267843219182859995942215316362429449983637161192948458385799435625432472399695557917723926815678834498379821192395363253412635244153971238243584678919637629487233277745457'
digits = [int(nb) for nb in instructions]
solution = sum(n for i, n in  enumerate(digits) if n == digits[i-1])
print(solution)
```

Une solution possible codée en *Natural* (**F.Simonnet**)

```
DEFINE DATA                                                             
LOCAL                                                                   
1 £I (N4)                                                               
1 £I2(N4)                                                               
1 £LG-CHAINE (N3)                                                       
1 £VALEUR(N1)                                                           
1 £TOTAL(N8)                                                            
1 £CHAINE (A1000) /* plus c'est long mieux c'est                        
1 £A1     (A1) /* plus c'est court, plus c'est facile                   
END-DEFINE                                                              
COMPRESS                                                                
  "52554437147555553177771524418267843219182859995942215316362429449983"
  "63716119294845838579943562543247239969555791772392681567883449837982"
  "1192395363253412635244153971238243584678919637629487233277745457"    
  INTO £CHAINE LEAVING NO                                               
EXAMINE £CHAINE FOR ' ' GIVING LENGTH £LG-CHAINE                        
COMPRESS £CHAINE SUBSTRING (£CHAINE,1,1) TO £CHAINE LEAVING NO          
FOR £I = 1 TO £LG-CHAINE                                                
  £I2 := £I + 1                                                         
  £A1 := SUBSTR(£CHAINE,£I,1)                                           
  IF £A1 = SUBSTR(£CHAINE,£I2,1)                                        
    £TOTAL:= £TOTAL + VAL(£A1)                                          
  END-IF                                                                
END-FOR                                                                 
WRITE '=' £TOTAL                                                        
END
```



