# KiCAD CLI python bindings

Strongly typed, auto-generated python bindings for KiCAD's command line interface. 


## Usage

### Setup
```bash
pip install kicadcliwrapper
```

### Examples
```python
from kicadcliwrapper.generated.kicad_cli import kicad_cli

# Get version
kicad_cli(
    kicad_cli.version(),
).exec()


# Export pdf for pcb
kicad_cli(
    kicad_cli.pcb(
        kicad_cli.pcb.export(
            kicad_cli.pcb.export.pdf(
                INPUT_FILE="input.kicad_pcb"
            )
        )
    ),
).exec()
```

For more examples you can check [faebryk](https://github.com/faebryk/faebryk/blob/ee0f662d9b2b69c5ebdb5b424d4232ffb2ac2d7c/src/faebryk/exporters/pcb/kicad/artifacts.py)

## Development

```bash
git clone https://github.com/faebryk/kicadcliwrapper.git
poetry install

# Re-generate bindings (make sure kicad-cli is installed)
python src/kicadcliwrapper/main.py
```

See [PARSER.md](PARSER.md) for an explanation of the internal parsing.
