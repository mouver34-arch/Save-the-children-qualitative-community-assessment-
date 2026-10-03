# Qualitative Community Assessment — Fieldwork Portfolio Demonstration

## Project overview

This repository is a **public portfolio demonstration** of qualitative fieldwork organization, transcription, coding, thematic analysis and evidence-based reporting.

It is informed by my professional experience supporting a **Save the Children qualitative field assessment in Jigawa State in March 2025**. The real assignment involved community engagement, Focus Group Discussions (FGDs), Key Informant Interviews (KIIs), interviews conducted primarily in Hausa, transcription into English, documentation of findings, and qualitative assessment/analysis.

**This repository does not contain Save the Children project data, participant records, confidential findings, internal documents or restricted materials. All records in `data/` are synthetic and were created solely for demonstration.**

## Real-world professional context

During the March 2025 assessment, field activities covered communities including:

- Masko
- Dorawa
- Babura
- Insharuwa

Stakeholder/participant groups included girls, boys, children with disabilities, parents, community leaders, religious leaders, Women Affairs stakeholders, Education stakeholders and Child Protection stakeholders.

The assessment considered areas such as participant experiences/performance, positive and negative effects of interventions, stakeholder responses, government support, community actions, challenges/gaps and recommendations.

This repository demonstrates the **methodological workflow** without reproducing the real assessment's findings.

## Problem being addressed

Qualitative fieldwork can produce large amounts of unstructured information across different participant groups and interview types. A useful workflow needs to preserve context while making recurring issues, differences between perspectives and supporting evidence easier to identify.

## Objectives

This demonstration shows how to:

1. Structure FGD and KII records.
2. Preserve source and respondent-group context.
3. Organize Hausa-to-English transcription examples.
4. Apply qualitative codes to responses.
5. Group codes into themes.
6. Compare stakeholder perspectives.
7. Identify recurring issues in synthetic evidence.
8. Produce a concise thematic summary and recommendations.

## Methodology

The demonstration follows a simplified workflow:

**Field engagement → FGD/KII capture → transcription → coding → theme development → stakeholder comparison → evidence summary → recommendations**

The synthetic records are intentionally small so that a recruiter or reviewer can inspect the complete workflow quickly.

### Real experience vs portfolio extension

**Supported by my real experience:** field participation in the March 2025 Save the Children qualitative assessment, community engagement, FGDs, KIIs, Hausa-language interviewing, English transcription, documentation, and qualitative assessment/analysis.

**Portfolio extension:** the coding matrix, Python thematic-analysis script and synthetic thematic summary are demonstrations of how I can structure and reproduce a qualitative analysis workflow. They should not be read as the exact tools or outputs used in the Save the Children assignment.

## Data collection framework

The synthetic dataset uses:

- `record_id` — fictional record identifier
- `method` — FGD or KII
- `participant_group` — fictional stakeholder/participant category
- `community` — one of the communities represented in the professional context
- `language` — synthetic source-language label
- `transcript_excerpt_en` — fictional English transcription excerpt
- `initial_code` — demonstration code
- `theme` — demonstration theme
- `evidence_type` — experience, challenge, response or recommendation

No real participant quotation is reproduced.

## Data processing and analysis

The Python script in `analysis/thematic_analysis.py`:

- loads the synthetic CSV;
- checks required columns;
- counts records by method and participant group;
- identifies recurring codes and themes;
- compares themes across participant groups;
- writes a Markdown summary.

The Excel-compatible coding matrix is provided as `analysis/qualitative_coding_example.xlsx`.

## Tools

- Microsoft Excel-compatible `.xlsx` workflow
- Python
- pandas
- Markdown
- KoboToolbox/ODK are part of my broader digital field-data toolkit, but this repository does not claim that the synthetic coding workflow was captured directly from either platform.

## Synthetic-data and confidentiality disclaimer

> **SYNTHETIC DATA — FOR DEMONSTRATION ONLY.**

Every record in `data/synthetic_qualitative_data.csv` is fictional. It is not a Save the Children dataset, not a participant register and not a transcription of a real participant.

This repository intentionally excludes:

- participant names or other personal identifiers;
- real quotations;
- phone numbers;
- NIN/BVN or other identity numbers;
- exact household addresses;
- identifiable geolocation;
- confidential programme information;
- internal reports, forms or questionnaires;
- passwords, API keys, access tokens or private URLs.

## Ethical considerations

Qualitative work involving children and other potentially vulnerable participants requires careful handling of consent/assent, confidentiality, safeguarding, data minimization and secure storage.

For a public portfolio, the safest approach is to demonstrate the **method and analytical logic**, not to publish source records from a real assignment.

See `docs/ethical_considerations.md` for the publication boundary used here.

## Repository structure

```text
qualitative-community-assessment/
├── README.md
├── PORTFOLIO_METADATA.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── data/
│   ├── README.md
│   └── synthetic_qualitative_data.csv
├── docs/
│   ├── methodology.md
│   ├── data_collection_framework.md
│   └── ethical_considerations.md
├── analysis/
│   ├── qualitative_coding_example.xlsx
│   └── thematic_analysis.py
├── outputs/
│   ├── example_thematic_summary.md
│   └── generated_thematic_summary.md
