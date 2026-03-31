## SentinelAI

AI-powered asset risk intelligence platform built on Mantle.

SentinelAI continuously monitors DeFi assets across chains, predicts depeg events and liquidity crises before they occur, and enables semi-automatic fund rerouting — letting AI handle detection while humans retain final approval on every action.



## What It Does

**Risk Scoring**
Real-time 0–100 risk scores per asset, updated continuously from on-chain data including peg deviation, collateral ratios, liquidity depth, and wallet flow anomalies.

**Early Warning Alerts**
Fires notifications when asset risk crosses user-defined thresholds, with plain-language summaries of what's wrong and why.

**1-Click Rerouting**
Pre-built rerouting recommendations ready to approve and execute atomically via Mantle smart contracts.

---

## Mantle Integration

| Touchpoint | Role |
|---|---|
| Smart Contract Execution | Atomic swap + deposit in a single transaction |
| Mantle DEX Liquidity Pools | Real-time pool depth and slippage data for routing |
| DAO Treasury Vaults | Institutional risk dashboard with governance hooks |
| mETH Protocol (LST) | Safe-haven destination for high-risk rerouting events |

---

## Target Users

- DeFi power users and whales with cross-chain exposure
- DAOs and protocol treasuries managing large stablecoin positions
- Protocols running liquidity pools on Mantle

---

## Stack (Concept)

- On-chain indexer across Mantle, Ethereum, Arbitrum
- LSTM + gradient boosting AI models trained on historical crisis data
- Mantle smart contracts for atomic execution
- Web dashboard with alert feed, risk meters, and 1-click action UI

---

## This Repository

This repo contains the concept UI — a static HTML/CSS mockup of the SentinelAI dashboard built as part of the Mantle ecosystem submission.

---

## SentinelAI (Backend Prototype)

AI-powered DeFi risk monitoring engine.

## Features
- Real-time risk scoring
- Early warning detection
- Action suggestion (asset rerouting)

## Run
```bash
python sentinelAI.py
```


*Built for the Mantle ecosystem. Concept submission tagging @Mantle_Official.*
