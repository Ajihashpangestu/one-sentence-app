#!/usr/bin/env python3
"""You don't need to learn code — you need - entry for a make.fun judge bounty."""
import os

LINE = "You don't need to learn code — you need one sentence. Tell make.fun's AI agent your app idea, it builds it, enters it in a bounty, and you could get paid in USDC by tonight."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
