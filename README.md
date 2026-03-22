# BlackRoad-Studio — RoadCode

> Creator Tools division of [BlackRoad OS, Inc.](https://github.com/BlackRoad-OS-Inc)

Video editing, graphic design, music production, and writing tools — all running on your device, your data, your agents. No cloud subscriptions. No watermarks. No upload-to-render.

**Domain**: [lucidia.studio](https://lucidia.studio)

## Products

| Product | What It Does |
|---------|-------------|
| **Canvas Studio** | Vector + raster design tool with template library |
| **Video Studio** | Timeline editor, transitions, export to any format |
| **Writing Studio** | Distraction-free writing with local AI assist |
| **Cadence** | Music sequencer and beat engine |

## Org Hierarchy

```
BlackRoad-OS-Inc (Parent — 254 repos, 67 agents, 7 nodes)
  └── BlackRoad-Studio (Creator Tools)
      ├── RoadCode          ← this repo (workspace + automation)
      ├── operator           ← CLI tools + bootstrap
      ├── source             ← canonical source tree
      └── templates          ← design system + starter files
```

## Repos in This Org

- [`RoadCode`](https://github.com/BlackRoad-Studio/RoadCode) — Workspace hub (this repo)
- [`operator`](https://github.com/BlackRoad-Studio/operator) — CLI + deployment scripts
- [`source`](https://github.com/BlackRoad-Studio/source) — Source tree for all Studio products
- [`templates`](https://github.com/BlackRoad-Studio/templates) — JSX design templates + brand assets

## How It Connects

- **Parent**: [BlackRoad-OS-Inc](https://github.com/BlackRoad-OS-Inc) — central coordination
- **AI Models**: [BlackRoad-AI](https://github.com/BlackRoad-AI) — Lucidia powers local AI assist in Writing Studio
- **Hardware**: [BlackRoad-Hardware](https://github.com/BlackRoad-Hardware) — Hailo-8 accelerators for video rendering
- **Infrastructure**: Runs on the BlackRoad fleet — 7 nodes, $38/mo total

## Getting Started

```bash
git clone https://github.com/BlackRoad-Studio/RoadCode.git
cd RoadCode && ./scripts/setup.sh
```

## License

Proprietary — BlackRoad OS, Inc. See [LICENSE](./LICENSE).

---

*Remember the Road. Pave Tomorrow.*
