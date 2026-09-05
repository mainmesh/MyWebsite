import subprocess, sys

try:
    r = subprocess.run(
        ["curl.exe", "-sS", "http://127.0.0.1:8000/"],
        capture_output=True, text=True, check=True, timeout=15
    )
    html = r.stdout
    print("STATUS: 200 (assumed)")
    print("LEN:", len(html))
    checks = [
        "Kimeta Capital",
        "initializing meshack.dev",
        "terminal",
        "case-study",
        "meshack@dev",
        "Meshack Mbithi",
        "Django · PostgreSQL · HTMX",
    ]
    for c in checks:
        ok = "OK" if c in html else "MISS"
        print(f"  [{ok}] {c}")
except Exception as e:
    print("ERROR:", e)
    sys.exit(1)
