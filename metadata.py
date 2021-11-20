"""OpenSea-compatible ERC-721 metadata and rarity scorer."""

from collections import Counter
from typing import Any, Dict, List


def build_erc721_metadata(item: Dict[str, Any], ipfs_cid: str = 'QmExampleCID') -> Dict[str, Any]:
    token_id = item['token_id']
    attrs = [
        {'trait_type': layer.title(), 'value': val[0]}
        for layer, val in item['traits'].items()
    ]
    return {
        'name': f'Pixel Student #{token_id}',
        'description': 'Generative pixel avatar created for Fall 2021 Web3 studio.',
        'image': f'ipfs://{ipfs_cid}/{token_id}.svg',
        'dna': item['dna'],
        'attributes': attrs,
    }


def score_rarity(collection: List[Dict[str, Any]]) -> Dict[int, float]:
    total = max(1, len(collection))
    counts: Counter[tuple[str, str]] = Counter()
    for item in collection:
        for layer, val in item['traits'].items():
            counts[(layer, str(val[0]))] += 1
    scores: Dict[int, float] = {}
    for item in collection:
        score = sum(total / counts[(layer, str(val[0]))] for layer, val in item['traits'].items())
        scores[int(item['token_id'])] = round(score, 2)
    return scores
