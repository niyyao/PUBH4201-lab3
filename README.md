# PUBH 4201 Lab 3: Parsing Messy Genomic Data

## Data

messy_sequences.fasta contains eight synthetic DNA sequence records generated for this course, with inconsistent header formats and no real patient information.

[Original data source](https://github.com/gwcbi/applied-computing-HDS/tree/main/data/raw/lab3-messy-data)

Raw data is downloaded locally and ignored by Git. Required cleaned outputs are committed.

## Project Structure

- scripts/clean_fasta.py — Python regex script
- outputs/regex_sequences.csv — Regex output
- outputs/ai_sequences.csv — AI output
- AI_USAGE.md — AI documentation and exact prompt
- comparison.md — Comparison and failure-mode analysis
- .gitignore — Excludes local data and temporary files

## Run

Requires Python 3; no additional packages are needed. Run from the repository root:

```bash
mkdir -p data/raw outputs
curl -fL https://raw.githubusercontent.com/gwcbi/applied-computing-HDS/main/data/raw/lab3-messy-data/messy_sequences.fasta -o data/raw/messy_sequences.fasta
python3 scripts/clean_fasta.py
```

Input: data/raw/messy_sequences.fasta

Output: outputs/regex_sequences.csv

Columns: sample_id, organism, gene, reported_length_bp, actual_length_bp, note, sequence. Missing fields stay blank; reported and calculated lengths remain separate.

## AI Extraction and Comparison

Attach the raw FASTA file to ChatGPT using the exact prompt in AI_USAGE.md. Save its CSV response unchanged as outputs/ai_sequences.csv.

Compare both tables by running:

```bash
python3 - <<'PY'
import csv
with open("outputs/regex_sequences.csv", newline="") as f:
    regex_rows = list(csv.DictReader(f))
with open("outputs/ai_sequences.csv", newline="") as f:
    ai_rows = list(csv.DictReader(f))
print("Regex records:", len(regex_rows))
print("AI records:", len(ai_rows))
print("All fields match:", regex_rows == ai_rows)
PY
```

Also check extracted values against the raw file. See comparison.md for the write-up and AI_USAGE.md for AI documentation.
