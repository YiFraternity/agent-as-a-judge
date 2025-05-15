import enum
from pathlib import Path
import yaml
from typing import Any
from jinja2 import Template, StrictUndefined


def populate_template(template: str, variables: dict[str, Any]) -> str:
    compiled_template = Template(template, undefined=StrictUndefined)
    try:
        return compiled_template.render(**variables)
    except Exception as e:
        raise Exception(f"Error during jinja template rendering: {type(e).__name__}: {e}")


def load_yaml_file(file_path: str=Path(__file__).parent / "prompt_template.yaml") -> dict:
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

class Language(enum.Enum):
    English = "English"
    Chinese = "Chinese"

    @property
    def type(self):
        if self == Language.English:
            return "en"
        elif self == Language.Chinese:
            return "zh"
        else:
            raise ValueError(f"Unsupported language: {self}")

