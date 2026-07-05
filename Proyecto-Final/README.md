# Proyecto Final - Automation Testing QA
## Propósito del proyecto
Aplicar pruebas de interzas sobre la plataforma de **SauceDemo** y pruebas de servicios utilizando la API pública **ReqRes**. Desarrollando un framework de automatización.

---

## Tecnologías Utilizadas
- **Lenguaje Principal:** Python 3.13
- **Framework de Testing:** Pytest 9.0.3
- **Automatización Web:** Selenium WebDriver 4.x
- **Generación de Reportes:** Pytest-HTML

---

## Estructura del Proyecto
Implementación del patrón de diseño **Page Object Model (POM)**
```text
|-- data/           # Fuente de datos externas
|-- logs/           # Historial y registros de la ejecución
|-- pages/          # Clases del Page Object Model
|-- reports/        # Reportes generados dinámicamente (HTML y capturas de pantallas)
|-- test/           # Pruebas automatizadas (UI y API)
|-- utils/          # Módulos auxiliares
|-- README.md       # Documentación Técnica
