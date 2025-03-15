# Diagrama de Red

Produzca un diagrama de red (puede utilizar lucidchart) de una aplicación web en GCP o AWS y escriba una descripción de texto de 1/2 a 1 página de sus elecciones y arquitectura.

El diseño debe soportar:
- Cargas variables
- Contar con HA (alta disponibilidad)
- Frontend en Js
- Backend con una base de datos relacional y una no relacional
- La aplicación backend consume 2 microservicios externos

El diagrama debe hacer un mejor uso de las soluciones distribuidas.

# Solución

Para la solución de este apartado, se eligió deployar el sistema en AWS.

Se comenzó armando el diagrama para el front. A pesar de que no se detalla en el enunciado, se asume que se utilizará:
- Cloudfront como CDN
- S3 para almacenamiento de archivos estáticos
- Una instancia de [App Runner](https://aws.amazon.com/es/apprunner/) para la aplicación en sí
    - Se eligió este servicio dado que se encarga de escalar automáticamente según el tráfico, y equilibra la carga del mismo. Probablemente hayan formas más baratas/eficientes de lograr esto, se eligió esta forma porque fue lo que se encontró googleando y, aparentemente, cumple con los requerimientos pedidos (escalabilidad y disponibilidad)
- Sentry para monitoreo
- PostHog para analytics

No se pidió en el enunciado que se agregara nada específico para el monitoreo ni las analytics en el front, pero se agregó de todas formas. Se eligieron Sentry y PostHog por familiaridad previa, y por dar ambas la posibilidad de usar el servicio provisto por las empresas o self-hostearlas según las necesidades del cliente.

Teniendo esto en cuenta, se diseñó el diagrama de esta parte de la red, quedando el mismo de la siguiente forma:



# Referencias

