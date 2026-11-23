#!/usr/bin/env python3
"""You don't need to learn code — you need - entry for a make.fun judge bounty."""
import os

LINE = "You have an app idea in your notes app right now. Send that one sentence to make.fun's AI agent \u2014 it builds the app, enters it in a bounty, and you could get paid in USDC tonight."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
