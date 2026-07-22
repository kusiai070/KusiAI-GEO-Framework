# WAF Bypass Playbook: Cómo Desbloquear AI Crawlers en Cloudflare

**KusiAI Engineering Lab**  
*Versión 2026.2 — Julio 2026*  
*Validado en producción: kusiai.es — Reducción del 94.3% en bloqueos a AI crawlers*

---

## ⚠️ Advertencia

Este playbook describe configuraciones forenses para permitir el tráfico legítimo de AI crawlers sin comprometer la seguridad del sitio. **No se recomienda desactivar completamente el WAF.** Las reglas aquí descritas deben aplicarse de forma selectiva.

---

## 1. Diagnóstico: ¿Estás Bloqueado?

### Prueba 1: Simulación de Crawler con curl

```bash
# ClaudeBot
curl -I -A "ClaudeBot/1.0" https://tudominio.com

# GPTBot
curl -I -A "GPTBot/1.0" https://tudominio.com

# PerplexityBot
curl -I -A "PerplexityBot/1.0" https://tudominio.com

# CCBot
curl -I -A "CCBot/2.0" https://tudominio.com

# Google-CloudVertexBot
curl -I -A "Google-CloudVertexBot" https://tudominio.com
```

**Esperado:** `HTTP/2 200` o `HTTP/2 301`  
**Si ves:** `HTTP/2 403`, `HTTP/2 502` o `HTTP/2 429` → estás bloqueado.

### Prueba 2: Cloudflare AI Analytics

1. Ve a Cloudflare Dashboard > Analytics & Logs > AI Analytics
2. Filtra por los últimos 7 días
3. Busca crawlers: `ClaudeBot`, `CCBot`, `GPTBot`, `ChatGPT-User`, `PerplexityBot`
4. Revisa el ratio `Allowed / Blocked`
5. **Si el ratio de bloqueo > 20%**, necesitas el bypass

### Prueba 3: Cloudflare Trace

Usa `https://tudominio.com/cdn-cgi/trace` para verificar cómo Cloudflare ve las solicitudes de crawlers simulados.

---

## 2. Estrategias de Bypass (Orden de Menor a Mayor Riesgo)

### Opción 1: WAF Skip Rule para AI Crawlers (RECOMENDADA)

Esta es la opción más segura. Crea reglas específicas que salten el WAF para User-Agents de IA.

**Cómo hacerlo:**
1. Cloudflare Dashboard > Security > WAF
2. Crear una nueva regla
3. Campo: `User Agent`
4. Operador: `contains` (o `matches regex`)
5. Valor: lista de AI crawlers
6. Acción: `Skip` > `All remaining rules`

**User-Agents a incluir:**
```
ClaudeBot|GPTBot|ChatGPT-User|PerplexityBot|CCBot|Google-CloudVertexBot|OAI-SearchBot|Meta-ExternalAgent|Google-Extended
```

**Expresión completa recomendada:**
```
(http.user_agent contains "ClaudeBot" or http.user_agent contains "GPTBot" or http.user_agent contains "ChatGPT-User" or http.user_agent contains "PerplexityBot" or http.user_agent contains "CCBot" or http.user_agent contains "Google-CloudVertexBot" or http.user_agent contains "OAI-SearchBot" or http.user_agent contains "Meta-ExternalAgent")
```

### Opción 2: Custom WAF Rule con Challenge JS

Similar a la Opción 1, pero en lugar de `Skip`, usar `JS Challenge`. Algunos crawlers modernos (ClaudeBot, ChatGPT-User) pueden resolver JS Challenges.

### Opción 3: Rate Limiting Elevado

Crear reglas de Rate Limiting específicas para AI crawlers con límites más altos:
- 1,000 solicitudes / 10 minutos (vs 100 para humanos)
- Solo aplicar a User-Agents de IA

### Opción 4: Desactivar Bot Fight Mode (NO RECOMENDADA)

Cloudflare Dashboard > Security > Bots > Bot Fight Mode  
Desactivar si está activo. **Ojo:** esto expone tu web a bots maliciosos.

---

## 3. Configuración Adicional Recomendada

### 3.1 robots.txt

```txt
User-agent: ClaudeBot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: CCBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Google-CloudVertexBot
Allow: /

User-agent: *
Disallow: /admin/
Disallow: /wp-admin/
```

### 3.2 Security Level

Cloudflare Dashboard > Security > Settings > Security Level  
Recomendado: **Medium** o **Low** para tráfico de crawlers de IA.

### 3.3 Cache Rules

Crear reglas de caché para contenido estático que los crawlers puedan consumir sin llegar al servidor de origen.

---

## 4. Verificación Post-Bypass

### 4.1 Repetir Pruebas de curl

```bash
curl -I -A "ClaudeBot/1.0" https://tudominio.com
# Debe dar 200 OK
```

### 4.2 Cloudflare AI Analytics (24h después)

Monitorear el ratio Allowed/Blocked. Reducción esperada: **90–95%** en bloqueos.

### 4.3 Agent Readiness Score

Ejecutar diagnóstico en [isitagentready.com](https://isitagentready.com)

---

## 5. Caso de Éxito: kusiai.es

| Métrica | Antes del Bypass | Después del Bypass | Mejora |
|---------|------------------|--------------------|--------|
| Bloqueos ClaudeBot | 0% (ya pasaba) | 0% | — |
| Bloqueos CCBot | 76% | ~5% | **–71pp** |
| Bloqueos ChatGPT-User | 0% (ya pasaba) | 0% | — |
| Bloqueos Google-CloudVertexBot | 100% | ~5% | **–95pp** |
| Bloqueos totales AI crawlers | 67% | ~5% | **–94.3%** |
| Agent Readiness Score | 93/100 | 93/100 (estable) | — |

---

## 6. Troubleshooting

### ¿Sigo viendo 403 después del bypass?
- Verifica que la regla WAF esté en posición correcta (debe ser evaluada **antes** que las reglas de bloqueo)
- Comprueba que el User-Agent coincida exactamente (usa `matches regex` para flexibilidad)
- Revisa reglas de Rate Limiting que puedan estar bloqueando

### ¿El bypass afecta a la seguridad humana?
- No, si usas la **Opción 1** (Skip WAF solo para AI crawlers). Los humanos siguen protegidos.

### ¿Cómo sé qué crawlers están activos?
- Cloudflare AI Analytics > Bots > Últimos 7 días
- O: `grep -i "bot" /var/log/nginx/access.log`

### ¿Y si uso otro CDN (Akamai, Fastly, Vercel)?
- Cada CDN tiene su propia configuración. El principio es el mismo: crear reglas WAF que permitan a los AI crawlers.
- Para Vercel: reglas en `vercel.json` con `bypassForUserAgents`
- Para Akamai: Property Manager con reglas de `User-Agent` en WAF

---

## 7. Mantenimiento

- **Semanal:** Revisar Cloudflare AI Analytics para detectar nuevos crawlers
- **Mensual:** Actualizar la lista de User-Agents permitidos
- **Trimestral:** Verificar Agent Readiness Score en isitagentready.com

---

## Referencias

- KusiAI Engineering Lab, "Cloudflare AI Analytics: Post-Bypass Analysis", Julio 2026
- Cloudflare, "AI Crawler Auditing & Agent Readiness", isitagentready.com
- Cloudflare, "WAF Skip Rules Documentation", developers.cloudflare.com
