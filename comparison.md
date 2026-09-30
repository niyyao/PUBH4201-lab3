# Regex and AI Cleaning Comparison

## Approach

I used messy_sequences.fasta, which contains eight synthetic DNA sequence records with inconsistent headers. My Python script used regular expressions to extract sample IDs, organisms, genes, reported lengths, and notes. It standardized IDs to sample_001 through sample_008 and recognized organism-name variants as Homo sapiens. It also joined each record's sequence lines and calculated the sequence length.

For the AI approach, I attached the same raw file to ChatGPT and specified the same seven output columns and cleaning rules. Both methods produced CSV tables.

## Agreement and Edge Cases

Both outputs contained eight records. A comparison using Python's csv.DictReader showed that all seven fields agreed for every record, including the complete sequences. There were no observed disagreements between the final outputs.

Both methods handled sample_004's species and target labels, standardizing H.sapiens to Homo sapiens and extracting BRCA1. Both recognized seq6 as sample_006 and extracted its unlabeled EGFR gene. They also preserved sample_007's re-sequenced note and left sample_008's len:NA value blank.

## Failure Modes and Unresolved Records

Sample_003 had length=150bp in its header, but its sequence contained 157 bases. Both methods retained 150 as the reported length and 157 as the calculated length. A method that trusted only the header would incorrectly treat 150 as the sequence's actual length. However, neither approach could determine whether the header was outdated or the sequence itself was incorrect. Preserving both values exposed the inconsistency without resolving it.

Sample_005 reported 130 bp, but its sequence contained 144 bases. Both methods again preserved the discrepancy. The length disagreement remained ambiguous because the raw file did not explain its cause. Neither method could establish whether the reported length or the supplied sequence needed correction.

Another limitation concerned sample_008: both approaches represented len:NA as blank, just as they represented an absent length field. This followed the cleaning rules but lost the distinction between explicitly reported NA and a field that was never provided. That distinction could matter in a real dataset.

## Time, Effort, and Trust

The regex script took substantially more time to write and check than obtaining the AI output. I needed to understand the patterns, account for different header formats, and check the code and results. AI produced the table quickly from one detailed extraction prompt, but its output still needed verification.

For repeated cleaning of a real dataset with known formats, I would prefer a checked regex script because its rules are visible and can be rerun consistently. AI would be useful for exploring unfamiliar formats and suggesting interpretations, but I would verify its results against the source. This dataset showed that agreement does not resolve inconsistent source information: the length discrepancies would still require clarification before using those fields confidently.
