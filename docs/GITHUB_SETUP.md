# GitHub setup and contribution tracking

## One-time setup (owner)

1. Create a **private** repo (no README/licence/.gitignore added by GitHub).
2. Push this project (`git init`, `git add .`, `git commit`, `git branch -M main`, `git remote add origin <url>`, `git push -u origin main`).
3. Invite your friend as a collaborator (repo Settings, Collaborators).
4. Protect `main`: require a pull request and at least 1 approval before merging (Settings, Branches or Rules).
5. In Settings, General, Pull Requests: allow **squash merging only**, and turn on "automatically delete head branches".

## Each person, on their own machine

```bash
git config user.name  "Your Name"
git config user.email "the-email-linked-to-your-GitHub-account"
```

GitHub only credits commits to an account if the commit email is added to that account (use the GitHub no-reply address if you want to keep your email private). Commits with an unlinked email will not appear on your profile or in the contributor graph.

## Tracking who is doing what

| Need | Where | Setup |
|---|---|---|
| Task board | Projects tab, new project, Board layout | Columns: Todo, In progress, In review, Done. Add the repo's issues; assign each to its owner |
| Weekly plan | Issues, Milestones | Create `Week 1` to `Week 6` and `Final`; set due dates; attach each issue to its week |
| Module view | Issues, Labels | `crowd`, `violence`, `tracking`, `pose`, `harassment`, `fusion`, `dashboard`, `evaluation`, `data`, `docs` |
| Who owns it | Issue assignee | One assignee per issue |
| Code review trail | Pull requests | Every change goes through a PR the other person reviews |
| Activity graphs | Insights, Contributors | Automatic: commits, additions, deletions per person |
| Written summary | `python scripts/contribution_report.py --md` | Generates docs/CONTRIBUTIONS.md from git history |

If one person commits under two emails, add a `.mailmap` file at the repo root so they are counted once:

```
Your Name <primary-email@example.com> <other-email@example.com>
```

## Reading the numbers honestly

Commits and lines of code are weak signals. Squash merges collapse many commits into one, generated or pasted code inflates lines, and reviewing, designing, collecting data and testing leave no lines. For your viva or report, use the project board, merged PRs and review history as evidence, and be able to explain your own modules.
