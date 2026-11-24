#!/usr/bin/env python3
"""You don't need to learn code — you need - entry for a make.fun judge bounty."""
import os

LINE = "The app idea in your notes app has been free for years. Tonight it can start paying you: one sentence to make.fun's AI agent, a working app back, and a bounty entry that pays real USDC."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
