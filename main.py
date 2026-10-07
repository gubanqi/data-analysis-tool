from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).parent
DATA_FILE = ROOT / "data" / "scores.xlsx"
RESULTS_DIR = ROOT / "results"
FIGURES_DIR = ROOT / "figures"

SUBJECTS = ["语文", "数学", "英语"]


def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"找不到成绩表：{DATA_FILE}")

    data = pd.read_excel(DATA_FILE)

    required_columns = ["姓名", *SUBJECTS]
    missing_columns = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(f"成绩表缺少这些列：{missing_columns}")

    scores = data[SUBJECTS].apply(
        pd.to_numeric,
        errors="coerce",
    )

    data["总分"] = scores.sum(axis=1)
    data["平均分"] = scores.mean(axis=1).round(2)
    data["排名"] = (
        data["总分"]
        .rank(method="min", ascending=False)
        .astype(int)
    )

    data = data.sort_values("排名")

    RESULTS_DIR.mkdir(exist_ok=True)
    FIGURES_DIR.mkdir(exist_ok=True)

    result_file = RESULTS_DIR / "成绩分析结果.xlsx"
    data.to_excel(result_file, index=False)

    subject_averages = scores.mean()

    subject_averages.plot(
        kind="bar",
        color=["#4C78A8", "#F58518", "#54A24B"],
        title="Average Score by Subject",
    )

    plt.xlabel("Subject")
    plt.ylabel("Average Score")
    plt.xticks(
        range(len(SUBJECTS)),
        ["Chinese", "Math", "English"],
        rotation=0,
    )
    plt.tight_layout()

    figure_file = FIGURES_DIR / "各科平均分.png"
    plt.savefig(figure_file, dpi=200)
    plt.close()

    print("分析完成")
    print(f"结果表：{result_file}")
    print(f"统计图：{figure_file}")


if __name__ == "__main__":
    main()