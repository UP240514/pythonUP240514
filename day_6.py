#Ejercicio 1
tupla=()
siblings=('karla', 'jorge', 'aaron')
print("tengo ", len(siblings),"hermanos")
padres=('gila','martin')
fmly_mmbrs=padres + siblings
print(fmly_mmbrs)

#ejercicio 2
fruits=('naranja','manzana','uva')
vegetables=('calabaza','lechuga','brocoli')
animals=('carne','leche','queso')
food_stuff_tp= fruits + vegetables + animals 
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)
mitad_items=food_stuff_lt[4:]
print(mitad_items)
pr_tr_ul_tr=food_stuff_lt[3:6]
print(pr_tr_ul_tr)
del food_stuff_tp
print(food_stuff_tp)