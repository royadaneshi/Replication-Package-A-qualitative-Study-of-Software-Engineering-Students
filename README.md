# Replication Package
## *A qualitative Study of Software Engineering Students*
To ensure transparency and reproducibility of this study, a comprehensive replication package has been made available. This repository contains the data and scripts required to reproduce the analysis of the relationship between gaming habits across eight semesters (SP22-FA25) in an undergraduate software engineering course. We employ a qualitative workflow.

**Repository Structure**
```
Replication_Package/
├── README.md                                           # Usage instructions and environment requirements
│
├── Qualitative/
│   ├── Comprehensive_Codebook.xlsx                     # 8 primary themes and 28 sub-codes with definitions
│   ├── LLM_Automation_Protocol.md                      # Gemini 3 Pro prompts and data cleaning instructions
│   ├── codebook.pdf                                    # Our codebook, which was used for qualitative coding
│   ├── Keywords_and_Phrases_Reference_Map.pdf          # Mapping used for LLM deductive coding
│   ├── Frequency_Analysis_Audited_Final.csv            # Consolidated longitudinal counts across all eight semesters
│   ├── Qualitative_Analysis_Scripts/
│   │   ├── GenerateAuditIndexes.ipynb                  # Reproduces 25% stratified random sample
│   │   ├── CountCodes.ipynb                            # Aggregates thematic code totals
│   │   └── FrequencyFinding.ipynb                      # Calculates number of low- vs. high-frequency rows
│   └── Phase_1_Manually_Coded/                         # Baseline manual coding for Phase 1, used to calibrate LLM prompts for Phase 2
│   │   ├── FA25_Manually_Coded.xlsx
│   │   └── SP25_Manually_Coded.xlsx
│   └── LLM_Outputs/
│       ├── Raw_Outputs/                                # CSVs coded by Gemini 3 Pro (SP22-FA24)
|       │   ├── FA22_Exhaustive_Coded.csv               
|       │   ├── FA23_Exhaustive_Coded.csv               
|       │   ├── FA24_Exhaustive_Coded.csv               
|       │   ├── SP22_Exhaustive_Coded.csv               
|       │   ├── SP23_Exhaustive_Coded.csv               
|       │   └── SP24_Exhaustive_Coded.csv               
│       └── Audited_Outputs/                            # Post-Audit CSVs coded by Gemini 3 Pro (SP22-FA24)
|       │   ├── AUDITED_FA22_Exhaustive_Coded.csv               
|       │   ├── AUDITED_FA23_Exhaustive_Coded.csv               
|       │   ├── AUDITED_FA24_Exhaustive_Coded.csv               
|       │   ├── AUDITED_SP22_Exhaustive_Coded.csv               
|       │   ├── AUDITED_SP23_Exhaustive_Coded.csv               
|       │   └── AUDITED_SP24_Exhaustive_Coded.csv    
│
└── Survey - A Gaming/
     ├── Gaming_Survey.pdf                               # Original Canvas survey instrument instrument
     └── Student_Responses/
         ├── FA/                                         # Original anonymized data (Fall 2022–2025)
         │   ├── FA22_Responses.csv
         │   ├── FA23_Responses.csv
         │   ├── FA24_Responses.csv
         │   └── FA25_Responses.csv
         └── SP/                                         # Original anonymized data (Spring 2022–2025)
             ├── SP22_Responses.csv
             ├── SP23_Responses.csv
             ├── SP24_Responses.csv
             └── SP25_Responses.csv
             

```

## Environment Requirements
To ensure the scripts run correctly, please use the following environments:

- **Statistical Analysis:** Python 3.9
- **Qualitative Code Counting and Random Sample Generator:** Python 3.9.12
- **Qualitative Frequency Splitter:** Python 3.12.12
- **Necessary Python Libraries:** pandas, numpy, matplotlib

## Contents

### Data
- **Data Files:** Anonymized CSV datasets (e.g., ``` FA22_Responses.csv```) containing self‑reported student gaming habits paired with final course grades. All identifiers were removed prior to inclusion.
- **Survey Instrument:** A PDF copy (```Gaming_Survey.pdf```) of the original Gaming Survey as delivered on Canvas, including all questions and multiple‑choice options exactly as presented to participants.

### Qualitative
- **Qualitative Analysis Scripts:** Python scripts used for thematic code counting, including ```CountCodes.ipnyb``` for thematic counting, ```FrequencyFinding.ipnyb``` to count the number of low‑ and high‑frequency gamers across the manually coded cohorts, and ```GenerateAuditIndexes.ipnyb``` for selecting a random 25% sample of rows for manual verification.
- **Comprehensive Codebook:** The finalized codebook (```Comprehensive_Codebook.xlsx```) which contains eight primary themes and twenty‑eight sub‑codes, each defined and illustrated with an example quote. These codes capture students’ gaming habits, study behaviors, motivations, time‑management strategies, and perceptions of learning. The codebook represents the final structure developed through iterative refinement and serves as the reference framework for all qualitative analyses reported in the study.
- **Keywords and References Map:** A structured mapping (```Keywords_and_Phrases_Reference_Map.pdf```) that lists specific keywords and phrases used by Gemini 3 Pro to automate assigning codes.
- **Finalized Frequency Analysis:** The consolidated longitudinal dataset containing the aggregated thematic counts across all eight semesters (```Frequency_Analysis_Audited_Final.csv```). It includes a breakdown for Low-Frequency and High-Frequency cohorts, a Combined Total, and individual term distributions (from SP22 through FA25), serving as the primary source for the study’s qualitative frequency findings.
- **Phase 1 Manually Coded Outputs:** Finalized thematic assignments for the SP25 and FA25 cohorts (```/Phase_1_Manually_Coded/```), manually coded by the research team. This established the foundational 8 primary themes and 28 codes used to develop the ```Keywords_and_Phrases_Reference_Map.pdf``` for Phase 2.
- **LLM Automation Protocol:** The prompts used with Gemini 3 Pro during the deductive coding phase, including instructions for data cleaning and markdown‑based keyword bolding (```LLM_Automation_Protocol.md```).
- **LLM Outputs:** The raw CSV outputs (e.g. ```FA22_Exhaustive_Coded.csv```) generated by Gemini 3 Pro and the post‑audit CSVs (e.g. ```AUDITED_FA22_Exhaustive_Coded.csv```) following the 25\% random sample manual verification.
  - Yellow Highlight: Rows randomly selected for the 25% manual audit.
  - Light Orange Highlight (SP Cohorts Only): Rows originally marked as UNCODED that were not part of the random 25% sample
 
### Qualitative Analysis
#### Phase 1: Manual Coding and Framework Development
- Reference: Consult the ```/Phase_1_Manual_Coding/``` directory and ```Comprehensive_Codebook.xlsx```.
- Logic: This phase involved the manual inductive coding of the SP25 and FA25 cohorts.
- Goal: Establishing the 8 primary themes and 28 sub-codes that serve as the foundational logic for the entire qualitative stream.

#### Phase 2: Systematic Scaling (Automation)
- Reference: Utilize the ```LLM_Automation_Protocol.md``` and ```Keywords_and_Phrases_Reference_Map.pdf```.
- Logic: Apply the established codebook deductively to the remaining six semesters (FA22–SP24) using Gemini 3 Pro.
- Source: The resulting data is stored in ```Qualitative/LLM_Outputs/Raw_Outputs/```.

#### Phase 3: Manual Audit
- Execution: Run ```Qualitative_Analysis_Scripts/GenerateAuditIndexes.ipynb```.
- Logic: Employs a fixed seed (random_state=42) to reproduce the 25% stratified random sample for manual verification.
- Verification: Review files in ```Qualitative/LLM_Outputs/Audited_Outputs/```:
  - Yellow Highlights: Rows randomly selected to audit LLM coding against the manual Codebook.
  - Light Orange Highlights (SP only): Rows originally marked as UNCODED that were not part of the random sample
    
#### Phase 4: Frequency
- Execution: For the initial manually coded cohorts (SP25 + FA25), analysis was conducted via ```CountCodes.ipynb``` and ```FrequencyFinding.ipynb```. However, for the full longitudinal dataset, the exhaustive frequency sorting and code counting were transitioned to Gemini 3 Pro using the prompts documented in ```LLM_Automation_Protocol.md```.
- Final Output: The results of this automated scale-up are consolidated in ```Frequency_Analysis_Audited_Final.csv```.
- Logic: This transition ensures that the counting and sorting logic developed in the Python scripts was scaled consistently across all eight semesters. The LLM processes the exhaustive coded files to aggregate occurrences of the 28 codes according to the established framework.
- Goal: Quantify the prevalence of specific teamwork competencies and barriers to identify differences in perceived skill transference between Low-Frequency (0–3 days/week) and High-Frequency (4–7 days/week) gamers.
