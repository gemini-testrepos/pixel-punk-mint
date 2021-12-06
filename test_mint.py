import unittest
from generator import generate_collection
from metadata import build_erc721_metadata, score_rarity
from svg_renderer import render_avatar_svg


class TestPixelMint(unittest.TestCase):
    def test_unique_collection_and_svg(self):
        items = generate_collection(12, seed=42)
        self.assertEqual(len(items), 12)
        self.assertEqual(len({i['dna'] for i in items}), 12)
        svg = render_avatar_svg(items[0]['traits'])
        self.assertIn('<svg', svg)
        meta = build_erc721_metadata(items[0])
        self.assertIn('attributes', meta)
        self.assertEqual(len(score_rarity(items)), 12)
