# music_pro_

Este proyecto está diseñado para proporcionar a Music Pro un sistema integral que incluye:

1. Inicio de sesión y gestión de usuarios.
2. Creación de productos, con categorización y control de inventario.
3. Funcionalidad de carrito de compras.
4. Capacidad para realizar transacciones de compra en línea utilizando la biblioteca Pykhipu.

El sistema está basado en una arquitectura cliente-servidor, con las siguientes características:

1. Backend: Desarrollado utilizando el framework Flask y una base de datos NoSQL, específicamente Firebase, gestionada a través de la biblioteca FireO.
2. Frontend: Construido con Vue.js, que se encarga de consumir los endpoints proporcionados por Flask. La interfaz de usuario está estilizada con Bootstrap.
