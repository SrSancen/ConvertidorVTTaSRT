<h1><p align="center"> 🎯 Convertidor de Subtítulos VTT → SRT<br><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></p></h1>

<h3><p align="center">🛠️ Tecnologías
    <br>
    <img src="https://img.shields.io/badge/Python-3.6+-blue.svg">
    <img src="https://img.shields.io/badge/Tkinter-GUI-green.svg">
</p></h3>
<br> 

# Python

Aplicación de escritorio sencilla y rápida para convertir archivos de subtítulos **.vtt** a **.srt** con pocos clics, completamente local en tu dispositivo.
<br>

<p align="center">
    <img width="878" height="790" alt="Convertidor VTT a SRT_python" src="https://github.com/user-attachments/assets/bd433742-71eb-4b67-a861-b5738f562dce" />
</p>
<br> 

## 📋 Requisitos

- **Python 3.6** o superior
- **Tkinter** (viene incluido con Python por defecto)
- Sistema operativo: Windows, macOS o Linux
<br>

## 🚀 Instalación

1. **Clona o descarga** este repositorio:
    ```
    git clone https://github.com/SrSancen/ConvertidorVTTaSRT.git
    ```
    
2. **Navega a la carpeta** del proyecto:
    ```
    cd ConvertidorVTTaSRT
    ```
    
3. **Ejecuta la aplicación**:
    ```
    python "Convertidor VTT a SRT.py"
    ```

> 💡 **Opcional**: Si quieres generar un ejecutable para compartir sin Python:
> 
> ```
> pip install pyinstaller
> pyinstaller --onefile --windowed --name="ConvertidorVTTaSRT" "Convertidor VTT a SRT.py"
> ```

<br>

## 🎮 Cómo usar

##### Paso 1: Seleccionar el archivo .vtt

- Haz clic en **"📁 Seleccionar"** y elige el archivo de subtítulos con extensión `.vtt` que deseas convertir.

<br>

##### Paso 2: Elegir carpeta de destino

- Selecciona la carpeta donde quieras guardar el archivo convertido.

> 	📌 Si no eliges una, la aplicación usará automáticamente la misma carpeta del archivo original.

<br>

##### Paso 3: Convertir

- Haz clic en **"⚡ Convertir"** y espera unos segundos. El archivo `.srt` se generará automáticamente.

<br>

##### Paso 4: Ver el resultado

- El archivo convertido se guardará con el mismo nombre pero extensión `.srt`
- Puedes abrir la carpeta de destino haciendo clic en **"📂 Abrir carpeta de destino"**
- En el panel de **Registros** verás todo el proceso y una vista previa del resultado

<br>
<br>
<br>

---
<h3><p align="center">🛠️ Tecnologías
    <br>
    <img src="https://img.shields.io/badge/HTML-red.svg">
</p></h3>
<br> 

# HTML

Página web simple y práctica para convertir archivos de subtítulos **.vtt** a **.srt**, completamente en tu dispositivo sin tener que buscar páginas web en internet.
<br>

<p align="center">
    <img width="900" height="752" alt="Convertidor VTT a SRT_html" src="https://github.com/user-attachments/assets/4a4a06ef-e5d4-499e-981b-3ef4edfc335d" />
</p>
<br> 

## 📋 Requisitos

- **Navegador** (Chrome, Mozilla, Edge, Opera, Brave, Yandex, etc.)
- **No hace falta tener conexión a internet** (todo el proceso se hace en tu equipo)
- Sistema operativo: Windows, macOS o Linux
<br>

## 🚀 Instalación

1. **Clona o descarga** este repositorio:
    ```
    git clone https://github.com/SrSancen/ConvertidorVTTaSRT.git
    ```
    
2. **Navega a la carpeta** del proyecto:
    ```
    cd ConvertidorVTTaSRT
    ```
    
3. **Abre la página web "Convertidor VTT a SRT.html"**.

<br>

## 🎮 Cómo usar

##### Paso 1: Seleccionar el archivo .vtt

- Haz clic en **"📁 Seleccionar"** y elige el archivo de subtítulos con extensión `.vtt` que deseas convertir. Puedes arrastrar y soltar directamente el archivo en el navegador.

<br>

##### Paso 2: Convertir

- Haz clic en **"⚡ Convertir"** y selecciona la ruta donde se guardará tu archivo en formato .srt.

<br>

##### Paso 3: Ver el resultado

- El archivo convertido se guardará con el mismo nombre pero extensión `.srt` (puedes cambiar el nombre si lo deseas).
- Busca la carpeta de destino donde guardaste el archivo (por defecto se guardará donde está el archivo original a menos que hayas cambiado la ruta de destino).
- En el panel de **Registros** verás todo el proceso y una vista previa del resultado.

<br>


## ✨ Características de ambas variantes

- ✅ **Interfaz moderna sencilla**
- ✅ **Conversión automática** de tiempos (`.` → `,` para milisegundos)
- ✅ **Limpieza de etiquetas HTML** (colores, estilos, etc.)
- ✅ **Selección de archivos y carpetas**
- ✅ **Logs en tiempo real** con colores y timestamps
- ✅ **100% local** - No envía datos a ningún servidor
<br>

## 📝 Ejemplo

**Entrada (.vtt):**
```
WEBVTT
00:01.100 --> 00:02.900
Would you like to come with me?.
```
<br>

**Salida (.srt):**
```
1
00:01,100 --> 00:02,900
Would you like to come with me?.
```
<br>

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Siéntete libre de usarlo, modificarlo y compartirlo.
