# Contestation wording in UK ATRS records

- Team Avengers, Gr10. Fatih Ridvan Kizik and Dheeraj Erpa.
- Revision 0.2.0-ai-assisted-census, prepared 9 November 2026. Current state: locally executed and checked; not yet published as a new Zenodo version or handed in to Teams.
- Purpose: count disclosed lexical patterns across all 153 records in the frozen 26 October 2026 snapshot. AI assisted the design revision, programming, review and contextual reading. The analysis itself is deterministic and requires no LLM API.
- Read `Technical_Review.md` before interpreting results. The implementation is complete for the revised wording questions in the checked local environment. GIQ publication readiness is not established.

## Files

- `ATRS_AI_Assisted_Census.ipynb`: fully executed local notebook, 12 code cells, 10 inline figures and 10 inline tables.
- `ATRS_results_ai_assisted_census.zip`: ten PDF figures plus PNGs, ten CSV tables, plot data, evidence, rules, captions, negation sensitivity, later guidance, metadata and checksums.
- `ATRS_Kaggle_Input.zip`: unchanged frozen record archive.
- `Linked_Guidance_Archive.zip`: supplementary later-page archive, including AI context notes and explicit failures; never used to alter frozen indicators.
- `Original_Research_Proposal.docx`: byte-preserved proposal used to generate the first code.
- `Team_Avengers_Methodology_Amendment.docx`: new questions, method, original-to-revised comparison, AI provenance and scientific limits. The original proposal's broader claims are not represented as completed.
- `Census_Validation.json`, `verify_release.py`, `file_manifest.json`: verification record and portable byte-integrity verification.
- `Target_Journal.txt`, `Submission_Links.txt`, `Assignment_Compliance.md`, `RIGHTS.md`, `CITATION.cff`, `requirements.txt`: delivery and attribution metadata.

## Reproduce locally

- Use Python 3.13 with the versions in `requirements.txt`, or a compatible scientific Jupyter environment. No GPU, training, internet or API key is needed for the notebook's frozen analysis.
- Extract `ATRS_Kaggle_Input.zip` into a folder named `input_data` beside the notebook, so `input_data/data/atrs_records.json` exists. Extract `Linked_Guidance_Archive.zip` beside the notebook so `linked_guidance/retrieval_manifest.json` exists.
- Open the notebook, restart its kernel and run all cells in order. A fresh dated results directory and one results ZIP are generated. Run times, file ordering/metadata and image/font library differences may alter binary hashes across environments; compare numerical outputs and source hashes, not timestamped archive bytes.
- Run `python3 verify_release.py` in the distributed release directory to verify the released bytes. This does not rerun the analysis or establish semantic validity.

## Run on Kaggle

- Import the IPYNB into the existing notebook or a new private notebook. Attach the frozen input ZIP as an extracted Kaggle dataset, and attach the linked-guidance archive as an extracted supplementary dataset. The loader searches `/kaggle/input` recursively.
- CPU and Internet off are sufficient. Run all cells and save a version using Save and Run All. The current release was executed locally; a new saved Kaggle run is still pending. The older successful Kaggle version belongs to the earlier exploratory notebook, not this revision.
- Guidance is supplementary: without the attachment the notebook explicitly reports that the archive is missing; record-level measurements remain unchanged. Attach it to reproduce all supplied supplementary outputs.

## Interpretation

- A detection is a regex match in a source sentence. It is not a confirmed procedural safeguard. Non-detection is not proof of absence. Seven cue types do not form a validated quality index.
- The census represents the frozen published register only. It cannot estimate all UK public-sector systems. Source texts are organizational self-reports and actual appeal outcomes were not measured.
- All five research questions were revised to concern wording. The original human pilot, independent coding and adjudication were not performed and are not reported as performed. No Cohen kappa, semantic precision/recall or invented reviewer labels are supplied.
- Existing version 0.1 remains the historical exploratory release. Its DOI 10.5281/zenodo.24080972 does not identify these new bytes. Publish and cite a new version before claiming the revised artifacts are publicly deposited.
