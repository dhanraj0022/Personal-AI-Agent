import git

def push(message):
    repo = git.Repo(search_parent_directories=True)
    repo.git.add(all=True)
    repo.index.commit(message)
    repo.remote(name="origin").push()

    print("✅ Pushed to GitHub")
