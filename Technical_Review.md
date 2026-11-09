# Technical review of the AI assisted lexical census

- Review date: 9 November 2026. Authors: Fatih Ridvan Kizik and Dheeraj Erpa, Team Avengers, Gr10.
- Reviewed run: `atrs_results_ai_assisted_lexical_census_20261109T183352831540Z`; revision `0.2.0-ai-assisted-census`.
- Review type: AI assisted code, data traceability and numerical review. No independent human record-level coding is claimed. Fatih reported both members checked the earlier notebook/results; that statement is not evidence of semantic annotation or adjudication.

## Explicit assignment question

**Is my code technically complete and publication ready for publication in the selected journal?**

- **Technically complete for the revised deterministic lexical-census implementation in the checked local environment: yes.** All 12 code cells executed, with no execution errors, using the verified 153-record frozen corpus. The program generated all 20 planned outputs, exact source evidence, disclosed rules, sensitivity diagnostics, provenance and an integrity-checked results ZIP. The final run passed 34 software, traceability and numerical checks.
- **Publication ready for Government Information Quarterly: not established, and I cannot give an affirmative approval.** Successful execution does not establish construct validity, methodological contribution, novelty or journal suitability. The revised questions are narrower than the original proposal and the instructor has not approved the change. The revised notebook has not yet completed a saved Kaggle run. No complete journal manuscript or full literature synthesis is included in this technical release.
- This is a technical research audit, not editorial acceptance or a guarantee of publication. Changing the label from human coding to AI assistance does not itself resolve the scientific limitations.

## Reviewed behavior and actual findings

- Frozen corpus: all 153 published records in the archived 26 October 2026 snapshot; 157 archived-response checksums verified. Every record is included by the revised wording-census definition. These are not 153 confirmed eligible individual-decision systems under the original proposal.
- Channel wording 16/153; submission wording 4/153; reviewer wording 20/153; review-scope wording 23/153; timing wording 3/153; remedy wording 6/153; escalation wording 11/153. Timing includes filing deadlines and must not be described as response time.
- Appeals-wording categories contain 23 bare NA/none, 5 human/nonautomated-decision, 1 missing extraction, 16 nonapplicability/no-route, 12 ordinary-process, 58 other/unclear and 38 other-contestation records. These are ordered regex categories, not semantic consistency decisions.
- Word count versus number of detected cue types: Spearman rho 0.1660052750 across all 153 records. No population p-value or causal interpretation.
- Routine-oversight and affected-person-review cue cross-tab: 19 both, 61 oversight only, 18 review only, 55 neither. The two conditional review-cue proportions are 19/80 and 18/73.
- Removing matches from sentences flagged by the negation pattern changes the seven record counts from 16,4,20,23,3,6,11 to 15,4,15,17,1,5,10. This is sensitivity to the disclosed flag, not a semantic accuracy test.
- Direct-link inventory: 13 record links to 12 official pages. Ten pages retrieved successfully; two HTTP 403 denials. AI contextual-relevance notes identify decision-specific guidance, general complaints and generic signposting separately. Later guidance does not change the frozen record measures; this inventory is not exhaustive.

## What was verified

- Every candidate excerpt occurs in its archived source after whitespace normalization. Unique evidence counts reconcile with all seven plotted feature counts.
- All main denominators and category totals reconcile; Spearman was independently recomputed from average ranks. Negation losses reconcile. All result checksums and ZIP CRC integrity pass.
- Ten figures were visually checked for layout and wording, and the three-page methodology amendment was rendered and inspected. No human screening forms, invented reviewer identities or human agreement scores are released as completed work.
- `Census_Validation.json` lists the 34 checks. They test the implementation, not the validity of lexical indicators as measures of real appeal access.

## Remaining scientific and delivery work

- Establish that the narrowed wording study has a sufficient original contribution for the journal, supported by a complete assessment of relevant journal literature. A prevalence inventory alone may be insufficient.
- Preserve the lexical interpretation throughout the manuscript. No conclusions about legal compliance, actual review availability, accessibility, successful remedies or citizen outcomes follow from these detections. Role categories are automatic cue groupings; 82 records are unclear and 18 have mixed cues.
- Any future semantic or substantive claim needs an appropriate evaluation design; the original independent-human design has been removed from this revision, not retrospectively fulfilled.
- Obtain instructor review of the method/RQ change; finish the required saved Kaggle execution; publish a new repository/Zenodo version with matching bytes; ensure the submitted ChatGPT review link actually contains the current explicit review. The user-selected historical share link predates this review.
- Student-written manuscript development and the instructor-provided Overleaf link follow technical review. No manuscript or journal submission is represented as completed here.
