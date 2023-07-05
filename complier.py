from os import system

PATH = "Sources/main.swift"
OUTPUT = "main.run"

system(f"swiftc -o {OUTPUT} {PATH}")
system(f"./{OUTPUT}")