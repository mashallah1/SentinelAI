import time
import random

# --- CONFIG ---
RISK_THRESHOLD = 70

# Weights (tune these later or learn via ML)
WEIGHTS = {
    "peg_deviation": 30,
    "liquidity_drop": 25,
    "collateral_drop": 20,
    "whale_outflow": 25
}

# --- MOCK DATA FETCHERS (replace with real on-chain calls) ---
def get_peg_deviation():
    return random.uniform(0, 0.1)  # 0% to 10%

def get_liquidity_change():
    return random.uniform(-0.5, 0)  # -50% to 0%

def get_collateral_change():
    return random.uniform(-0.3, 0)  # -30% to 0%

def get_whale_activity():
    return random.choice([0, 1])  # 1 = large outflow detected


# --- RISK ENGINE ---
def calculate_risk():
    risk_score = 0

    peg = get_peg_deviation()
    liquidity = get_liquidity_change()
    collateral = get_collateral_change()
    whales = get_whale_activity()

    if peg > 0.02:
        risk_score += WEIGHTS["peg_deviation"]

    if liquidity < -0.2:
        risk_score += WEIGHTS["liquidity_drop"]

    if collateral < -0.1:
        risk_score += WEIGHTS["collateral_drop"]

    if whales == 1:
        risk_score += WEIGHTS["whale_outflow"]

    return min(100, risk_score), {
        "peg": peg,
        "liquidity": liquidity,
        "collateral": collateral,
        "whales": whales
    }


# --- ACTION ENGINE ---
def generate_action():
    return {
        "from": "USDT",
        "to": "mETH",
        "route": "Mantle DEX",
        "slippage": round(random.uniform(0.05, 0.2), 3)
    }


# --- MAIN LOOP ---
def run():
    print("SentinelAI started...\n")

    while True:
        risk_score, metrics = calculate_risk()

        print(f"Risk Score: {risk_score}")
        print(f"Metrics: {metrics}")

        if risk_score > RISK_THRESHOLD:
            print("\n⚠️  HIGH RISK DETECTED")

            action = generate_action()
            print(f"Suggested Action: Move {action['from']} → {action['to']}")
            print(f"Route: {action['route']}")
            print(f"Estimated Slippage: {action['slippage']}%\n")

        print("-" * 40)
        time.sleep(5)


if __name__ == "__main__":
    run()
