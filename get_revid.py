

def get_rev_id_for_article_in_20170601(article_name,date_expected_str):
    from mwclient import Site
    import datetime
    import time

    # construct date_expected
    date_expected = time.strptime(date_expected_str, "%d %b %Y")

    user_agent = 'Uni Koblenz-Landau student, vasilev@uni-koblenz.de'
    wiki = Site(host='en.wikipedia.org', clients_useragent=user_agent)
    start_profile_time = time.time()
    # Init biography page and output dict
    profile_page = wiki.pages[article_name]
    profile_list = dict()
    
    # Get all revisions of the biography page
    # Revisions are ordered chronologically (starting with newest rev)
    timestamp_revisions = profile_page.revisions(prop='ids|timestamp')
    print (timestamp_revisions)
    #print(date_expected)

    # print(date_expected.year)
    #print(type(date_expected))
    
    exp_rev_id = None
    for rev in timestamp_revisions:
        print (rev)

        # go back in time and read all revisions

        # ID and Upload date of the webpage
        timestamp_id = rev['revid']
        timestamp = rev['timestamp']

        #print(timestamp)
        # print(type(timestamp))
        
        #exp_rev_id = timestamp_id
        #print(timestamp, date_expected)
        if (timestamp <= date_expected):
            exp_rev_id = timestamp_id
            break
    return [exp_rev_id,timestamp]


if __name__ == "__main__":
    get_rev_id_for_article_in_20170601('Koblenz', "02 Jun 2017")


