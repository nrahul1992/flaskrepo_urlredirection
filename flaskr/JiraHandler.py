# Run this module once to create the JIRA issues collections. This will work as a data source for Chat application where
# the user query will be processed against.
# DB used- CHATAPP, Collection used- jiradatasource
# jql- Modify the Jira project
import ChatHandler

from jira.client import JIRA


def queryJira2():
    jira_server = "https://www.myjira.nl"
    jira_user = "Noupada.RahulAchary"
    jira_password = "yamahaYZFR1$"

    jira_server = {'server': jira_server}
    jira = JIRA(options=jira_server, basic_auth=(jira_user, jira_password))
    print("Entry into jira successfull")
    jql = 'project = KWCMSLIVE AND issuetype in standardIssueTypes() AND status in (Closed, Done)'
    block_size = 100
    block_num = 0
    while True:
        start_idx = block_num * block_size
        issues = jira.search_issues(jql, start_idx, block_size)
        if len(issues) == 0:
            # Retrieve issues until there are no more to come
            break
        block_num += 1
        for issue in issues:
            issueSummaryLexeme = ChatHandler.parseText(issue.fields.summary)
            insertQuery = dict()
            insertQuery['issueKey'] = issue.key
            insertQuery['issueId'] = issue.id
            insertQuery['issueSummary'] = issue.fields.summary
            insertQuery['issueSummaryLexeme'] = issueSummaryLexeme
            print(insertQuery)

queryJira2()

