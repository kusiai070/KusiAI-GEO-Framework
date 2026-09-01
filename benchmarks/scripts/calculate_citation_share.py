#!/usr/bin/env python3
"""
KusiAI GEO Framework: Citation Share & Cross-Provider Variance Calculator
Author: Julio Arevalo Piedra
Copyright (c) 2026 KusiAI Research Lab (https://kusiai.es)
License: MIT
"""

import json
import math
import sys
from typing import Dict, List, Any

def calculate_metrics(data: List[Dict[str, Any]], target_entity: str) -> Dict[str, Any]:
    """
    Calculates Citation Selection Rate (CSR) per model, Global CSR, and Cross-Provider Variance (CPV).
    """
    models = set()
    for item in data:
        for m in item.get("results", {}).keys():
            models.add(m)
    
    models = sorted(list(models))
    total_queries = len(data)
    
    if total_queries == 0:
        return {"error": "Dataset is empty"}
        
    model_hits = {m: 0 for m in models}
    
    for item in data:
        results = item.get("results", {})
        for m in models:
            cited_entities = results.get(m, [])
            if any(target_entity.lower() in str(e).lower() for e in cited_entities):
                model_hits[m] += 1
                
    model_csr = {m: round((model_hits[m] / total_queries) * 100, 2) for m in models}
    
    # Global CSR average
    csr_values = list(model_csr.values())
    global_csr = round(sum(csr_values) / len(csr_values), 2) if csr_values else 0.0
    
    # Cross-Provider Variance (Standard Deviation across model CSRs)
    variance = sum((val - global_csr) ** 2 for val in csr_values) / len(csr_values) if csr_values else 0.0
    cpv = round(math.sqrt(variance), 2)
    
    return {
        "target_entity": target_entity,
        "total_queries_evaluated": total_queries,
        "model_citation_selection_rate": model_csr,
        "global_citation_share": global_csr,
        "cross_provider_variance": cpv,
        "status": "Robust Grounding" if cpv < 15.0 and global_csr > 50.0 else "High Variance / Fragile Grounding"
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python calculate_citation_share.py <dataset.json> [target_entity]")
        sys.exit(1)
        
    filepath = sys.argv[1]
    target = sys.argv[2] if len(sys.argv) > 2 else "KusiAI"
    
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    metrics = calculate_metrics(data, target)
    print(json.dumps(metrics, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
