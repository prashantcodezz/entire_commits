import subprocess
from datetime import datetime, timedelta

DAYS_BACK = 7
COMMITS_PER_DAY = 2

start_date = datetime.now() - timedelta(days=DAYS_BACK)

for i in range(DAYS_BACK + 1):
    current_date = start_date + timedelta(days=i)

    for j in range(COMMITS_PER_DAY):
        # Slightly different time for each commit
        commit_time = current_date.replace(
            hour=10 + j,
            minute=30
        )

        date = commit_time.strftime("%Y-%m-%d %H:%M:%S")

        env = {
            "GIT_AUTHOR_DATE": date,
            "GIT_COMMITTER_DATE": date
        }

        print(f"Creating commit: {date}")

        subprocess.run(
            ["git", "commit", "--allow-empty", "-m", f"Test commit {i+1}-{j+1}"],
            env={**__import__("os").environ, **env},
            check=True
        )

print("\n✅ Test commits created successfully!")
print("Now check your test repository.")