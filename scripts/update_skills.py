from pathlib import Path

import requests

EXE_DIR = Path(__file__).parent.parent
SKILLS_DIR = EXE_DIR / "moltbook_skills"


def download_file(url: str, filename: str) -> None:
    save_path = SKILLS_DIR / filename
    save_path.parent.mkdir(parents=True, exist_ok=True)  # create folders if needed

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with save_path.open("wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)


if __name__ == "__main__":
    download_file("https://www.moltbook.com/skill.md", "skill.md")
    download_file("https://www.moltbook.com/heartbeat.md", "heartbeat.md")
    download_file("https://www.moltbook.com/rules.md", "rules.md")
    download_file("https://www.moltbook.com/skill.json", "skill.json")
