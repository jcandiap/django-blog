# Aplicación: Blog

## Author
- [@jcandiap](https://github.com/jcandiap)

Esta es una aplicación web Django para una plataforma de blogs. Proporciona las siguientes funcionalidades:

## Funcionalidad 1: Índice

**URL:** /  
**Método HTTP:** GET  
**Descripción:** Muestra la página principal del blog con una lista de publicaciones ordenadas por fecha de publicación. Cada publicación incluye el número de comentarios y votos que ha recibido. Si un usuario está autenticado, también verifica si el usuario ya ha votado por cada publicación.

## Funcionalidad 2: Enviar

**URL:** /submit  
**Método HTTP:** GET, POST  
**Descripción:** Permite a un usuario autenticado enviar una nueva publicación al blog. Si el método de solicitud es GET, muestra el formulario de envío de publicaciones. Si el método de solicitud es POST, valida el formulario enviado y, si es válido, guarda la publicación en la base de datos y redirige al índice del blog. Si hay errores de validación, muestra los mensajes de error correspondientes en el formulario.

## Funcionalidad 3: Registro

**URL:** /register  
**Método HTTP:** GET, POST  
**Descripción:** Permite a un usuario registrarse en la plataforma del blog. Si el método de solicitud es GET, muestra el formulario de registro de usuarios. Si el método de solicitud es POST, valida el formulario enviado y, si es válido, crea un nuevo usuario en la base de datos y realiza el inicio de sesión automático, redirigiendo al índice del blog. Si hay errores de validación, muestra los mensajes de error correspondientes en el formulario.

## Funcionalidad 4: Inicio de sesión

**URL:** /login  
**Método HTTP:** POST  
**Descripción:** Permite a un usuario iniciar sesión en la plataforma del blog. Verifica las credenciales proporcionadas y, si son válidas, realiza el inicio de sesión y redirige al índice del blog. Si las credenciales no son válidas, muestra un mensaje de error.

## Funcionalidad 5: Detalle de la publicación

**URL:** /post_detail  
**Método HTTP:** GET  
**Descripción:** Muestra los detalles de una publicación específica, incluidos los comentarios asociados. El ID de la publicación se pasa como parámetro en la URL. Si no se encuentra la publicación, se redirige al índice del blog.

## Funcionalidad 6: Me gusta en una publicación

**URL:** /like_post  
**Método HTTP:** GET  
**Descripción:** Permite a un usuario autenticado dar me gusta o quitar el me gusta en una publicación. El ID de la publicación se pasa como parámetro en la URL. Si el usuario ya ha dado me gusta a la publicación, se quita el me gusta. Si el usuario aún no ha dado me gusta a la publicación, se agrega el me gusta. Después de realizar la acción, se redirige al índice del blog. Si el usuario no está autenticado, se redirige a la página de registro.

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jcandiap/)