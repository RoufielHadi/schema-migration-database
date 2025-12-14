import os
from pathlib import Path


def ensure_runtime_ready() -> None:
    """
    Ensure the runtime environment is ready:
    - antlr4-python3-runtime is importable
    - ANTLR_JAR is set OR generated parser files exist
    """
    try:
        import antlr4  # noqa: F401
    except Exception as e:  # pragma: no cover - environment dependent
        raise RuntimeError(
            "antlr4-python3-runtime is not installed. Install with: pip install -r requirements.txt"
        ) from e

    root = Path(__file__).resolve().parents[2]
    gen_parser = root / 'generated' / 'DBSchemaParser.py'
    gen_visitor = root / 'generated' / 'DBSchemaVisitor.py'

    antlr_jar = os.environ.get('ANTLR_JAR')
    if not antlr_jar:
        # allow if generated artifacts already exist
        if gen_parser.exists() and gen_visitor.exists():
            return
        raise RuntimeError(
            "Environment variable ANTLR_JAR is not set and generated parser was not found. "
            "Either set ANTLR_JAR to your antlr-4.x-complete.jar path, or generate the parser via: "
            "python -m src.cli.dslc compile grammar/DBSchema.g4"
        )

    # If ANTLR_JAR set, basic existence check for file path
    if antlr_jar and not Path(antlr_jar).exists():
        raise RuntimeError(
            f"ANTLR_JAR is set to '{antlr_jar}' but file does not exist. Ensure the jar path is correct."
        )
