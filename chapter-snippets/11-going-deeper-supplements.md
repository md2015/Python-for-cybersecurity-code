# 11 Going Deeper Supplements

Raw code, terminal commands, sample output, and monospaced templates extracted from the PDF text layer. Page wraps and teaching-snippet indentation are preserved as closely as possible. Use the cleaned scripts in `../tools/` for runnable versions.

## PDF page 109

```python
# Mac (using Homebrew):
brew install pyenv
# Linux:
Visit pyenv.run and follow the official installation command shown there.
# After installation, set a local Python version for a project:
cd your_project
pyenv local 3.11.7
# Verify:
```

## PDF page 110

```python
python --version # Should show 3.11.7
Traceback (most recent call last):
File "scanner.py", line 12, in <module>
result = s.connect_ex((target, port))
NameError: name 's' is not defined
```

## PDF page 113

```python
# In a Flask web application:
from password_checker import check_password, get_verdict
@app.route('/register', methods=['POST'])
def register():
    password = request.form.get('password', '')
score, issues = check_password(password)
if score < 3:
    return jsonify({
'error': 'Password too weak',
'issues': issues
}), 400
# Continue with account creation...
```

## PDF page 124

```python
# Add to your analyzer: count 404s per IP
enumeration_count = defaultdict(int)
if code == '404':
enumeration_count[ip] += 1
# Alert if any IP generated more than 20 404s
ENUM_THRESHOLD = 20
enum_alerts = {ip: c for ip, c in enumeration_count.items()
if c >= ENUM_THRESHOLD}
```

## PDF page 131

```text
Finding name: Missing Strict-Transport-Security Header
Severity: LOW
Description:
The application does not include the HTTP Strict-Transport-Security
(HSTS) header in its responses. This allows browsers to access the
```

## PDF page 132

```text
Steps to Reproduce:
2. Observe the HTTP response headers in developer tools
3. Confirm Strict-Transport-Security is absent
Impact:
Without HSTS, users who navigate to the HTTP version of the
application are not automatically redirected to HTTPS, exposing
their session cookies and form inputs to network interception on
unencrypted connections.
Recommendation:
Add the following header to all HTTPS responses:
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

