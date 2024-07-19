
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

#init: es lo que va a a inicializar mi modelo (class). Siempre va a recibir self (no es una palabra reservada pero
# se usa por convenio). Self hace referencía a sí mismo, recibe a este mismo elemento y a last_name, que será el 
#primer elemento que reciba nuestra clase (self.last_name = last_name
# El doble guion bajo significa que tiene una función escondida y qué solo se puede ejecutar en esta clase. 
# Sólo se utiliza una sola vez, en el momento en el que se crea. Sirve para generar una misma estructira de familia, pero
# pudiendo crear muchas familias a la vez. 

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

   
    # Genera IDs aleatorios al crear a un nuevo miembro en la familia. 
    # Tiene un guión bajo a diferencia del resto porque sólo vamos a poder usarlo dentro de esta clase, no fuera. 
    # Es un método para el funcionamiento de la clase. 
    def _generateId(self):
        return randint(0, 99999999)

    # MÉTODO AÑADIR MIEMBROS: Va a recibirse a sí mismo y al miembreo que se va a añadir. Se va a hacer generando el ID
    # y añadiendo el last_name ("Jackson")
    # member['last_name'] = self.last_name -> recibe el valor que se haya asignado al generar una familia nueva ("Jackson")
    # member['id'] = self._generateId() -> llama al método privado que genera el id que tendrá el nuevo miembro
    # member['lucky_numbers'] -> convierte en lista lo que le llega al acceder al atribututo l_n del miembro, si no tuviese ninguno crea con el set una lista vacía 
    # Por ultimo añade el miembro a members con un .append y devuelve miembro. 
    def add_member(self, member):
        member['last_name'] = self.last_name
        member['id'] = self._generateId()
        member['lucky_numbers'] = list(member.get('lucky_numbers', set()))
        self._members.append(member)
        return member

    def delete_member(self, id):
        member_to_remove = None
        for member in self._members:
            if member['id'] == id:
                member_to_remove = member
                break        
        if member_to_remove:
            self._members.remove(member_to_remove)
        
        return self._members


    def get_member(self, id):
        member_to_show = None
        for member in self._members:
            if member['id'] == id:
                member_to_show = member
                break
        return member_to_show
    
  
    def get_all_members(self):
        return self._members
