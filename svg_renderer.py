"""Render trait dictionaries into crisp 8x8 pixel-grid SVGs."""

from typing import Dict


def render_avatar_svg(traits: Dict[str, tuple[str, object]]) -> str:
    bg = traits['background'][1]
    skin = traits['skin'][1]
    eyewear = traits['eyewear'][1]
    headgear = traits['headgear'][1]
    rects = [
        f'<rect x="0" y="0" width="8" height="8" fill="{bg}" />',
        f'<rect x="2" y="2" width="4" height="5" fill="{skin}" />',
        '<rect x="3" y="4" width="1" height="1" fill="#222" />',
        '<rect x="5" y="4" width="1" height="1" fill="#222" />',
    ]
    if eyewear:
        rects.append(f'<rect x="2" y="4" width="4" height="1" fill="{eyewear}" />')
    if headgear:
        rects.append(f'<rect x="2" y="1" width="4" height="1" fill="{headgear}" />')
    body = ''.join(rects)
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 8 8" shape-rendering="crispEdges">'
        f'{body}</svg>'
    )
