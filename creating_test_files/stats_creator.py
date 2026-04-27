import csv
import random

titles = [
    "I quit IT and became a farmer",
    "How I learned Python in 7 days",
    "Why programmers hate meetings",
    "I built an app in one weekend",
    "How I got my first remote job",
    "Debugging nightmare story",
    "Secrets senior devs never tell you",
    "Why I switched from Java to Python",
    "I automated my boring work",
    "The truth about coding bootcamps"
]

for file_number in range(1, 101):
    filename = f"stats{file_number}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "title",
            "ctr",
            "retention_rate",
            "views",
            "likes",
            "avg_watch_time"
        ])

        for _ in range(20):
            title = random.choice(titles)
            ctr = round(random.uniform(5, 30), 1)
            retention = round(random.uniform(15, 95), 1)
            views = random.randint(1000, 500000)
            likes = random.randint(50, 20000)
            watch_time = round(random.uniform(1, 12), 1)

            writer.writerow([
                title,
                ctr,
                retention,
                views,
                likes,
                watch_time
            ])

print("100 CSV files created successfully.")