from pathlib import Path

from youtube_clickbait.csv_reader import load_videos
from youtube_clickbait.reports import ClickbaitReport


def test_clickbait_report_filters_and_sorts(tmp_path: Path) -> None:
    file_path = tmp_path / "stats.csv"
    file_path.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "A,18,35,1,1,1\n"
        "B,25,20,1,1,1\n"
        "C,10,10,1,1,1\n"
        "D,20,45,1,1,1\n",
        encoding="utf-8",
    )

    rows = ClickbaitReport().build(load_videos([file_path]))

    assert [row["title"] for row in rows] == ["B", "A"]
    assert [row["ctr"] for row in rows] == [25.0, 18.0]
    assert [row["retention_rate"] for row in rows] == [20.0, 35.0]
