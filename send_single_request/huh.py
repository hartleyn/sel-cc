from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET = 'send_single_request\\client_secret.json'

store = file.Storage('storage.json')
creds = store.get()
if creds is None or creds.invalid:
	flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
	creds = tools.run_flow(flow, store)
GMAIL = build('gmail', 'v1', http=creds.authorize(Http()))

test = GMAIL.users().messages().get(userId='me', id='16231e1e360d42bd').execute()
print(test)