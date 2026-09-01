# 🛰️ KusiGEO: Motor de Auditoría Forense y Observabilidad en Motores de IA

**Autor:** Julio Arévalo Piedra  
**Organización:** KusiAI Research Lab (`https://kusiai.es`)  
**Clasificación:** Documentación Técnica de Arquitectura (Nivel Público)  
**Versión:** 2026.3  

---

## 1. ¿Qué es KusiGEO?

**KusiGEO** es la plataforma de ingeniería de software desarrollada por **KusiAI** diseñada para auditar, medir y diagnosticar la visibilidad de entidades corporativas y marcas dentro de los **Motores de Razonamiento Generativo** (LLMs).

A diferencia de las herramientas de SEO tradicional que miden posiciones en páginas de resultados de búsqueda (SERPs) y volumen de clics orgánicos, KusiGEO opera como un **sistema de observabilidad semántica** que cuantifica si los modelos de lenguaje recomiendan a una empresa cuando un usuario realiza una consulta de decisión o compra.

---

## 2. El Punto Ciego que Resuelve KusiGEO

Las plataformas de analítica clásicas (Ahrefs, Semrush, Google Search Console) sufren de una **ceguera técnica absoluta** frente a la búsqueda moderna:

1. **Incapacidad de Medir Síntesis:** No pueden rastrear respuestas generadas dinámicamente en tiempo real por OpenAI Search, Perplexity, Gemini o Claude.
2. **Desconocimiento del Bloqueo WAF 403:** No detectan si los cortafuegos de la empresa (Cloudflare, AWS, Datadome) están rechazando a los rastreadores de IA mediante falsos positivos de seguridad.
3. **Falta de Métricas de Cuota de Citación:** No disponen de fórmulas matemáticas para calcular el *Citation Share* frente a los competidores del sector.

KusiGEO resuelve esta brecha mediante un pipeline de auditoría determinista de 4 capas.

---

## 3. Arquitectura Conceptual de KusiGEO (Pipeline de 4 Capas)

```
┌────────────────────────────────────────────────────────────────────────┐
│                        PIPELINE KUSIGEO 2026                           │
└────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
 ┌──────────────────────────────────────────────────────────────────────┐
 │ CAPA 1: Diagnóstico de Accesibilidad y Red (Crawler Handshake)       │
 │ - Simulación de User-Agents oficiales (ChatGPT-User, ClaudeBot, etc) │
 │ - Verificación de cabeceras HTTP, Vary: Accept y Content Signals     │
 │ - Detección de bloqueos 403 / desafíos JS en CDN perimetral          │
 └──────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
 ┌──────────────────────────────────────────────────────────────────────┐
 │ CAPA 2: Auditoría Semántica y Grafos de Entidad (Fact Density)       │
 │ - Extracción de tripletas Sujeto-Predicado-Objeto en JSON-LD         │
 │ - Validación de canonicidad (KGMID, Wikidata, DOI, sameAs)           │
 │ - Análisis de densidad atómica (Regla de las 60 palabras por tesis)  │
 └──────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
 ┌──────────────────────────────────────────────────────────────────────┐
 │ CAPA 3: Sondeo Controlado en 6 Modelos de Frontera                   │
 │ - Inyección de baterías de prompts comerciales tipados               │
 │ - Evaluación cruzada: ChatGPT, Gemini, Perplexity, Claude, DeepSeek  │
 │ - Detección de alucinaciones y marcas competidoras recomendadas      │
 └──────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
 ┌──────────────────────────────────────────────────────────────────────┐
 │ CAPA 4: Motor de Cálculo y Métricas Deterministas                    │
 │ - CSR (Citation Selection Rate): Porcentaje de respuestas ganadas    │
 │ - CAS (Citation Absorption Score): Relevancia y contexto del extracto│
 │ - CPV (Cross-Provider Variance): Estabilidad entre distintos LLMs    │
 └──────────────────────────────────────────────────────────────────────┘
```

---

## 4. Las Métricas del Estándar KusiGEO

KusiGEO sintetiza la visibilidad en tres indicadores objetivos:

### A. Citation Selection Rate (CSR)
Calcula la probabilidad de que una marca aparezca citada y recomendada dentro de un conjunto de consultas comerciales del sector:
$$\text{CSR} = \frac{\text{Apariciones Recomendadas}}{\text{Total de Consultas Evaluadas}} \times 100$$

### B. Citation Absorption Score (CAS)
Mide la calidad semántica con la que el modelo absorbe la propuesta de valor: si la marca es citada como líder de categoría, como alternativa secundaria o si sus datos de contacto/precios son interpretados con exactitud.

### C. Cross-Provider Variance (CPV)
Mide la consistencia de la entidad a través de los diferentes espacios vectoriales:
* **CPV < 15% (Robusto):** La marca tiene presencia uniforme en todos los modelos.
* **CPV > 40% (Frágil):** La marca aparece en un buscador (ej. Perplexity) pero es invisible o distorsionada en otros (ej. ChatGPT o Gemini).

---

## 5. Entregables de la Auditoría Forense KusiGEO

Una auditoría ejecutada por KusiGEO proporciona:

1. **Matriz de Brecha de Citación (Citation Gap):** Comparativa directa frente a los 3 principales competidores recomendados por la IA en el mercado objetivo.
2. **Protocolo de Remediación de Cortafuegos:** Instrucciones técnicas para configurar Cloudflare y servidores web sin exponer la seguridad humana.
3. **Esquema de Inyección Semántica:** Generación de JSON-LD multicapa optimizado para sistemas RAG y panels de conocimiento.
4. **Plan de Transición a Nivel 5 (Agent-Native):** Despliegue de catálogos OpenAPI 3.1, Model Context Protocol (MCP) y directivas `llms.txt`.

---

## 6. Distinción Fundamental: Qué NO es KusiGEO

* **NO es un generador automático de textos con IA:** No produce artículos de relleno ni spam masivo que degradan la reputación de la marca.
* **NO es una herramienta de trucos temporales:** Se basa estrictamente en la documentación oficial de recuperación de información de los laboratorios de IA (OpenAI, Anthropic, Google, Vercel) y en los estándares de la IETF / W3C.
* **Es una plataforma de diagnóstico, observabilidad y arquitectura de datos** para asegurar que las empresas sean tratadas como fuentes de máxima autoridad por los sistemas inteligentes.
