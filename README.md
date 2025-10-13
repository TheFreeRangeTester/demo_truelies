# Chatbot Test Project 🤖

Un proyecto de chatbot desarrollado en Python con capacidades de procesamiento de lenguaje natural y validación automatizada de respuestas usando **True Lies Validator**.

## 🚀 Configuración Inicial

### 1. Crear y activar entorno virtual

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate  # En macOS/Linux
# o
venv\Scripts\activate     # En Windows
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
pip install true-lies-validator>=0.8.0
```

### 3. Configurar variables de entorno

```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

## 📁 Estructura del Proyecto

```
chatbot-test/
├── .github/
│   └── workflows/          # GitHub Actions workflows
│       ├── test-and-report.yml
│       └── README.md
├── venv/                   # Entorno virtual
├── tests/                  # Tests con True Lies
│   ├── test_chatbot.py
│   └── test_clinic.py
├── true_lies_reporting/    # Reportes y datos históricos
│   └── validation_history.json
├── *.html                  # Reportes HTML generados
├── requirements.txt        # Dependencias
├── .gitignore             # Archivos a ignorar
└── README.md              # Este archivo
```

## 🛠️ Desarrollo

### Ejecutar tests localmente

```bash
# Ejecutar todos los tests
pytest tests/ -v

# Ejecutar un test específico
pytest tests/test_clinic.py -v
```

Los tests generarán reportes HTML automáticamente en el directorio raíz y en `true_lies_reporting/`.

### 🎭 Validación con True Lies

Este proyecto usa **True Lies Validator** para validar las respuestas del chatbot. Los tests evalúan:

- ✅ **Similitud semántica**: ¿La respuesta transmite el mismo significado?
- ✅ **Exactitud factual**: ¿Los datos extraídos son correctos?
- ✅ **Análisis de polaridad**: ¿El tono es apropiado?

#### Ver reportes localmente

Después de ejecutar los tests, abre cualquier archivo `.html` en tu navegador:

```bash
# En macOS
open clinic_semana_1.html

# En Linux
xdg-open clinic_semana_1.html

# En Windows
start clinic_semana_1.html
```

### 📊 GitHub Actions - Integración Continua

El proyecto incluye un workflow de GitHub Actions que:

1. ✅ Ejecuta automáticamente los tests en cada push/PR
2. 📊 Genera reportes HTML con True Lies
3. 📈 Preserva el historial de validaciones para trends
4. 📦 Publica los reportes como artifacts descargables
5. 💬 Comenta en PRs con resumen de resultados

#### Descargar reportes de GitHub Actions

1. Ve a la pestaña **Actions** de tu repositorio
2. Selecciona la ejecución del workflow
3. Descarga el artifact `true-lies-reports-[número]`
4. Descomprime y abre `index.html`

📖 Para más detalles, consulta [`.github/workflows/README.md`](.github/workflows/README.md)

### Formatear código

```bash
black tests/
```

### Verificar estilo de código

```bash
flake8 tests/
```

## 🛠️ Tecnologías

- **Python 3.13** - Lenguaje de programación
- **True Lies Validator** - Validación de respuestas LLM
- **pytest** - Framework de testing
- **NLTK** - Procesamiento de lenguaje natural
- **GitHub Actions** - Integración continua
- **scikit-learn** - Machine Learning

## 📝 Notas

- Este proyecto usa True Lies para validación automática de respuestas de chatbot
- Los reportes HTML incluyen métricas detalladas y visualizaciones interactivas
- El historial de validaciones permite tracking de métricas a lo largo del tiempo
- GitHub Actions ejecuta los tests automáticamente y preserva el historial

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request
