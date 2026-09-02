# GEO: Lo que dice la evidencia, lo que se puede hacer y los límites

**Manual Anti-Placebo de Generative Engine Optimization**  
**Autor:** Julio Arévalo Piedra & KusiAI Engineering Lab  
**Organización:** KusiAI Research (`https://kusiai.es`)  
**Fecha:** Septiembre 2026  
**Alcance:** Síntesis técnica de la literatura científica revisada por pares sobre Generative Engine Optimization (GEO).  
**Naturaleza:** Este documento analiza la evidencia disponible en papers académicos (ACM SIGKDD, arXiv) y su traducción a la ingeniería práctica.

---

## Propósito y honestidad del documento

Las bóvedas de conocimiento suelen caer en dos trampas:
1. Ser un conjunto de resúmenes teóricos sin aplicación práctica.
2. Convertirse en una lista de "trucos" y promesas comerciales exageradas.

Este documento distingue siempre dos tipos de afirmación:
* **Evidencia sólida:** Lo que un paper midió con datos empíricos revisados por pares.
* **Práctica de mercado:** Lo que se ejecuta en la industria y que puede o no estar respaldado por métricas.

**Metodología:** La evidencia principal proviene del paper fundacional de GEO (*Aggarwal et al., "GEO: Generative Engine Optimization", Proceedings of ACM SIGKDD KDD'24, DOI: 10.1145/3637528.3671900*) evaluado sobre el corpus **GEO-bench** (10.000 consultas, 25 dominios).

---

## 1. Qué es GEO (y la trampa del nombre)

**GEO = Generative Engine Optimization.** Es la disciplina de optimizar la arquitectura de datos y el contenido de un sitio web para que un motor de búsqueda generativo te **cite como fuente de verdad canónica** en su respuesta sintética. No se trata de aparecer en un listado de enlaces azules (eso es SEO tradicional). Se trata de que los motores de IA (OpenAI ChatGPT Search, Google Gemini, Perplexity Pro, DeepSeek, Alibaba Qwen, Moonshot Kimi) te recomienden y atribuyan la respuesta a tu dominio.

**La trampa en el nombre:** Decir "optimización" suele confundirse con "tráfico asegurado". GEO optimiza una métrica muy concreta: **la probabilidad y densidad de citación textual en una respuesta generada (Position-Adjusted Word Count - PAWC)**.

* **SEO:** Optimiza el ranking en un buscador de páginas web.
* **GEO:** Optimiza la **probabilidad de ser citado y recomendado** por un sistema de síntesis de lenguaje.

---

## 2. Lo que GEO SÍ puede hacer y lo que NO puede prometer

### 2.1 Lo que GEO SÍ puede hacer (Respaldado por evidencia)
* Aumentar la **probabilidad de que tu contenido sea citado** en la respuesta de un motor generativo.
* Mejorar exponencialmente tu visibilidad cuando tu web tiene **poca autoridad de dominio tradicional (Domain Rating bajo)**: es, precisamente, donde mayor impacto tiene.
* Optimizar la digestibilidad de la información para agentes autónomos mediante datos estructurados, citas atómicas y catálogos de descubrimiento (ARD v0.91).

### 2.2 Lo que GEO NO puede prometer (Límites honestos)
* **No garantiza clics automáticos:** Que la IA te cite en su respuesta no implica que el 100% de los usuarios hagan clic en el hipervínculo.
* **No garantiza ventas por sí solo:** Los papers midieron **visibilidad textual y posición de cita**, no conversión final. Convertir la visibilidad en ingresos sigue dependiendo de la propuesta de valor y el embudo comercial de la empresa.
* **No sustituye a una web sólida:** Si una página web no contiene datos concretos (precios, especificaciones, metodologías, hechos verificables), ninguna técnica de GEO puede inventarlos.

---

## 3. Hallazgos Científicos con Datos Duros (ACM SIGKDD 2024)

### 3.1 Eficacia de las Técnicas de Optimización

Evaluación sobre el dataset GEO-bench (10.000 queries, 25 dominios) midiendo el impacto en **Position-Adjusted Word Count (PAWC)**:

| Técnica Evaluada | Impacto en PAWC | Impacto Subjetivo | Veredicto Científico |
| :--- | :---: | :---: | :--- |
| **Sin optimización (Baseline)** | 19.5 | 19.3 | Punto cero de referencia |
| **Keyword Stuffing (Relleno de palabras clave)** | **17.8** | 20.2 | **Contraproducente (Empeora el resultado)** |
| **Unique Words (Vocabulario complejo)** | 20.7 | 20.4 | Efecto neutro |
| **Easy-to-Understand (Lenguaje simple)** | 22.2 | 20.5 | Positivo leve |
| **Authoritative (Tono de autoridad)** | 21.8 | 22.9 | Positivo en debates e historia |
| **Technical Terms (Terminología técnica)** | 23.1 | 21.4 | Positivo en nichos de ingeniería |
| **Fluency Optimization (Fluidez de lectura)** | 25.1 | 21.9 | Positivo en legibilidad general |
| **Cite Sources (Citar fuentes de terceros)** | 24.9 | 21.9 | Muy bueno en datos y hechos |
| **Statistics Addition (Inyección de estadísticas)** | **25.9** | **23.7** | **Excelente (+33% sobre baseline)** |
| **Quotation Addition (Inyección de citas textuales)**| **27.8** | **24.7** | **El mejor método (+41% sobre baseline)** |

**Conclusión clave:** El método más eficaz es la **adición de citas textuales y estadísticas verificables (+41% en visibilidad textual)**. Por el contrario, el **Keyword Stuffing tradicional fue la única técnica que empeoró activamente los resultados**.

---

### 3.2 El Efecto Democratizador de GEO (El hallazgo estratégico)

El análisis del paper por posición previa en el ranking orgánico revela una dinámica fundamental:

| Técnica | Sitios en Rank 5 (Poca autoridad) | Sitios en Rank 1 (Líderes de la SERP) |
| :--- | :---: | :---: |
| **Cite Sources (Citar fuentes)** | **+115.1%** | **-30.3%** |
| **Quotation Addition (Citas textuales)** | **+99.7%** | **-22.9%** |
| **Statistics Addition (Estadísticas)** | **+97.9%** | **-20.6%** |

**Interpretación para la toma de decisiones:**  
GEO **favorece estructuralmente a las empresas retadoras y de nicho frente a los monopolios establecidos**. Un sitio web con poca autoridad que estructura sus datos con rigor gana más de un **+100% de visibilidad**, mientras que un sitio líder en Google clásico puede perder visibilidad relativa si su contenido carece de hechos atómicos citables.

---

## 4. La Cadena Causal de 5 Eslabones en GEO

Para auditar y corregir la presencia en IA, KusiGEO mapea la cadena completa de decisión del modelo:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      LA CADENA CAUSAL DE GEO                            │
└─────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
 1. RECUPERACIÓN (Retrieval / RAG)
    El rastreador de IA (ej. ChatGPT-User) debe poder acceder al servidor
    sin ser bloqueado por falsos positivos de cortafuegos (WAF 403).
                                     │
                                     ▼
 2. ATRIBUCIÓN Y ENLAZADO DE ENTIDAD (Entity Linking)
    El modelo debe reconocer a la empresa como una entidad canónica
    distinta y validada (KGMID, Wikidata, JSON-LD, DOI).
                                     │
                                     ▼
 3. ESTRUCTURACIÓN ATÓMICA (Structural Feature Engineering)
    Organización en bloques de información de alta densidad (Regla de
    las 60 palabras por tesis declarativa) para facilitar el chunking.
                                     │
                                     ▼
 4. DEFENSA Y VERIFICACIÓN (SCI-Defense)
    Protección contra distorsión y verificación de que el LLM no alucina
    datos clave (precios, horarios, propuesta de valor).
                                     │
                                     ▼
 5. IMPACTO EN EL USUARIO Y MEDICIÓN
    Monitoreo cruzado: Cuota de Citación (Citation Share) + Analítica
    web (GA4 / Search Console) para medir el tráfico derivado.
```

---

## 5. Resumen de Buenas Prácticas para KusiGEO

1. **Priorizar datos duros sobre narrativa vacía:** Precios, metodologías, cifras con fuente, especificaciones técnicas y comparativas objetivas.
2. **Cero Keyword Stuffing:** Redactar para claridad semántica y precisión de respuesta.
3. **Optimizar para los 6 motores del Doble Eje:**
   * *Eje Occidental:* OpenAI ChatGPT Search, Google Gemini, Perplexity AI.
   * *Eje Oriental:* DeepSeek (R1/V3), Alibaba Cloud Qwen, Moonshot AI Kimi.
4. **Desbloqueo de infraestructura:** Garantizar que los rastreadores oficiales de IA tengan acceso HTTP 200 limpio mediante políticas perimetrales transparentes.

---

### Referencias Principales

* Aggarwal, P., Vishwakarma, A., et al. (2024). *GEO: Generative Engine Optimization*. Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '24). DOI: `10.1145/3637528.3671900`.
* KusiAI Research Lab (2026). *AI Retrieval & Citation Share Benchmark*. DOI: `10.5281/zenodo.21063287`.
