## Informe de unidad

### Unidad: U2: Mi primer pipeline de datos con dlt y DuckDB

**Nombre:** Diana Raquel Moré (CI 3.625.595)
**Usuario GitHub:** dianamorefacet  
**Fecha:** 25 de Octubre de 2026  
**Tag de cierre:** u2-completa

#### Qué se hizo

En esta segunda unidad construí un pipeline de extracción y carga (EL) automatizado en Python utilizando la librería dlt para consumir datos paginados desde la API pública Rick and Morty API (https://rickandmortyapi.com/documentation), procesar la información de los personajes y almacenarla en una base de datos analítica DuckDB.

El pipeline obtiene automáticamente todas las páginas disponibles del catálogo de personajes utilizando el mecanismo de paginación provisto por la API. Posteriormente, los datos son transformados y cargados en una base de datos local llamada data.duckdb, permitiendo realizar consultas SQL de verificación y análisis.

##### Entorno

Trabajé sobre el entorno configurado en el Dev Container del repositorio. Verifiqué la instalación y funcionamiento de las dependencias dlt, duckdb, requests y pytest, asegurando que los comandos de validación, ejecución y pruebas funcionaran correctamente.

Asimismo, ejecuté los comandos sugeridos por la guía de la actividad para validar el pipeline, verificar los datos almacenados y comprobar el correcto funcionamiento de las pruebas unitarias.

##### Flujo de Git

Creé la rama de trabajo u2/dianamorefacet e incorporé todos los archivos dentro de la carpeta u2-pipeline/entregas/dianamorefacet/. Durante el desarrollo realicé commits pequeños y descriptivos para registrar cada avance de forma incremental, siguiendo las buenas prácticas de control de versiones.

Finalmente preparé el Pull Request correspondiente modificando exclusivamente los archivos contenidos dentro de mi carpeta de entrega.

#### Una decisión de diseño, explicada

Elegí utilizar la Rick and Morty API debido a que ofrece información estructurada, gratuita y paginada, lo que permite demostrar de forma clara el funcionamiento de un pipeline de extracción de datos.

Una decisión importante fue conservar únicamente atributos escalares relevantes de cada personaje: identificador, nombre, estado, especie, género, origen y ubicación. Aunque la API devuelve objetos anidados para algunos campos, decidí almacenar solamente los nombres de origen y ubicación para simplificar el esquema generado por dlt.

De esta manera se evita la creación de estructuras más complejas o tablas secundarias innecesarias, obteniendo una tabla única y fácil de consultar desde DuckDB.

Otra decisión de diseño fue incorporar un cooldown de 0.5 segundos entre solicitudes consecutivas a la API mediante time.sleep(). Aunque la cantidad de solicitudes realizadas no es excesiva, esta práctica ayuda a evitar sobrecargar el servicio remoto y demuestra un consumo responsable de recursos externos.

#### Un problema que apareció

Durante el desarrollo surgieron varios desafíos técnicos.

El primero fue comprender cómo dlt genera automáticamente los esquemas a partir de los datos emitidos por el recurso. Inicialmente evalué almacenar estructuras más complejas provenientes de la API, pero observé que simplificar los campos producía un esquema más limpio y adecuado para esta actividad.

El segundo problema apareció durante la implementación de las pruebas unitarias. Al simular errores de conexión utilizando mocks sobre requests.get, esperaba capturar directamente una excepción requests.ConnectionError. Sin embargo, durante la ejecución observé que dlt encapsula internamente los errores de extracción y los transforma en una excepción ResourceExtractionError.

Para resolver este inconveniente adapté la prueba correspondiente para validar correctamente la excepción generada por dlt, manteniendo la simulación del fallo de red mediante mocks. Esta experiencia permitió comprender mejor el funcionamiento interno de la librería y cómo gestiona los errores durante el proceso de extracción.

Adicionalmente implementé pruebas para respuestas vacías, validación de estructura de registros y comprobación de tipos de datos, logrando una suite de cinco pruebas unitarias reproducibles.

#### Reflexión y ayudas externas

##### Reflexión

Trabajar con dlt y DuckDB simplifica considerablemente la construcción de pipelines de datos. dlt abstrae gran parte del trabajo relacionado con la extracción, transformación ligera y carga de información, mientras que DuckDB proporciona un motor analítico rápido y fácil de utilizar sin necesidad de instalar o administrar un servidor de base de datos.

También resultó interesante observar cómo dlt maneja automáticamente la creación de esquemas y la administración del flujo de carga, permitiendo concentrarse principalmente en la lógica de negocio y la calidad de los datos.

Por otra parte, DuckDB facilitó la validación de resultados mediante consultas SQL sencillas. La posibilidad de almacenar los datos localmente en un único archivo simplifica enormemente el proceso de desarrollo y pruebas.

##### Ayudas externas

Para completar la tarea consulté la documentación oficial de dlt (https://dlthub.com/docs/), la documentación oficial de DuckDB (https://duckdb.org/docs/), la documentación oficial de Pytest (https://docs.pytest.org/) y la documentación pública de Rick and Morty API (https://rickandmortyapi.com/documentation).

Asimismo, utilicé Microsoft Copilot como herramienta de asistencia basada en inteligencia artificial para comprender ejemplos de integración con dlt, revisar buenas prácticas de testing, analizar errores relacionados con ResourceExtractionError, resolver inconvenientes surgidos durante las pruebas unitarias y mejorar la redacción final del informe técnico.

Todo el código entregado fue revisado, comprendido y adaptado antes de su inclusión en la solución final.

#### Qué harías distinto con más tiempo

Con más tiempo implementaría una estrategia de carga incremental para evitar reprocesar todos los personajes en cada ejecución. También incorporaría métricas de calidad de datos y validaciones automáticas del esquema generado por dlt.

Adicionalmente, ampliaría el script de verificación con consultas analíticas más avanzadas, como distribuciones por especie, género y ubicación, aprovechando las capacidades analíticas de DuckDB para generar indicadores más completos sobre los datos obtenidos desde la API.