import requests
import pytest

url_ddg = "https://api.duckduckgo.com"

resp = requests.get(url_ddg + "/?q=presidents of the united states&format=json")
rsp_data = resp.json()


def test_heading_is_presidents():
    assert "Presidents of the United States" in rsp_data["Heading"]


def test_related_topics_is_populated():
    assert len(rsp_data["RelatedTopics"]) > 0


LASTNAMES = [
    "Washington",
    "Adams",
    "Jefferson",
    "Madison",
    "Monroe",
    "Jackson",
    "Buren",
    "Harrison",
    "Tyler",
    "Polk",
    "Taylor",
    "Fillmore",
    "Pierce",
    "Buchanan",
    "Lincoln",
    "Johnson",
    "Grant",
    "Hayes",
    "Garfield",
    "Arthur",
    "Cleveland",
    "McKinley",
    "Roosevelt",
    "Taft",
    "Wilson",
    "Harding",
    "Coolidge",
    "Hoover",
    "Truman",
    "Eisenhower",
    "Kennedy",
    "Nixon",
    "Ford",
    "Carter",
    "Reagan",
    "Bush",
    "Clinton",
    "Obama",
    "Trump",
    "Biden"
]


@pytest.mark.parametrize("lastname", LASTNAMES)
def test_if_president_lastname_exists(lastname):
    exists = False

    for result in rsp_data["RelatedTopics"]:
        if lastname in result["Text"]:
            exists = True

    assert exists is True
