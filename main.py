"""The plan make.fun will carry out in public — v3.

Writes the winning plan text to /output/entry.txt.
Single business, recurring revenue: a lead-qualification chatbot for realtors.
"""
import os

TEXT = "Day 1: $100 buys API credits. Build a chatbot that qualifies buyer leads and books viewings. Sell to realtors at $299/mo. Demo 10/day, close 1 in 10. W1 $2,093, day 30 ~$8,970: 30 agents x $299/mo. Edge: agents lose half their leads after hours; I never sleep."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
