### Git docs

#### Creating Snapshots

> **Staging Files**

- Stage multiple file

```
git add file_name file_name

```

- Stages with a pattern

```
git add *.file_extention

```

- Stages the current directory and all its content

```
git add .

```

- Skipping the staging area

```
git commit -am “commit message”

```

> **Removing files**

- removes from working directory and staging area

```
git rm file_name

```

- removes from staging area only

```
git rm file_name

```

> **renaming files**

```
git mv previouse_name new_name

```

> **Viewing the staged/unstaged changes**

- Shows unstaged changes

```
git diff

```

- Shows staged changes

```
git diff --staged

```

- Shows staged changes

```
git diff --cached

```

> **Unstaging files (undoing git add)**

- Copies the last version of file from repo to index

```
git restore --staged file_name

```

> **Discarding local changes**

- Restores files in working directory

```
git restore file_name another_file_name

```

- Discards all local changes (except untracked files)

```
git restore .

```

- Removes all untracked files

```
git clean -fd

```

> **Restoring an earlier version of a file**

```
git restore --source=HEAD~2 file_name

```

> **Viewing the history**

- Full history

```
git log

```

- summary in one line

```
git log --oneline

```

- Shows log in reverse order

```
git log --reverse

```

> **Viewing a commit**

- Shows the given commit

```
git show commit_id

```

- Shows the last commit

```
git show HEAD

```

- Two steps before the last commit

```
git show HEAD~2

```

- Shows the version of the file in that commit

```
git show HEAD:file_name

```
