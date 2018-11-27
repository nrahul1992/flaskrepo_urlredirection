# Run this module once to create the JIRA issues collections. This will work as a data source for Chat application where
# the user query will be processed against.
# DB used- CHATAPP, Collection used- jiradatasource
# jql- Modify the Jira project
from __future__ import print_function
import pysolr

import ChatHandler

from pymongo import MongoClient
from jira.client import JIRA



client = MongoClient('localhost', 27017)
db2 = client.CHATAPP


def solrTest():
    # Setup a basic Solr instance. The timeout is optional.
    solr = pysolr.Solr('http://localhost:8983/solr/', timeout=10)
    print("Connected to solr")

    # How you would index data.
    solr.add([
        {
            "id": "doc_1",
            "title": "A very small test document about elmo",
        }
    ])

    #searching
    results = solr.search('elmo')
    print("result is", results)
    print("Saw {0} result(s).".format(len(results)))


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
            db2.jiradatasource.insert_one(insertQuery)
            # print(insertQuery)

queryJira2()

#solrTest()