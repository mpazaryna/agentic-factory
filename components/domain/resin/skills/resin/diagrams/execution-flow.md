# Execution Flow Diagrams

## High-Level Pipeline

```mermaid
flowchart LR
    subgraph Input
        SF[(Salesforce)]
    end

    subgraph Stage1[Stage 1: Extraction]
        SPECS[Spec Executor]
        SYNTH[Synthesis]
    end

    subgraph Stage2[Stage 2: Enrichment]
        PERSONA[Persona Mapping]
        TEMPLATE[Template Matching]
    end

    subgraph Stage3[Stage 3: Sync]
        R2[(R2 Storage)]
    end

    subgraph Output
        DASH[Dashboard]
    end

    SF --> SPECS
    SPECS --> SYNTH
    SYNTH --> PERSONA
    PERSONA --> TEMPLATE
    TEMPLATE --> R2
    R2 --> DASH
```

## Pipeline Execution Flow

```mermaid
flowchart TD
    START([resin pipeline workflow tenant-env]) --> PARSE[Parse Arguments]
    PARSE --> VALIDATE{Prerequisites OK?}

    VALIDATE -->|No| FAIL1[Report Error & Stop]
    VALIDATE -->|Yes| EXTRACT[Run /run-specs]

    EXTRACT --> EXTRACT_OK{Extraction OK?}
    EXTRACT_OK -->|No| FAIL2[Report Failed Specs]
    EXTRACT_OK -->|Yes| ENRICH[Run enrich script]

    ENRICH --> ENRICH_OK{Enrichment OK?}
    ENRICH_OK -->|No| FAIL3[Report Enrichment Error]
    ENRICH_OK -->|Yes| SYNC[Run sync script]

    SYNC --> SYNC_OK{Sync OK?}
    SYNC_OK -->|No| FAIL4[Report Sync Error]
    SYNC_OK -->|Yes| DONE([Report Success])
```

## Data Flow

```mermaid
flowchart LR
    subgraph Salesforce
        OPP[Opportunities]
        ACC[Accounts]
        CON[Contacts]
    end

    subgraph Raw[dat/tenant/raw/]
        JSON1[01-lapse-risk.json]
        JSON2[02-upgrade.json]
        JSON3[99-synthesis.json]
    end

    subgraph Enriched[dat/tenant/enriched/]
        DASH_JSON[dashboard-data.json]
        QUEUE[focus-queue.json]
    end

    subgraph R2[Cloudflare R2]
        BUCKET[tenant-data bucket]
    end

    OPP & ACC & CON --> JSON1 & JSON2
    JSON1 & JSON2 --> JSON3
    JSON3 --> DASH_JSON & QUEUE
    DASH_JSON & QUEUE --> BUCKET
```

## Gating Logic

```mermaid
flowchart TD
    subgraph Extraction
        S1[Spec 1] --> G1{All specs pass?}
        S2[Spec 2] --> G1
        S3[Spec 3] --> G1
        G1 -->|Yes| SYNTH[Synthesis]
        G1 -->|No| STOP1[Stop - No Synthesis]
    end

    subgraph Pipeline
        SYNTH --> G2{Extraction complete?}
        G2 -->|Yes| ENRICH[Enrichment]
        G2 -->|No| STOP2[Stop - No Enrichment]
        ENRICH --> G3{Enrichment complete?}
        G3 -->|Yes| SYNC[Sync]
        G3 -->|No| STOP3[Stop - No Sync]
    end
```

## Execution Modes

```mermaid
flowchart TB
    subgraph Development
        CC[Claude Code CLI]
        SKILL[resin skill]
        CC --> SKILL
        SKILL --> SPECS[/run-specs]
    end

    subgraph Production
        CRON[Cron/Scheduler]
        CF[Cloudflare Worker]
        API[Claude API]
        CRON --> CF
        CF --> API
    end

    SPECS -.->|graduates to| CF
```
