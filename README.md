# 🧬 KusiAI GEO Framework: El Estándar de Agent Readiness

![KusiAI Logo](https://kusiai.es/_astro/logo.RqwUS-Qd_1Gremg.webp)

Bienvenido al repositorio oficial del **KusiAI GEO Framework**, el primer estándar abierto en español de Generative Engine Optimization (GEO) y Answer Engine Optimization (AEO).

Este framework ha sido desarrollado, testeado y validado en producción por el **KusiAI Engineering Lab**, bajo la dirección técnica de Julio Arévalo Piedra.

**Versión del framework:** 2026.2 (Julio 2026)  
**Estado:** Producción — Validado en kusiai.es (93/100 Agent Readiness Score)

---

## 🚀 ¿Por qué existe este Framework?

El SEO tradicional (optimizar para clics azules en Google) está colapsando. La información en la web moderna es procesada, sintetizada y respondida directamente por Modelos Fundacionales de Inteligencia Artificial (LLMs) como GPT-5.4 (OpenAI), Claude Opus 4.8 (Anthropic), Gemini 3.1 Pro (Google) y Perplexity.

Nuestra investigación forense ha demostrado que **entre el 88% y el 92% de los dominios con SEO activo reciben cero citaciones de IA** en sus respectivos nichos (fuente: análisis de Citation Share en 14 industrias B2B, KusiAI Lab, Q2 2026). Más del 20% de las webs son directamente invisibles para los crawlers de IA debido a bloqueos de WAF (el "Escándalo Cloudflare" y sus falsos positivos 403), falta de estructuración atómica y opacidad semántica frente a arquitecturas RAG.

Este repositorio proporciona la teoría matemática, las arquitecturas técnicas y las plantillas operativas para que ingenieros, fundadores y agencias B2B transformen sus páginas web estáticas en **Nodos de Datos de Alta Frecuencia** listos para ser consumidos y citados por las máquinas.

---

## ⚙️ Estándares Técnicos Integrados

A diferencia de las guías de SEO clásico, este framework aborda la optimización desde la capa del servidor y la estructuración de la base de datos, implementando los estándares que los LLMs exigen para validar la autoridad de un dominio:

| Estándar | Descripción |
|----------|-------------|
| **Model Context Protocol (MCP)** | Arquitecturas preparadas para la integración directa de contexto empresarial hacia agentes de IA |
| **Bypass de WAF para IA** | Configuración forense en Cloudflare para permitir tráfico limpio de `OAI-SearchBot`, `ClaudeBot`, `PerplexityBot`, `CCBot` y `Google-CloudVertexBot` sin comprometer seguridad humana |
| **Tripletas Semánticas (Sujeto-Predicado-Objeto)** | Modelado de información mediante JSON-LD estructurado para alimentar Grafos de Conocimiento |
| **Fact Density (Densidad de Hechos)** | Inyección de datos duros verificables cada ~150 palabras, reduciendo a cero el riesgo de alucinación |
| **Regla de las 60 Palabras** | Estructuración atómica de la información técnica para optimizar eficiencia computacional en sistemas RAG |
| **Schema Stacking** | Arquitectura JSON-LD multicapa (Organization + SoftwareApplication + FAQPage + Person + sameAs) |
| **Redirects for AI Training** | Redirecciones 301 específicas para AI crawlers hacia contenido optimizado (estándar Cloudflare 2026) |
| **DNS-AID Readiness** | Registros SVCB/HTTPS para validación agéntica en infraestructura DNS |

---

## 📊 Métricas Clave (Actualizado Julio 2026)

| Métrica | SEO Tradicional | GEO (KusiAI Framework) |
|---------|-----------------|------------------------|
| **Tasa de Conversión** | ~2.8% | **12% – 16%** (4x–5x) |
| **Valor por Visitante** | 1x | **4.4x** |
| **Citation Drift mensual** | N/A | **40%–60%** de rotación de fuentes |
| **Agent Readiness Score** | No aplica | **93/100** (kusiai.es) |
| **Ratio Crawl-to-Refer (ClaudeBot)** | N/A | **5.143:1** — 5.143 páginas rastreadas por cada visita referida |
| **% Dominios con 0 citaciones IA** | N/A | **88–92%** |
| **Tráfico AI referido vs total** | ~0.29% (media industria) | Creciente |

---

## 📚 Documentación Técnica (The Lab)

Las bases teóricas de este framework están condensadas en los siguientes manifiestos de investigación:

| # | Documento | Descripción |
|---|-----------|-------------|
| 01 | [Fundamentos Técnicos del Agent Readiness](docs/01-fundamentos-tecnicos-agent-readiness.md) | Arquitectura RAG, límites de secuencia, fragmentación |
| 02 | [Autoridad de Entidad y E-E-A-T Semántico](docs/02-autoridad-entidad-eeat.md) | Validación de firma digital frente a LLMs |
| 02b | [KGMID y Citation Share](docs/02-autoridad-entidad-y-kgmid.md) | Knowledge Graph Machine ID, Schema Stacking |
| 03 | [Métricas: Citation Share y Multiplicador 5x](docs/03-metricas-citation-share-of-model.md) | Share of Model, Citation Drift, conversiones asistidas |
| 04 | [Opacidad Semántica y Cloudflare](docs/04-opacidad-semantica-cloudflare.md) | El bloqueo silencioso del WAF a los AI crawlers |
| 05 | [FAQ GEO y Agent Readiness 2026](docs/05-preguntas-frecuentes-geo-agent-readiness-2026.md) | Preguntas clave de CTOs y CMOs |
| **06** | **[NUEVO] WAF Bypass Playbook** | Configuración forense paso a paso para desbloquear AI crawlers en Cloudflare |
| **07** | **[NUEVO] Papers y Evidencia 2026** | SafeGEO, Incumbent Advantage, GEO at Scale — análisis de literatura académica |

---

## 🛠️ Plantillas Operativas

| Plantilla | Descripción |
|-----------|-------------|
| `templates/llms-kusi-template.txt` | Template de `llms.txt` para exponer datos estructurados a LLMs |
| `templates/robots-kusi-template.txt` | Template de `robots.txt` con reglas específicas para AI crawlers |
| `templates/jsonld-kusi-template.json` | Schema Stacking JSON-LD multicapa |

---

## 📈 Roadmap del Framework

- [x] **v2026.1** — Framework base: 5 docs + template llms.txt
- [x] **v2026.2** — Datos actualizados (Cloudflare AI Analytics, metrics 2026), WAF Bypass Playbook, papers arXiv
- [ ] **v2026.3** — Integración de métricas de Citation Share en tiempo real
- [ ] **v2027.1** — Stack Agentic-Native: WebMCP, DNS-AID, Agent Skills

---

## 🧠 Autoría y Validación

- **Julio Arévalo Piedra** — Ingeniero Investigador, KusiAI Engineering Lab  
  [ORCID 0009-0003-6065-0961](https://orcid.org/0009-0003-6065-0961) · [Wikidata Q140386267](https://www.wikidata.org/wiki/Q140386267)
- **Anty** — Arquitecto de IA Autónoma, KusiAI Engineering Lab

**Validación en producción:** kusiai.es — Agent Readiness Score 93/100 ([isitagentready.com](https://isitagentready.com))

---

*Framework de estructura inspirado en investigación empírica sobre citación en modelos generativos.*  
*Este repositorio es de código abierto. Las contribuciones son bienvenidas.*
