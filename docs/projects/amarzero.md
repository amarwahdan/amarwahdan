# AmarZero — Architecture Brief

[Back to profile](../../README.md#featured-projects)

## System purpose

My research prototype explores predictive object tracking and planning through a proposed combination of transformer-based vision, Kalman state estimation, a learned world model, and Monte Carlo Tree Search.

## Engineering challenge

Connect perception, uncertainty-aware state estimation, transition prediction, and action search in a tracking loop—rather than treating localization as an isolated prediction.

## Documented data flow

```mermaid
flowchart LR
    F[Frames] --> V[ViT or CNN visual encoding]
    V --> K[Kalman state estimation]
    K --> W[Learned world model]
    W --> M[MCTS action search]
    M --> A[Tracking action]
    A -. next step .-> F
```

## Numeric evidence and status

The paper reports **1.35 px single-object** and **2.08 px multi-object** mean error. Checked-in CSVs correspond to limited experiments; see the scope and comparison notes in the architecture brief.

Research prototype and authored paper. The reported metrics do not establish full-dataset generalization, production real-time throughput, or superiority over every tracker.

## Technologies

Python · PyTorch / torchvision · ViT-B/16 · OpenCV · NumPy / pandas · Kalman filtering · Model-based RL · MCTS

### Research design versus implementation

The diagram summarizes the architecture proposed in the paper. The public scripts extract ViT features, but those extracted features are not passed into the Kalman/world-model decision path in the inspected implementation. The four-state estimate is `[x, y, vx, vy]`; the learned transition MLP is `6 → 128 → 64 → 4`. MCTS uses a discrete eight-action move set, with 50 simulations in single-object mode and 100 in multi-object mode.

### What the published numbers mean

The single-object CSV contains 19 rows with mean Euclidean center error **1.3511303962 px**. The multi-object CSV contains 60 rows spanning 20 frames and three IDs, with mean **2.0857977985 px**. The paper prints 1.35 px and 2.08 px. These are existing reported artifacts, not a newly reproduced evaluation. The scripts cap processing at 20 frames; the multi-object path reads ground-truth centers directly, while the single-object script uses the image center as the observation.

### Comparison discipline

The paper's comparison table lists multi-object errors of **2.08 px for AmarZero**, **35.6 px for Kalman**, and **1.2 px for DeepSORT**. Because lower error is better, that table does not support blanket superiority over DeepSORT. The conclusion's 40% occlusion-loss reduction lacks a published denominator and evaluation protocol, so it is not used as a profile headline metric. The paper identifies real-time edge deployment and improved initial localization as future work; no measured FPS or latency is asserted here.

## Original artifacts

- [Code repository](https://github.com/amarwahdan/AmarZero)
- [Paper / writeup](https://github.com/amarwahdan/AmarZero/blob/main/AmarZero%20paper%20v10.pdf)
- [Authored paper](https://github.com/amarwahdan/AmarZero/blob/main/AmarZero%20paper%20v10.pdf)
- [Single-object implementation](https://github.com/amarwahdan/AmarZero/blob/main/single_task/amarzero_single.py)
- [Multi-object implementation](https://github.com/amarwahdan/AmarZero/blob/main/multi_task/amarzero_multi.py)
- [Single-object evaluation CSV](https://github.com/amarwahdan/AmarZero/blob/main/evaluation%20single.csv)
- [Multi-object evaluation CSV](https://github.com/amarwahdan/AmarZero/blob/main/evaluation_multi%20%282%29.csv)
