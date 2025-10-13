# 🎭 GitHub Actions - True Lies Testing

Este workflow ejecuta automáticamente tus tests de True Lies y genera reportes HTML que puedes descargar como artifacts.

## 🚀 Características

- ✅ **Ejecución automática** en push y pull requests
- 📊 **Generación de reportes HTML** con True Lies Validator
- 📈 **Preservación del historial** de validaciones entre ejecuciones
- 🎨 **Página índice elegante** para navegar los reportes
- 📦 **Artifacts descargables** con retención de 30 días
- 💬 **Comentarios automáticos** en Pull Requests con resumen de resultados

## 📋 ¿Cuándo se ejecuta?

El workflow se ejecuta automáticamente cuando:

- Haces push a las ramas `main`, `master` o `develop`
- Creas o actualizas un Pull Request hacia estas ramas
- Lo ejecutas manualmente desde la pestaña Actions (workflow_dispatch)

## 📦 Cómo descargar los reportes

### Opción 1: Desde la página de Actions

1. Ve a la pestaña **Actions** de tu repositorio
2. Selecciona la ejecución del workflow que te interesa
3. En la sección **Artifacts**, busca `true-lies-reports-[número]`
4. Haz clic para descargar el archivo ZIP
5. Descomprime y abre `index.html` en tu navegador

### Opción 2: Desde un Pull Request

Si el workflow se ejecutó en un PR, verás un comentario automático con:

- Resumen de los resultados del test
- Enlace directo a los artifacts de esa ejecución

## 📈 Historial de validaciones

El archivo `validation_history.json` se preserva entre ejecuciones usando el sistema de cache de GitHub Actions. Esto permite que True Lies genere gráficos de tendencias mostrando la evolución de tus métricas a lo largo del tiempo.

El historial se guarda con cada ejecución y se restaura automáticamente en la siguiente, permitiendo ver:

- Tendencias de tasa de éxito
- Evolución de similitud semántica
- Cambios en exactitud factual

## 🎨 Reportes incluidos

Cada artifact contiene:

- `index.html` - Página de navegación principal
- Todos los reportes `.html` generados por tus tests
- `validation_history.json` - Datos históricos para trends

## ⚙️ Configuración personalizada

### Cambiar la retención de artifacts

Por defecto, los artifacts se mantienen por 30 días. Para cambiar esto, modifica la línea:

```yaml
retention-days: 30
```

### Agregar más ramas

Para que el workflow se ejecute en otras ramas, agrega sus nombres en:

```yaml
on:
  push:
    branches: [main, master, develop, tu-rama-aqui]
```

### Instalar dependencias adicionales

Si necesitas instalar paquetes adicionales, agrégalos en el paso "Install dependencies":

```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    pip install true-lies-validator>=0.8.0
    pip install tu-paquete-adicional
```

## 🐛 Solución de problemas

### Los tests fallan pero necesito ver los reportes

El workflow está configurado con `continue-on-error: true` en los tests, lo que significa que **siempre generará los reportes** incluso si algunos tests fallan.

### No veo el historial de validaciones

El historial se guarda usando el sistema de cache de GitHub. Si es la primera ejecución, es normal que no haya historial previo. A partir de la segunda ejecución, verás las tendencias.

### Los artifacts no se generan

Verifica que:

1. Tus tests están generando archivos `.html`
2. El directorio `true_lies_reporting` existe
3. La ejecución del workflow completó todos los pasos

## 📚 Más información

- [True Lies Validator Documentation](https://pypi.org/project/true-lies-validator/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Actions Artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts)
