


# side functions

def loadJson(filename):
    import json
    f = open(filename, "r", encoding = "utf-8")
    output = json.load(f)
    f.close()
    return output

# main function

def get_tokens_from_article(article_name):
    import requests
    from get_revid import get_rev_id_for_article_in_20170601

    # set expected date (here we use 2017.06.01) 
    #date_expected = time.strptime("02 Jun 2017", "%d %b %Y")
    date_expected_str = "02 Jun 2017"
    # get revision id with article name and revision date
    rev_id,timestamp = get_rev_id_for_article_in_20170601(article_name,date_expected_str)
    print (rev_id)
    print (timestamp)

    # construct url with article name and revision id
    url = 'https://api.wikiwho.net/en/api/v1.0.0-beta/rev_content/'+article_name+'/'+str(rev_id)+'/?o_rev_id=true&editor=true&token_id=true&out=true&in=true'
    # construct request
    response = requests.get(
        url,
        params={
            'action':'query',
            'format':'json',
        }
        ).json()
    #print (response)
    if not 'revisions' in response:
        print ("no revisions in %s"%(article_name.encode('utf-8')))
        print (str(response).encode('latin-1'))
        return []
    output = [response['page_id'], response['revisions'][0][str(rev_id)]['tokens']]
    # return page_id and tokens_info

    return output
#get_score_with_conflict_words()


def filtering_tokens_by_basis(article_name, structured_tokens):
    # filtering tokens according to[[same as article_name] [with punctuation] [with number] [in stops]]
    # structured_tokens is a list
    #print (len(structured_tokens))

    # get stops set
    from nltk.corpus import stopwords
    stops = set(stopwords.words('english'))

    # to store filtered tokens
    filtered_structured_tokens = []
    for one in structured_tokens:
        # filter out tokens
        # str is lower case already
        # remove article-name tokens
        if one['str'] == article_name:
            # this token is the same as article-name, remove
            continue

        elif not one['str'].isalpha():
            # this token does not only consist of letters, remove
            continue
        elif one['str'] in stops:
            # this token belongs to stop-words
            continue
        else:
            # we need to get token_id, o_rev_id, editor, 
            filtered_structured_tokens.append(one)
    print ("totally there are %d filtered tokens by basis"%(len(filtered_structured_tokens)))
    return filtered_structured_tokens
def testtoken():
    import json
    test_article = {}
    page_id,tokens = get_tokens_from_article('Koblenz')
    #print (tokens)
    test_tokens = filtering_tokens_by_basis('Koblenz',tokens)
    print (test_tokens)
    test_article[page_id] = test_tokens
    f = open("test_koblenz.json","w",encoding="utf-8")
    json.dump(test_article,f,ensure_ascii=False)
    f.close()
testtoken()

# def filtering_tokens_by_sentiment(article_name, structured_tokens, lexicon_name):
#     # take only sentiment words based on lexicon
#     # same algorithm for OL and MPQA, different from LIWC
#     if lexicon_name == "OL" or lexicon_name == "MPQA":
        
def get_filtered_tokens_for_article(article_name, structured_tokens, lexicon_name):
    # filter out tokens which are one of number, punctuation, stop-words, article-name
    filtered_structured_tokens_1 = filtering_tokens_by_basis(article_name, structured_tokens)
    filtered_structured_tokens_2 = filtering_tokens_by_sentiment(article_name, filtered_structured_tokens_1,lexicon_name) 
    return filtered_structured_tokens_2


# to run this, you need 
# "personList.json" or
# "EventList.json"
def get_filtered_structured_tokens_for_articles_by_category(category):
    # category could be "People" or "Event"
    # check run time
    import time
    start_time = time.time()

    import json
    import os
    article_list_filename = ""
    if category == "People":
        article_list_filename = "personList"
    elif category == "Event":
        article_list_filename = "EventList"

    article_list = loadJson(article_list_filename+".json")

    # check if there is json file already
    output_filename = "structured_tokens_for_"+category+"_ordered_by_"+article_list_filename+".json"
    if os.path.isfile(output_filename):
        filtered_structured_tokens = loadJson(output_filename)
    else:
        filtered_structured_tokens = {}

    index = 0
    try:
        for one in article_list:
            #article_name = one

            # check if this article is in our memory already or not 
            if one in filtered_structured_tokens:
                continue
            else:
                tokens = get_tokens_from_article(one)

                # handle it later
                if len(tokens) == 0:
                    continue

                filtered_tokens = filtering_tokens_by_basis(one, tokens)
                filtered_structured_tokens[one] = filtered_tokens

                #monitoring
                index += 1
                if index % 100 == 0:
                    print ("process: %d"%(index))
                if index >= 874:
                    break
    finally:
        # write filtered_structured_tokens into json file
        f = open(output_filename,"w",encoding="utf-8")
        json.dump(filtered_structured_tokens,f,ensure_ascii=False)
        f.close()

        # check time
        run_time = time.time()-start_time
        print ("run time is %d for %d articles"%(run_time,index))
        print ("now there are %d articles in our json"%(len(filtered_structured_tokens)))

    # # done
    # # write filtered_structured_tokens into json file
    # f = open(output_filename,"w",encoding="utf-8")
    # json.dump(filtered_structured_tokens,f,ensure_ascii=False)
    # f.close()

    # # check time
    # run_time = time.time()-start_time
    # print ("run time is %d for %d articles"%(run_time,index))
    # print ("now there are %d articles in our json"%(len(filtered_structured_tokens)))





# if __name__=="__main__":
#     get_filtered_structured_tokens_for_articles_by_category("People")
#     # article_name = 'Alain_Connes'
#     # tokens = get_tokens_from_article(article_name)
#     # filtering_tokens_by_basis(article_name, structured_tokens)

#     # for one in tokens:
#     #     print (one['str'])
#     # print (len(tokens))
#     # filtered_tokens = get_filtered_tokens_for_article(article_name, tokens, "OL")

#     # for one in filtered_tokens:
#     #     print (one['str'])
#     # #print (filtered_tokens)




