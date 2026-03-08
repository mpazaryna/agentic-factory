---
description: Run only MLX processor tests
tags: [test, mlx, ai]
---

# Test MLX Processors

Run only the MLX integration tests (ICD-10, CPT, Vertebral Level processors).

```bash
cd pab && xcodebuild test -project pab.xcodeproj -scheme pab -only-testing:pabTests/MLXIntegrationTests
```

**What gets tested:**
- `ICD10MLXProcessor` - Diagnostic code predictions
- `CPTCodeMLXProcessor` - Procedure billing code predictions
- `VertebralLevelMLXProcessor` - Vertebral notation expansion
- Model loading and inference pipelines
- Sigmoid activation (multi-label classification)

**Common Issues:**
1. **Models not loading:**
   - Check cache: `ls ~/Library/Containers/paz.pab/Data/Library/Caches/MLXModels/`
   - Clear cache: `rm -rf ~/Library/Containers/paz.pab/Data/Library/Caches/MLXModels/`
   - Restart app to re-download from HuggingFace

2. **Zero predictions:**
   - Verify sigmoid (not softmax) in `MLXUtils.swift:212`
   - Check model metadata for confidence thresholds

3. **Model format issues:**
   - Safetensors preferred over NPZ
   - Verify metadata JSON exists alongside model files

**Related:**
- `/test` - Run full test suite
- `/diagnose` - Debug MLX model loading
- MLX training workflow: `../mlx/.claude/README.md`
