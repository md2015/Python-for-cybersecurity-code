# Update the GitHub Repository

Target repository: `md2015/Python-for-cybersecurity-code`

## GitHub website method

1. Extract the ZIP file on your computer.
2. Open the repository in GitHub.
3. Select **Add file**, then **Upload files**.
4. Open the extracted folder and drag its contents into the upload area. Upload the contents, not the outer folder itself.
5. Confirm that the paths begin with `tools/`, `tests/`, `sample-data/`, and the root files such as `README.md`.
6. Enter this commit message: `Update companion code to final corrected manuscript edition`.
7. Select **Commit directly to the main branch**, then commit the changes.

## Git command method

```bash
git clone https://github.com/md2015/Python-for-cybersecurity-code.git
cd Python-for-cybersecurity-code
```

Copy the contents of the extracted update package into the cloned repository, replacing matching files. Then run:

```bash
git add -A
git commit -m "Update companion code to final corrected manuscript edition"
git push origin main
```

After the upload, open the **Actions** tab. The automated test workflow should finish with a green check mark.
