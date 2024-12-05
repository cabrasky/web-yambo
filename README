# **Yambo - Asociación Juvenil de Alcobendas**

### **Descripción**

Este es el repositorio de la página web oficial de **Yambo**, una asociación infantojuvenil ubicada en Alcobendas. Puedes visitar el sitio en [yambo.ddns.net](http://yambo.ddns.net).  
Nuestra misión es proporcionar un espacio seguro y acogedor donde los niños y jóvenes puedan crecer, aprender y divertirse mientras fortalecen sus valores.

---

### **Índice**

1. [Descripción](#descripción)  
2. [Capturas de pantalla](#capturas-de-pantalla)  
3. [Características](#características)  
4. [Tecnologías utilizadas](#tecnologías-utilizadas)  
5. [Requisitos previos](#requisitos-previos)  
6. [Configuración del archivo .env](#configuración-del-archivo-env)  
7. [Instalación](#instalación)  
8. [Contribuir](#contribuir)  
9. [Licencia](#licencia)  
10. [Contacto](#contacto)  

---

### **Capturas de pantalla**

Aquí te mostramos algunas capturas de pantalla de nuestra página web:

[![Imagen de la página de inicio](docs/imgs/inicio.png)](docs/imgs/inicio.png)  
*Página de inicio*  

[![Imagen de la página de monitores](docs/imgs/monitores.png)](docs/imgs/monitores.png)
*Página de monitores*  

[![Imagen de la página de contacto](docs/imgs/contacto.png)](docs/imgs/contacto.png)  
*Página de contacto*  

---

### **Características**

- **Página de inicio:** Información general sobre la asociación y su misión.  
- **Página de proyectos:** Descripción de los diferentes proyectos que llevamos a cabo.  
- **Página de contacto:** Formulario para contactar con la asociación.  

---

### **Tecnologías utilizadas**

- [Django 4.1.1](https://www.djangoproject.com/)  
- [MariaDB 10.6](https://mariadb.org/)  
- [Bootstrap 5.2.1](https://getbootstrap.com/)  
- [Pillow 9.2.0](https://pillow.readthedocs.io/)  
- [python-decouple](https://pypi.org/project/python-decouple/)  

---

### **Requisitos previos**

Asegúrate de contar con los siguientes componentes instalados:

- **Python** 3.9 o superior  
- **pip** (Administrador de paquetes de Python)  
- **MariaDB** 10.6 o superior  
- **Entorno virtual** (opcional, pero recomendado): `virtualenv` u otro equivalente  

---

### **Configuración del archivo .env**

Este proyecto utiliza el paquete **python-decouple** para gestionar configuraciones sensibles. Antes de ejecutar la aplicación, crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
# Configuración general
SECRET_KEY=tu-clave-secreta
DEBUG=True

# Configuración de la base de datos
DB_NAME=yambo_db
DB_USERNAME=yambo_user
DB_PASSWORD=contraseña_segura
DB_HOST=localhost
DB_PORT=3306

# Configuración de correo
EMAIL_HOST=smtp.tu-proveedor.com
EMAIL_HOST_USER=tu-correo@example.com
EMAIL_HOST_PASSWORD=tu-contraseña
EMAIL_RECIPIENT=destinatario@example.com

# Configuración de hosts permitidos
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost,http://127.0.0.1
```

---

### **Instalación**

Sigue estos pasos para configurar y ejecutar la página web en tu entorno local:

```bash
# 1. Clona el repositorio
git clone https://github.com/cabrasky/web-yambo-dev.git

# 2. Accede al directorio del proyecto
cd web-yambo-dev

# 3. (Opcional) Crea y activa un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 4. Instala las dependencias
pip install -r requirements.txt

# 5. Crea el archivo .env en la raíz del proyecto y configura las variables de entorno según la sección anterior

# 6. Crea las migraciones e inicializa la base de datos
python manage.py makemigrations
python manage.py migrate

# 7. Inicia el servidor
python manage.py runserver
```

La aplicación estará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

### **Contribuir**

¡Tu ayuda es bienvenida! Puedes contribuir de las siguientes formas:

1. Reportando errores o sugerencias en la sección **Issues** del repositorio.  
2. Realizando un **Fork** del proyecto, desarrollando mejoras, y enviando un **Pull Request** con tus cambios.  

---

### **Licencia**

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

### **Contacto**

Si tienes preguntas o necesitas más información, no dudes en contactarnos:

- **Correo electrónico:** yamboalcobendas@gmail.com
- **Sitio web:** [yambo.ddns.net](https://yambo.ddns.net)  
- **Redes sociales:** [Instagram](https://www.instagram.com/yambo_jambo/)

---

🎉 **¡Gracias por tu interés en Yambo!**