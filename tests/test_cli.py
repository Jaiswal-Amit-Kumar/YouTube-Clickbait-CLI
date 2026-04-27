from pathlib import Path

from youtube_clickbait.cli import main


def test_main_prints_table(tmp_path: Path, capsys) -> None:
    file_path = tmp_path / "stats.csv"
    file_path.write_text(
        "title,ctr,retention_rate\n"
        "A,18,35\n",
        encoding="utf-8",
    )

    exit_code = main(["--files", str(file_path), "--report", "clickbait"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "A" in captured.out
    assert "18.0" in captured.out
    assert "35.0" in captured.out


def test_main_rejects_unknown_report(capsys) -> None:
    exit_code = main(["--files", "missing.csv", "--report", "unknown"])
    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Unknown report: unknown" in captured.err


def test_main_rejects_missing_file(capsys) -> None:
    exit_code = main(["--files", "missing.csv", "--report", "clickbait"])
    captured = capsys.readouterr()

    assert exit_code == 1
    assert "File not found: missing.csv" in captured.err
