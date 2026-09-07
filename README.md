# LangChain Architecture Lab: Gemini & Agentic Workflows

Laboratorio práctico de experimentación y análisis sobre arquitecturas con **LangChain**, adaptado para utilizar **Google Gemini** como LLM principal y gestionado de forma reproducible mediante **uv**.

---

## Stack Tecnológico

| Componente | Herramienta / Paquete | Propósito |
| :--- | :--- | :--- |
| **Package Manager** | [`uv`](https://github.com/astral-sh/uv) | Gestión rápida y determinista del entorno virtual |
| **Core Framework** | `langchain` | Orquestación de cadenas, memoria y agentes |
| **Model Provider** | `langchain-google-genai` | Integración nativa con la API de Google Gemini |
| **Configuración** | `python-dotenv` | Gestión desacoplada de secretos y variables de entorno |
| **Code Quality** | `black`, `isort` | Formateo consistente y ordenamiento de imports |

---

## Configuración del Entorno

### Crear y activar el entorno virtual con uv
`uv venv`

`source .venv/bin/activate`

### Instalar dependencias
`uv pip install langchain langchain-google-genai python-dotenv`

`uv pip install --dev black isort langchain-tavily tavily-python`