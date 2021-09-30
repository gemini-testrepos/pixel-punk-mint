"""Deterministic DNA generator for layered collectibles."""

import hashlib
import random
from typing import Dict, List, Set

from traits import TRAIT_LAYERS


def pick_traits(rng: random.Random) -> Dict[str, tuple[str, object]]:
    chosen: Dict[str, tuple[str, object]] = {}
    for layer, options in TRAIT_LAYERS.items():
        weights = [opt[2] for opt in options]
        picked = rng.choices(options, weights=weights, k=1)[0]
        chosen[layer] = (picked[0], picked[1])
    return chosen


def dna_hash(traits: Dict[str, tuple[str, object]]) -> str:
    key = '|'.join(f'{k}:{v[0]}' for k, v in sorted(traits.items()))
    return hashlib.sha256(key.encode('utf-8')).hexdigest()[:16]


def generate_collection(count: int, seed: int = 2021) -> List[Dict[str, object]]:
    rng = random.Random(seed)
    seen: Set[str] = set()
    collection: List[Dict[str, object]] = []
    attempts = 0
    while len(collection) < count and attempts < count * 20:
        attempts += 1
        traits = pick_traits(rng)
        dna = dna_hash(traits)
        if dna in seen:
            continue
        seen.add(dna)
        collection.append({'token_id': len(collection) + 1, 'dna': dna, 'traits': traits})
    return collection
