# AI Usage

## AI-Assisted Extraction

I used ChatGPT (GPT-6.1 Sol) to clean all eight records from the original messy_sequences.fasta file. I attached the file in the chat.

### Prompt Summary

I asked ChatGPT to return a CSV containing sample ID, organism, gene, reported length, actual length, note, and sequence. I instructed it to standardize IDs and organism names, leave missing reported lengths blank, join and uppercase sequences, count their bases, and preserve notes without inventing information or altering sequences.

### Output and Verification

ChatGPT returned eight records with the requested columns, which I saved without changing the values as outputs/ai_sequences.csv.

I verified the header fields against the original FASTA headers and used Python's csv.DictReader to compare the AI and regex outputs. The comparison returned:

```text
Regex records: 8
AI records: 8
All fields match: True
```

All seven fields matched, including the complete sequences. Both outputs preserved the discrepancies in sample_003 (150 bp reported versus 157 bases calculated) and sample_005 (130 bp reported versus 144 bases calculated). These discrepancies remained unresolved because the file alone could not establish whether the headers or sequences were incorrect. Agreement between the outputs did not by itself prove correctness.

## AI Assistance with Troubleshooting

I wanted to empty my Python script but was unsure how, so I asked ChatGPT (GPT-6.1 Sol). It suggested:

```bash
> scripts/clean_fasta.py
```

However, my shell waited for input instead of returning to the terminal prompt. I reported, "it wont enter anything," and provided a screenshot showing the command and terminal state. ChatGPT explained that the shell was waiting for input before I could ask what the problem meant, then instructed me to press Control+C.

After I confirmed that the prompt had returned, it suggested this command instead:

```bash
printf '' > scripts/clean_fasta.py
```

Before running the replacement command, I reviewed its explanation that it would clear only the working script. I had already saved a backup at /tmp/lab3_clean_fasta_backup.py. I verified the fix by confirming that the command returned to the prompt without an error and that the script was blank when reopened in nano.
## Exact Extraction Prompt

```text
Extract and clean all eight records from the attached messy_sequences.fasta file.

Return CSV with these exact columns:
sample_id,organism,gene,reported_length_bp,actual_length_bp,note,sequence

Standardize sample IDs to sample_001 through sample_008.
Standardize Homo_sapiens, Homo sapiens, H.sapiens, and Hsapiens
to Homo sapiens.
Extract each gene symbol from its header.
Keep the reported header length separate from the actual sequence length.
Leave missing or NA reported lengths blank.
Join each record's sequence lines, remove whitespace, and use uppercase.
Count the bases to obtain actual_length_bp.
Preserve notes such as re-sequenced; leave absent notes blank.
Do not invent missing information or alter the sequence.
Return only CSV.
```
