import os
import random
import subprocess
from datetime import datetime, timedelta

DAYS_BACK = 365
start_date = datetime.now() - timedelta(days=DAYS_BACK)

total_created = 0

# Alternate days (step of 2)
for i in range(0, DAYS_BACK + 1, 2):
    current_date = start_date + timedelta(days=i)
    # 1 to 3 random commits on alternate days
    num_commits = random.randint(1, 3)

    for j in range(num_commits):
        hour = random.randint(9, 22)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        commit_time = current_date.replace(hour=hour, minute=minute, second=second)

        date = commit_time.strftime("%Y-%m-%d %H:%M:%S")

        env = {
            "GIT_AUTHOR_NAME": "prashantcodezz",
            "GIT_AUTHOR_EMAIL": "pkgope6743@gmail.com",
            "GIT_COMMITTER_NAME": "prashantcodezz",
            "GIT_COMMITTER_EMAIL": "pkgope6743@gmail.com",
            "GIT_AUTHOR_DATE": date,
            "GIT_COMMITTER_DATE": date,
        }

        subprocess.run(
            ["git", "commit", "--allow-empty", "-m", f"Activity log {i+1}-{j+1}"],
            env={**os.environ, **env},
            check=True
        )
        total_created += 1

print(f"\n✅ {total_created} commits created successfully across alternate days!")