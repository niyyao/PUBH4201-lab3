import re
import csv

with open("data/raw/messy_sequences.fasta") as file:
    text = file.read()

records = text.split(">")[1:]

rows = []

for record in records:
    lines = record.strip().splitlines()
    header = lines[0]
    sequence = "".join(lines[1:]).replace(" ", "").upper()

    id_match = re.search(r"^(?:sample|seq)[_-]?(\d+)", header, re.I)
    sample_id = "sample_" + id_match.group(1).zfill(3)

    organism_match = re.search(r"Homo[_ ]sapiens|H\.sapiens|Hsapiens", header, re.I)
    organism = ""
    if organism_match:
        organism = "Homo sapiens"

    gene_match = re.search(r"(?:gene|target)[:=]([\w-]+)(?=[;|\s]|$)", header, re.I)
    gene = ""
    if gene_match:
        gene = gene_match.group(1).upper()

    if not gene_match and organism_match:
        after_organism = header[organism_match.end():]
        gene_match = re.search(r"^\s*[|;]\s*([\w-]+)", after_organism)
        if gene_match:
            gene = gene_match.group(1).upper()

    length_match = re.search(r"\blen(?:gth)?[:=](\d+)", header, re.I)
    if not length_match:
        length_match = re.search(r"\b(\d+)\s*bp\b", header, re.I)
    reported_length = ""
    if length_match:
        reported_length = int(length_match.group(1))

    actual_length = len(sequence)
    note_match = re.search(r"note[:=]([^|;]+)", header, re.I)
    note = ""
    if note_match:
        note = note_match.group(1).strip()

    rows.append([sample_id, organism, gene, reported_length, actual_length, note, sequence])

with open("outputs/regex_sequences.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "sample_id", "organism", "gene", "reported_length_bp",
        "actual_length_bp", "note", "sequence"
    ])
    writer.writerows(rows)
