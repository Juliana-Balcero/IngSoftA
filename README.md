# Beads App
Beads es una App que consiste en manejar las cuentas ya sea de un usuario o más,
con la finalidad de almacenar, registrar y manejar gastos de una pareja, grupo familiar,
etc. Primeramente, en nuestra App se registra un primer usuario, el cuál puede anexar
en su grupo a otras personas y a partir de allí cada uno es capaz de acceder a
información acerca de dinero disponible, información de cantidades gastadas por los
otros usuarios del grupo y demás.


### Pre-requisitos 📋


```
Durante un periodo de cuatro semanas se establecieron las bases que todo ingeniero
de sistemas y desarrollador de software debe tener presente a la hora de realizar su
labor, los dos temas a destacar son:

- Ética En la ingeniería de Software: En el desarrollo de software se pueden
presentar algunos conflictos éticos y profesionales de gran relevancia, por
tanto, la persona a cargo debe estar en la capacidad de saber sobrellevar estos
de tal manera que impacten en el menor grado a todos los involucrados y que
en la medida de lo posible sea consciente de la información que puede llegar
a estar en su poder. 

- Aprendizaje de metodologías ágiles: Estudio de los métodos de desarrollo ágil
de software y el manifiesto ágil, así como de las distinciones entre el desarrollo
ágil y el dirigido. Esto, con el fin de tener conocimiento de las prácticas en la 
programación extrema y su similitud con los principios generales de los
métodos ágiles. Por otra parte, es vital entender el enfoque de Scrum para la
administración de un proyecto ágil. 
```

* **Contando con una base conceptual, el primer paso a efectuar es el desarrollo del ciclo
de los requerimientos funcionales y no funcionales por parte de los interesados.**
<br/><br/>
### Instalación 🔧


* **Configurando el entorno**

Windows PowerShell
Copyright (C) Microsoft Corporation. Todos los derechos reservados.

PS C:\Users\Equipo> **pip install flask**

Requirement already satisfied: flask in c:\users\equipo\anaconda3\lib\site-packages (1.1.1)

Requirement already satisfied: Werkzeug>=0.15 in c:\users\equipo\anaconda3\lib\site-packages (from flask) (1.0.0)

Requirement already satisfied: itsdangerous>=0.24 in c:\users\equipo\anaconda3\lib\site-packages (from flask) (1.1.0)

Requirement already satisfied: Jinja2>=2.10.1 in c:\users\equipo\anaconda3\lib\site-packages (from flask) (2.11.1)

Requirement already satisfied: click>=5.1 in c:\users\equipo\anaconda3\lib\site-packages (from flask) (7.0)

Requirement already satisfied: MarkupSafe>=0.23 in c:\users\equipo\anaconda3\lib\site-packages (from Jinja2>=2.10.1->flask) (1.1.1)

PS C:\Users\Equipo>

PS C:\Users\Equipo> **pip install virtualenv**

Requirement already satisfied: virtualenv in c:\users\equipo\anaconda3\lib\site-packages (20.0.21)

Requirement already satisfied: appdirs<2,>=1.4.3 in c:\users\equipo\anaconda3\lib\site-packages (from virtualenv) (1.4.4)

Requirement already satisfied: filelock<4,>=3.0.0 in c:\users\equipo\anaconda3\lib\site-packages (from virtualenv) (3.0.12)

Requirement already satisfied: importlib-metadata<2,>=0.12; python_version < "3.8" in c:\users\equipo\anaconda3\lib\site-packages (from virtualenv) (1.5.0)

Requirement already satisfied: six<2,>=1.9.0 in c:\users\equipo\anaconda3\lib\site-packages (from virtualenv) (1.14.0)

Requirement already satisfied: distlib<1,>=0.3.0 in c:\users\equipo\anaconda3\lib\site-packages (from virtualenv) (0.3.0)

Requirement already satisfied: zipp>=0.5 in c:\users\equipo\anaconda3\lib\site-packages (from importlib-metadata<2,>=0.12; 

python_version < "3.8"->virtualenv) (2.2.0)

PS C:\Users\Equipo>

PS C:\Users\Equipo> **virtualenv venv -p python3**

created virtual environment CPython3.7.6.final.0-64 in 16696ms

creator CPython3Windows(dest=C:\Users\Equipo\venv, clear=False, global=False)

seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy,

app_data_dir=C:\Users\Equipo\AppData\Local\pypa\virtualenv\seed-app-data\v1.0.1

activators BashActivator,BatchActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

PS C:\Users\Equipo>

* **Ahora en el símbolo del sistema**

Microsoft Windows [Versión 10.0.17763.1282]
(c) 2018 Microsoft Corporation. Todos los derechos reservados.

C:\Users\Equipo>**cd C:\Users\Equipo\venv**

C:\Users\Equipo\venv>**cd Scripts**

C:\Users\Equipo\venv\Scripts>**activate**

(venv) C:\Users\Equipo\venv\Scripts>**cd ..**

(venv) C:\Users\Equipo\venv>**app1.py**

(venv) C:\Users\Equipo\venv>**pip install Flask**

Requirement already satisfied: Flask in c:\users\equipo\venv\lib\site-packages (1.1.2)
Requirement already satisfied: click>=5.1 in c:\users\equipo\venv\lib\site-packages (from Flask) (7.1.2)
Requirement already satisfied: Werkzeug>=0.15 in c:\users\equipo\venv\lib\site-packages (from Flask) (1.0.1)
Requirement already satisfied: itsdangerous>=0.24 in c:\users\equipo\venv\lib\site-packages (from Flask) (1.1.0)
Requirement already satisfied: Jinja2>=2.10.1 in c:\users\equipo\venv\lib\site-packages (from Flask) (2.11.2)
Requirement already satisfied: MarkupSafe>=0.23 in c:\users\equipo\venv\lib\site-packages (from Jinja2>=2.10.1->Flask) (1.1.1)

(venv) C:\Users\Equipo\venv>**python app1.py**
 * Serving Flask app "app1" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

<br/><br/>
## Diseño Arquitectónico 📦
<br/><br/>
![Sin título2](https://user-images.githubusercontent.com/66752504/84430300-1bca5600-abef-11ea-8028-cb76ae849ffe.jpg)


## Diagrama de clases ⚙️

<br/><br/>
![Sin título3](https://user-images.githubusercontent.com/66752504/84430869-f38f2700-abef-11ea-9db6-1be54b17f985.jpg)



<br/><br/>
## Salidas de la Base de Datos 🔩


![3cca1588-fde9-48c1-9c4c-3ed0518773d8](https://user-images.githubusercontent.com/66752504/84427180-19b1c880-abea-11ea-840e-e135d6290cbf.jpg)



![e9f0a765-ca7f-465f-a3f6-a376a539b4ca](https://user-images.githubusercontent.com/66752504/84427186-1e767c80-abea-11ea-95c4-04af0d9bb12f.jpg)




<br/><br/>
## Salidas de al app ⌨️

![f39b4e93-95c9-44cd-b8b6-acb97c4d1652](https://user-images.githubusercontent.com/66752504/84426767-62b54d00-abe9-11ea-90f3-4651ec1a5e6e.jpg)


<br/><br/>
## Construido con 🛠️

Para esta parte de desarrollo se tuvo en consideración los conocimientos que
tenemos los integrantes del grupo, de ahí se decidió utilizar 

* Python (lenguaje de
programación)
* Flask (framework) 
* MySQL (base de datos)

<br/><br/>

## Autores ✒️

* **Juliana Balcero** - *Implementación de la App*
* **César Badillo** - *Implementación de la App* 
* **Juan David Ruiz** - *Documentación*
* **Luigi Cano Valdes** - *Documentación*

 
<br/><br/>
## Agradecimientos 🎁


* Invito a mi grupo a una  cerveza 🍺  
* Gracias a todos por su aporte 🤓.





