# 🎭 GitHub Actions - True Lies Testing

Este workflow ejecuta automáticamente tus tests de True Lies y publica los reportes HTML en GitHub Pages para acceso directo desde el navegador.

## 🚀 Características

- ✅ **Ejecución automática** en push y pull requests
- 📊 **Generación de reportes HTML** con True Lies Validator
- 📈 **Preservación del historial** de validaciones entre ejecuciones
- 🎨 **Página índice elegante** para navegar los reportes
- 🌐 **Publicación en GitHub Pages** con acceso directo por URL
- 💬 **Comentarios automáticos** en Pull Requests con resumen de resultados

## 📋 ¿Cuándo se ejecuta?

El workflow se ejecuta automáticamente cuando:

- Haces push a las ramas `main`, `master` o `develop`
- Creas o actualizas un Pull Request hacia estas ramas
- Lo ejecutas manualmente desde la pestaña Actions (workflow_dispatch)

## 🌐 Cómo ver los reportes

Los reportes están disponibles públicamente en GitHub Pages:

**URL:** https://thefreerangetester.github.io/demo_truelies/

Los reportes se actualizan automáticamente después de cada push a main e incluyen:

- Métricas detalladas de validación
- Gráficos de tendencias históricas
- Datos del validation_history.json visualizados
- Página índice elegante para navegación

### Acceso desde Pull Requests

Si el workflow se ejecutó en un PR, verás un comentario automático con:

- Resumen de los resultados del test
- Enlace directo a la página de GitHub Pages

## 📈 Historial de validaciones

El archivo `validation_history.json` se preserva entre ejecuciones usando el sistema de cache de GitHub Actions y se publica junto con los reportes HTML, permitiendo que True Lies genere gráficos de tendencias automáticamente.

El historial se guarda con cada ejecución y se restaura automáticamente en la siguiente, permitiendo ver:

- Tendencias de tasa de éxito a lo largo del tiempo
- Evolución de similitud semántica
- Cambios en exactitud factual
- Comparación entre diferentes ejecuciones

Los gráficos de tendencias se generan automáticamente en los reportes HTML cuando hay suficiente historial disponible.

## 🎨 Reportes publicados

El sitio de GitHub Pages incluye:

- `index.html` - Página de navegación principal con diseño moderno
- Todos los reportes `.html` generados por tus tests
- `validation_history.json` - Datos históricos para trends
- Gráficos interactivos de tendencias (cuando hay historial suficiente)

## ⚙️ Configuración personalizada

### Retención de reportes

Los reportes en GitHub Pages se mantienen indefinidamente (sin límite de tiempo) y se actualizan automáticamente con cada push a main. No hay costos de almacenamiento adicionales.

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

### Los reportes no se publican en GitHub Pages

Verifica que:

1. Tus tests están generando archivos `.html`
2. El directorio `true_lies_reporting` existe
3. La ejecución del workflow completó todos los pasos
4. GitHub Pages está habilitado en Settings → Pages → Source: "GitHub Actions"
5. El push fue a la rama `main` o `master` (solo estas ramas publican a Pages)

## 📚 Más información

- [True Lies Validator Documentation](https://pypi.org/project/true-lies-validator/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
