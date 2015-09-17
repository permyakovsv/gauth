# gauth
Simple google api oauth library

Import this script for singing in into google api with one string
For example:
```python
import gauth
CLIENT_SECRETS = 'secret.json'
OAUTH2_STORAGE = 'reports_oauth2.dat'
GCE_SCOPE = 'https://www.googleapis.com/auth/admin.reports.usage.readonly'

auth_http = gauth.signin(CLIENT_SECRETS, OAUTH2_STORAGE, GCE_SCOPE)
reports_service = build('admin', 'reports_v1')
reports_service.userUsageReport().get(userKey=account, date=CUR_DATE ).execute(http=auth_http)
```
