# Python-Ejercicios

## Ejercicio 1
Este ejercicio simula un perfil de usuario en una red social, con información sobre el usuario, sus amigos y publicaciones. El objetivo es realizar algunas modificaciones en estos datos. A través de las operaciones que se realizan, puedes agregar, modificar y eliminar elementos dentro de las estructuras de datos. El código imprime la información antes y después de los cambios.

### El ejercicio está estructurado en tres partes principales:

**Datos iniciales**: El usuario, la lista de amigos y las publicaciones.  
**Modificaciones**: Se realiza un cambio en los datos: agregar una nueva publicación, modificar un dato del usuario (como la ciudad) y eliminar un amigo de la lista.  
**Impresión de los resultados:** Se muestran los datos antes y después de las modificaciones.  

### Explicacion de Solucion

**Agregar un nuevo post:** Se añade una nueva entrada a la variable posts, asignándole contenido, cantidad de "likes" y comentarios.  
**Modificar un dato del usuario:** Se cambia el valor de la clave "Ciudad" dentro del diccionario usuario.  
**Eliminar un amigo de la lista:** Se usa el método pop() para eliminar el segundo amigo de la lista amigos, que tiene el índice 1.
**Mostrar los resultados:** Se imprimen los datos del usuario, amigos y publicaciones, antes y después de las modificaciones, para visualizar los cambios.

## Ejercicio 2

Este ejercicio maneja un sistema simple de productos, pedidos y clientes registrados. Realiza las siguientes operaciones:  

**Muestra los pedidos actuales:** Muestra los detalles de los pedidos como el ID, el email del cliente, los productos comprados y el estado del pedido.  
**Muestra los productos actuales:** Muestra el ID, el nombre, el precio y la cantidad de cada producto disponible.  
**Añadir un nuevo producto:** Se agrega un producto adicional ("Chaqueta") al catálogo.  
**Cambiar el estado de un pedido:** El estado del pedido con ID 101 se actualiza a "Entregado".  
**Mostrar pedidos de un cliente por email:** Permite al usuario ingresar un correo electrónico y muestra los productos de los pedidos asociados a ese cliente.  

**Breve explicación de la solución:**  

**Mostrar pedidos y productos:** El código recorre los diccionarios pedidos y productos e imprime la información de cada uno.  
**Añadir un nuevo producto:** Se inserta un nuevo producto al diccionario productos utilizando un nuevo ID (id5).  
**Actualizar el estado de un pedido:** Se busca el pedido con ID 101 en la lista de pedidos y se cambia su estado a "Entregado".  
**Mostrar pedidos por cliente:** El programa solicita un correo electrónico, busca los pedidos asociados a ese correo y muestra los productos de esos pedidos. Si no hay pedidos para el correo proporcionado, imprime un mensaje de error.  

## Ejercicio 3

Este ejercicio simula la gestión de estudiantes, cursos y notas en un sistema educativo. El objetivo es realizar las siguientes tareas:

**1. Agregar un estudiante** y matricularlo en un curso.  
**2. Consultar estudiantes por curso:** El usuario ingresa el nombre de un curso y el sistema muestra los estudiantes matriculados en él.  
**3. Mostrar información detallada de los estudiantes:** Muestra los estudiantes, sus cursos, horarios, profesores y sus notas.  

**Breve explicación de la solución:**

**Agregar un nuevo estudiante:** Se agrega un nuevo estudiante ("Jorge Trejo") a la lista estudiantes.  
**Matriculación del estudiante en un curso:** Jorge es matriculado en el curso "Des. Aplicaciones con acceso a datos", añadiéndose a la lista de estudiantes de ese curso.  
**Promedio de notas de un estudiante:** El código calcula el promedio de las notas del primer estudiante (Paula Casas) en el primer curso.  
**Entrada del usuario:** El sistema solicita al usuario que ingrese el nombre de un curso y luego muestra la lista de estudiantes matriculados en ese curso.  
**Lista final con cursos y notas:** El código genera una lista que muestra, para cada estudiante, los cursos a los que está matriculado, junto con los horarios, profesores y las notas asociadas.  

