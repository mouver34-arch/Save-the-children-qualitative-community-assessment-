"""Create a reproducible thematic summary from synthetic qualitative data."""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_qualitative_data.csv"
OUTPUT = ROOT / "outputs" / "generated_thematic_summary.md"

REQUIRED_COLUMNS = {
    "record_id", "method", "participant_group", "community",
    "transcript_excerpt_en", "initial_code", "theme", "evidence_type"
}


def main() -> None:
    df = pd.read_csv(DATA)

    missing = REQUIRED_COLUMNS.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    if df["record_id"].duplicated().any():
        duplicates = df.loc[df["record_id"].duplicated(), "record_id"].tolist()
        raise ValueError(f"Duplicate record IDs found: {duplicates}")

    theme_counts = df["theme"].value_counts()
    code_counts = df["initial_code"].value_counts()
    group_theme = pd.crosstab(df["participant_group"], df["theme"])

    lines = [
        "# Generated thematic summary",
        "",
        "> **SYNTHETIC DATA — FOR DEMONSTRATION ONLY**",
        "",
        "This output is generated from fictional portfolio records. It is not a report of the Save the Children assessment.",
        "",
        "## Theme frequency",
        "",
        theme_counts.to_frame("records").to_markdown(),
        "",
        "## Code frequency",
        "",
        code_counts.to_frame("records").to_markdown(),
        "",
        "## Theme distribution by participant group",
        "",
        group_theme.to_markdown(),
        "",
        "## Synthetic evidence examples",
        "",
    ]

    for _, row in df.head(6).iterrows():
        lines.extend([
            f"- **{row['participant_group']} / {row['method']} / {row['theme']}**: "
            f"{row['transcript_excerpt_en']}"
        ])

    lines.extend([
        "",
        "## Demonstration recommendations",
        "",
        "- Use clear community-facing communication channels when synthetic evidence indicates information gaps.",
        "- Provide accessible feedback/reporting pathways where synthetic records indicate accessibility or feedback barriers.",
        "- Strengthen coordination among relevant community and service stakeholders when coordination appears repeatedly in coded evidence.",
        "",
        "These recommendations are generated for the portfolio demonstration and are **not** recommendations from Save the Children.",
    ])

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
