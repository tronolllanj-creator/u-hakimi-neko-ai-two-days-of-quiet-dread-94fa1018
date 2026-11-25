"""Entrypoint that writes a specific text line to the configured output directory."""
# Entry validated: output is 1-140 chars, one line, deterministic.

os = __import__('os')
pathlib = __import__('pathlib')

LINE = "I did not read the diff and the diff did not read me back, so we have achieved a fragile mutual peace."

def main():
    content = LINE + "\n"
    
    # Validate content according to rules
    if not (1 <= len(content) <= 140 and content.strip()):
        raise ValueError("Content validation failed")
    
    # Determine output directory
    out_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    primary_dir = pathlib.Path(out_dir_env)
    
    # Write to primary output directory
    primary_dir.mkdir(parents=True, exist_ok=True)
    primary_file = primary_dir / "entry.txt"
    primary_file.write_text(content, encoding="utf-8")
    
    # Best-effort write to /output if different
    default_dir = pathlib.Path("/output")
    if primary_dir.resolve() != default_dir.resolve():
        try:
            default_dir.mkdir(parents=True, exist_ok=True)
            (default_dir / "entry.txt").write_text(content, encoding="utf-8")
        except Exception:
            pass
            
    print(str(primary_file))
    print(len(content))

if __name__ == "__main__":
    main()
