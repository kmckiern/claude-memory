#!/usr/bin/env python3
"""
Generate CLAUDE.md files by combining global patterns with repo-specific content.
"""

import sys
from pathlib import Path

def read_file(path):
    """Read file content, return empty string if file doesn't exist."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""

def write_file(path, content):
    """Write content to file."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_claude_md(repo_name, base_dir=None):
    """Generate CLAUDE.md for a specific repo."""
    if base_dir is None:
        # Assume script is in tools/ directory
        base_dir = Path(__file__).parent.parent
    else:
        base_dir = Path(base_dir)
    
    # Read source files
    global_patterns = read_file(base_dir / "global" / "DEVELOPMENT_PATTERNS.md")
    repo_content = read_file(base_dir / "repos" / repo_name / "repo.md")
    
    if not repo_content:
        print(f"Warning: No repo.md found for {repo_name}")
        return False
    
    # Remove the top-level heading from global patterns for combining
    global_lines = global_patterns.split('\n')
    if global_lines and global_lines[0].startswith('# '):
        global_lines = global_lines[1:]  # Remove first line
        if global_lines and global_lines[0] == '':
            global_lines = global_lines[1:]  # Remove empty line after heading
    global_content = '\n'.join(global_lines)
    
    # Remove the top-level heading from repo content for combining
    repo_lines = repo_content.split('\n')
    if repo_lines and repo_lines[0].startswith('# '):
        repo_lines = repo_lines[1:]  # Remove first line
        if repo_lines and repo_lines[0] == '':
            repo_lines = repo_lines[1:]  # Remove empty line after heading
    clean_repo_content = '\n'.join(repo_lines)
    
    # Combine content
    combined_content = f"""# CLAUDE.md - {repo_name}

{clean_repo_content}

---

# Global Development Patterns

{global_content}"""
    
    # Write combined file
    output_path = base_dir / "repos" / repo_name / "CLAUDE.md"
    write_file(output_path, combined_content)
    print(f"Generated {output_path}")
    return True

def find_repos(base_dir=None):
    """Find all repo directories."""
    if base_dir is None:
        base_dir = Path(__file__).parent.parent
    else:
        base_dir = Path(base_dir)
    
    repos_dir = base_dir / "repos"
    if not repos_dir.exists():
        return []
    
    repos = []
    for item in repos_dir.iterdir():
        if item.is_dir() and (item / "repo.md").exists():
            repos.append(item.name)
    
    return repos

def main():
    """Main function - generate CLAUDE.md for all repos or specific repo."""
    base_dir = None
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help":
            print("Usage: generate-claude-md.py [repo_name] [--base-dir /path/to/claude-memory]")
            print("  If no repo_name provided, generates for all repos")
            return
        elif sys.argv[1] == "--base-dir":
            if len(sys.argv) < 3:
                print("Error: --base-dir requires a path")
                sys.exit(1)
            base_dir = sys.argv[2]
            target_repos = find_repos(base_dir)
        elif not sys.argv[1].startswith("--"):
            # Specific repo requested
            target_repos = [sys.argv[1]]
            if len(sys.argv) > 3 and sys.argv[2] == "--base-dir":
                base_dir = sys.argv[3]
        else:
            target_repos = find_repos(base_dir)
    else:
        # Generate for all repos
        target_repos = find_repos(base_dir)
    
    if not target_repos:
        print("No repos found with repo.md files")
        return
    
    success_count = 0
    for repo in target_repos:
        if generate_claude_md(repo, base_dir):
            success_count += 1
    
    print(f"Generated CLAUDE.md for {success_count}/{len(target_repos)} repos")

if __name__ == "__main__":
    main()