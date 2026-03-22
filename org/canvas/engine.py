"""Canvas Studio — browser-based design tool engine."""
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Layer:
    id: str
    type: str  # text, image, shape, group
    x: float = 0
    y: float = 0
    width: float = 100
    height: float = 100
    properties: dict[str, Any] = field(default_factory=dict)
    visible: bool = True
    locked: bool = False

@dataclass
class Canvas:
    id: str
    name: str
    width: int = 1920
    height: int = 1080
    layers: list[Layer] = field(default_factory=list)
    background: str = "#0a0a0a"

    def add_layer(self, layer: Layer) -> None:
        self.layers.append(layer)

    def remove_layer(self, layer_id: str) -> bool:
        self.layers = [l for l in self.layers if l.id != layer_id]
        return True

    def export_svg(self) -> str:
        return f'<svg width="{self.width}" height="{self.height}" xmlns="http://www.w3.org/2000/svg"></svg>'
