# Import this script for singing in into google api with one string
# For example:
#  import gauth
#  CLIENT_SECRETS = 'secret.json'
#  OAUTH2_STORAGE = 'reports_oauth2.dat'
#  GCE_SCOPE = 'https://www.googleapis.com/auth/admin.reports.usage.readonly'
#
#  auth_http = gauth.signin(CLIENT_SECRETS, OAUTH2_STORAGE, GCE_SCOPE)
#  reports_service = build('admin', 'reports_v1')
#  reports_service.userUsageReport().get(userKey=account, date=CUR_DATE ).execute(http=auth_http)

import httplib2
import argparse
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from oauth2client import tools


def signin(clientSecretsPath, storage, scope, args=[]):

    parser = argparse.ArgumentParser(parents=[tools.argparser])

  # Parse the command-line flags.
    flags = parser.parse_args(args)

    CLIENT_SECRETS = clientSecretsPath
    OAUTH2_STORAGE = storage
    GCE_SCOPE = scope


  # Perform OAuth 2.0 authorization.
    flow = flow_from_clientsecrets(CLIENT_SECRETS, scope=GCE_SCOPE)
    storage = Storage(OAUTH2_STORAGE)
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage, flags)
    http = httplib2.Http()
    auth_http = credentials.authorize(http)
    return auth_http

