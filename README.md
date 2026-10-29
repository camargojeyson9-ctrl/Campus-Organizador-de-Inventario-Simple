# Campus-Organizador-de-Inventario-Simple

Imagina que estás desarrollando un sistema para una pequeña tienda o para gestionar el inventario de un personaje en un videojuego. Necesitas crear una herramienta de consola simple que permita al usuario administrar una lista de objetos.



Tu tarea es construir una aplicación interactiva que se ejecute en un bucle y presente al usuario un menú de opciones para gestionar un inventario. El inventario se almacenará en una única lista. El programa debe ser capaz de procesar las siguientes acciones:

Agregar un ítem: El usuario podrá añadir un nuevo objeto al inventario. Para hacerlo más interesante, el programa debe evitar que se agreguen ítems duplicados.
Remover un ítem: El usuario podrá eliminar un objeto existente del inventario. El programa debe verificar primero si el objeto se encuentra en la lista antes de intentar eliminarlo.
Mostrar el inventario: El programa deberá imprimir una lista con todos los objetos que se encuentran actualmente en el inventario.
Verificar un ítem: El usuario podrá consultar si un objeto específico ya existe en el inventario.
Salir: La opción para terminar el programa.

Resultado esperado

El programa debe presentar al usuario un menú de opciones dentro de un bucle. El usuario interactúa seleccionando un número para realizar una acción. El programa debe responder a cada acción con un mensaje claro y actualizar el estado del inventario según corresponda.



Ejemplo de una Sesión de Usuario Completa:

El siguiente bloque muestra cómo debería verse la interacción en la consola, cubriendo todas las funcionalidades y el manejo de casos comunes.

--- Organizador de Inventario ---
1. Agregar ítem
2. Remover ítem
3. Mostrar inventario
4. Verificar ítem
5. Salir

Elige una opción: 3
Tu inventario está vacío.

--- Organizador de Inventario ---
1. Agregar ítem
2. Remover ítem
3. Mostrar inventario
4. Verificar ítem
5. Salir

Elige una opción: 1
Ingresa el nombre del ítem a agregar: Espada
'Espada' ha sido agregado al inventario.

--- Organizador de Inventario ---
1. Agregar ítem
2. Remover ítem
3. Mostrar inventario
4. Verificar ítem
5. Salir

Elige una opción: 1
Ingresa el nombre del ítem a agregar: Pocion
'Pocion' ha sido agregado al inventario.

--- Organizador de Inventario ---
1. Agregar ítem
2. Remover ítem
3. Mostrar inventario
4. Verificar ítem
5. Salir

Elige una opción: 1
Ingresa el nombre del ítem a agregar: Espada
El ítem 'Espada' ya existe en el inventario.

--- Organizador de Inventario ---
1. Agregar ítem
2. Remover ítem
3. Mostrar inventario
4. Verificar ítem
5. Salir

Elige una opción: 3
--- Inventario Actual ---
- Espada
- Pocion
-------------------------

--- Organizador de Inventario ---
1. Agregar ítem
2. Remover ítem
3. Mostrar inventario
4. Verificar ítem
5. Salir

Elige una opción: 4
Ingresa el nombre del ítem a verificar: Escudo
El ítem 'Escudo' no se encuentra en el inventario.

--- Organizador de Inventario ---
1. Agregar ítem
2. Remover ítem
3. Mostrar inventario
4. Verificar ítem
5. Salir

Elige una opción: 2
Ingresa el nombre del ítem a remover: Llave
El ítem 'Llave' no se encuentra en el inventario.

--- Organizador de Inventario ---
1. Agregar ítem
2. Remover ítem
3. Mostrar inventario
4. Verificar ítem
5. Salir

Elige una opción: 2
Ingresa el nombre del ítem a remover: Pocion
'Pocion' ha sido removido del inventario.

--- Organizador de Inventario ---
1. Agregar ítem
2. Remover ítem
3. Mostrar inventario
4. Verificar ítem
5. Salir

Elige una opción: 5
Gracias por usar el organizador de inventario. ¡Hasta luego!
