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
                input_file="input.kicad_pcb"
            )
        )
    ),
).exec()
```


## Development

```bash
git clone https://github.com/faebryk/kicadcliwrapper.git
poetry install

# Re-generate bindings (make sure kicad-cli is installed)
python src/kicadcliwrapper/main.py
```