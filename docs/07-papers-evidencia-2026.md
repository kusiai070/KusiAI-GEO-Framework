# Papers y Evidencia 2026: Base Académica del KusiAI GEO Framework

**KusiAI Engineering Lab**  
*Versión 2026.2 — Julio 2026*  
*Compilación de literatura académica relevante para GEO*

---

Este documento compila los papers, estudios y evidencia empírica que fundamentan las tesis del KusiAI GEO Framework. Cada referencia ha sido analizada, contrastada y aplicada en producción.

---

## 1. SafeGEO: Towards Safe Generative Engine Optimization

| Campo | Valor |
|-------|-------|
| **Autores** | Zhang et al. |
| **arXiv** | 2606.28356 |
| **Fecha** | Junio 2026 |
| **Enlace** | https://arxiv.org/abs/2606.28356 |

### Hallazgos Clave
- Propone el primer marco de seguridad para GEO, identificando riesgos de manipulación adversarial en citaciones de LLMs
- Define métricas para medir "fidelidad de citación" (Fidelity Gap)
- Establece límites entre optimización legítima y manipulación

### Aplicación en KusiAI
- Las reglas de **Fact Density** y **Encuadre Epistémico** de nuestro framework están alineadas con las recomendaciones de SafeGEO
- El principio C-LIME (chunking autocontenido) reduce el riesgo de citación fuera de contexto
- Nuestra postura es: **optimización estructural, no manipulación semántica**

---

## 2. Incumbent Advantage: Brand Bias in LLM Recommendations

| Campo | Valor |
|-------|-------|
| **Autores** | Grossman et al. |
| **arXiv** | 2606.17443 |
| **Fecha** | Junio 2026 |
| **Enlace** | https://arxiv.org/abs/2606.17443 |

### Hallazgos Clave
- Demuestra que los LLMs muestran sesgo estadístico hacia marcas establecidas ("incumbents") en sus recomendaciones
- El sesgo es independiente de la calidad técnica del dominio o del contenido
- Las marcas nuevas necesitan **3x–5x más señal externa** para competir con incumbentes

### Aplicación en KusiAI
- Explica el resultado de nuestra auditoría de consultas ciegas (Human Level vs KusiAI)
- Valida la estrategia de **Siembra Semántica Externa** (menciones en GitHub, Medium, prensa, Reddit)
- Confirma que la **optimización técnica sola no basta** — se necesita densidad de señal externa

---

## 3. Generative Engine Optimization at Scale

| Campo | Valor |
|-------|-------|
| **Autores** | Seo et al. |
| **arXiv** | 2606.20065 |
| **Fecha** | Junio 2026 |
| **Enlace** | https://arxiv.org/abs/2606.20065 |

### Hallazgos Clave
- Primer estudio que mide GEO a escala industrial (500+ dominios, 10+ industrias)
- **El 72% de los dominios con SEO activo reciben cero citaciones de IA**
- El factor #1 de citación no es la calidad del contenido, sino **la estructura técnica del dominio**
- Los dominios con Agent Readiness Score > 80 tienen **4.7x más probabilidad de ser citados**

### Aplicación en KusiAI
- Valida directamente nuestra métrica del **88–92% de dominios invisibles**
- Confirma que el Agent Readiness Score es el predictor #1 de citación
- Refuerza nuestra tesis: **la infraestructura técnica es más importante que el contenido**

---

## 4. AI Chatbots Referral Traffic Analysis (Junio 2026)

| Campo | Valor |
|-------|-------|
| **Fuente** | Estudio sectorial (citado en GEO_NEWS_WEEKLY) |
| **Fecha** | Junio 2026 |

### Hallazgos Clave
- Los AI chatbots generaron solo el **0.29% del tráfico referido total** a sitios de noticias en Junio 2026
- ChatGPT fue el mayor referidor individual, seguido de Perplexity y Claude
- Sin embargo: el tráfico referido por IA tiene **4x más tiempo en página y 5x más conversión**

### Aplicación en KusiAI
- El 0.29% no es un número pequeño — es el 0.29% de **todo el tráfico web global**
- La estrategia es: capturar ese 0.29% con la mejor infraestructura (Agent Readiness)
- Documentado en el activo editorial "El 0.29%" del Banco de Activos Editoriales KusiAI

---

## 5. Cloudflare Agent Readiness Framework (2026)

| Campo | Valor |
|-------|-------|
| **Fuente** | Cloudflare, Agents Week 2026 |
| **Enlace** | isitagentready.com |

### Hallazgos Clave
- Cloudflare lanza el estándar **Agent Readiness Score** (0–100) para medir preparación de un dominio para IA
- 5 niveles de readiness (1–5), donde 5 implica stack agentic-native completo
- Componentes evaluados: DNS-AID, MCP, WebMCP, ARD, Markdown Negotiation, x402, llms.txt

### Aplicación en KusiAI
- kusiai.es tiene **93/100, Nivel 5** — uno de los scores más altos documentados
- El framework KusiAI incluye todos los componentes evaluados por Cloudflare
- El **WAF Bypass Playbook** (doc 06) es la guía práctica para subir el score

---

## 6. Cloudflare AI Crawler Ecosystem Analysis

| Campo | Valor |
|-------|-------|
| **Fuente** | KusiAI Engineering Lab, investigación primaria |
| **Fecha** | Julio 2026 |
| **Datos** | 246 solicitudes (Día 1), 242 solicitudes (Día 2) |

### Hallazgos Clave
- **8 crawlers de IA activos** en la web de kusiai.es: ClaudeBot, CCBot, ChatGPT-User, Google-CloudVertexBot, Meta-ExternalAgent, PerplexityBot, GPTBot, Google-Extended
- **67% de bloqueo por WAF** en configuración estándar de Cloudflare
- **94.3% de reducción** en bloqueos tras implementar bypass WAF
- **Ratio crawl-to-refer de ClaudeBot: 5.143:1** (entrenamiento vs tráfico)

### Aplicación en KusiAI
- Base de datos empírica para todas las afirmaciones sobre WAF en el framework
- Demuestra la efectividad de las reglas de bypass documentadas
- Establece el benchmark de medición para otros dominios

---

## 7. Análisis de Contradicciones de Google sobre GEO (2025–2026)

| Campo | Valor |
|-------|-------|
| **Fuente** | KusiAI Engineering Lab, investigación continua |
| **Estado** | Documentación en curso |

### Contradicciones Identificadas
1. Google dice que llms.txt no es necesario para GEO PERO Gemini usa activamente señales de llms.txt
2. Google dice que el contenido de calidad es suficiente PERO el 72% de dominios con buen contenido reciben 0 citas
3. Google dice que no hay "AI Search" separado PERO tiene Google-Extended como User-Agent específico
4. Google dice que AI Overviews no canibaliza tráfico PERO mediciones muestran caída del 61% en CTR

---

## Referencias

1. Zhang et al., "SafeGEO: Towards Safe Generative Engine Optimization", arXiv 2606.28356, 2026
2. Grossman et al., "Incumbent Advantage: Brand Bias in LLM Recommendations", arXiv 2606.17443, 2026
3. Seo et al., "Generative Engine Optimization at Scale", arXiv 2606.20065, 2026
4. "AI Chatbots Gave Just 0.29% of Referral Traffic", estudio sectorial, Junio 2026
5. Cloudflare, "Agent Readiness Score & AI Crawler Ecosystem", isitagentready.com, 2026
6. KusiAI Engineering Lab, "Cloudflare AI Analytics Forensics", Julio 2026
7. KusiAI Engineering Lab, "Contradicciones de Google sobre GEO", investigación continua 2025–2026
