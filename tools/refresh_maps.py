import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SCRIPTS = [
    "tools/generate_project_index.py",
    "tools/generate_asset_index.py",
    "tools/generate_dashboard_data.py",
    "tools/generate_xmind.py",
    "tools/generate_operation_flow_xmind.py",
    "tools/generate_file_responsibility_xmind.py",
]


def main():
    for script in SCRIPTS:
        print(f"正在刷新：{script}")
        result = subprocess.run(
            [sys.executable, script],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.stdout:
            print(result.stdout.strip())
        if result.stderr:
            print(result.stderr.strip(), file=sys.stderr)
        if result.returncode != 0:
            raise SystemExit(result.returncode)

    print("全部可视化视图已刷新。")


if __name__ == "__main__":
    main()
