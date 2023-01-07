import praw
import random
import madlibs
import time


    
def get_topic_comments(submission):
    """(object) -> list
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/eay2ne/mcgill_subreddit_bingo_finals_edition/'
    >>> submission = reddit.submission(url=url)
    >>> get_topic_comments(submission)
    [Comment(id='fb0vh26'), Comment(id='fb0l4dk'), Comment(id='fb15bvy'), \
    Comment(id='fb1pwq8'), Comment(id='fb26drr'), Comment(id='fj2wd6x'), \
    Comment(id='i11plzg'), Comment(id='fb1spzv'), Comment(id='fb1td2g'), \
    Comment(id='fb1trul')]
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/bj29g8/quantitative_biology_vs_csbiology/'
    >>> submission = reddit.submission(url=url)
    >>> get_topic_comments(submission)
    [Comment(id='em4q0fh'), Comment(id='em4wbj3'), Comment(id='em4z5xu'), \
    Comment(id='em5frig'), Comment(id='em4ymbw'), Comment(id='em5dc96'), \
    Comment(id='em5hzwd'), Comment(id='em6eht5'), Comment(id='em5kftw'), \
    Comment(id='em5ne3e'), Comment(id='em6n63n'), Comment(id='em5pkw6'), Comment(id='em5uk2l')]
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/dve1xh/comp_204_or_phgy_210/'
    >>> submission = reddit.submission(url=url)
    >>> get_topic_comments(submission)
    [Comment(id='f7chgnh'), Comment(id='f7e9vf7')]
    """
    
    return submission.comments.list()


def filter_comments_from_authors(comments, list_of_author_names):
    """
    (object, list) -> list
    >>> url = 'https://www.reddit.com/r/mcgill/comments/paf85s/the_only_society_we_deserve/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_comments_from_authors(comments, ['recursion_is_fun'])
    [Comment(id='ha4piat'), Comment(id='ha4j1r7')]
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/dve1xh/comp_204_or_phgy_210/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_comments_from_authors(comments, ['recursion_is_fun'])
    [Comment(id='f7chgnh')]
    
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/1wfq5s/should_i_switch_majors/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_comments_from_authors(comments, ['Fitbumblebee', 'xcpram'])
    [Comment(id='cf1ls9i'), Comment(id='cf1luq7'), Comment(id='cf212j0'), Comment(id='cf21ah7')]
    """
    
    targetted_comment = []
    
    for  comment in comments:
        if comment.author in list_of_author_names:
            targetted_comment.append(comment)
        
    return targetted_comment


def filter_out_comments_replied_to_by_authors(comments, list_of_author_names):
    """(comments, list) -> list
    >>> url = 'https://www.reddit.com/r/mcgill/comments/pa6ntd/does_mcgill_have_a_taylor_swift_society/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_out_comments_replied_to_by_authors(comments, ['basicbitch122'])
    [Comment(id='ha33z5m'), Comment(id='ha2sq62'), Comment(id='ha3d39f'),
      Comment(id='ha2s4lw'), Comment(id='ha3mrwm'), Comment(id='ha3m2kv'),
      Comment(id='ha5okfd'), Comment(id='ha7e0ei'), Comment(id='hbpxpi1'),
      Comment(id='ha4e526'), Comment(id='ha3837c'!), Comment(id='hdo2kmm'!),
      Comment(id='ha3f5q2'), Comment(id='hdof500'), Comment(id='hdol6rn'),
      Comment(id='hcrklp6')]
      
      
    >>>>>> url = 'https://www.reddit.com/r/mcgill/comments/1wfq5s/should_i_switch_majors/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_out_comments_replied_to_by_authors(comments, ['Fitbumblebee'])
    [Comment(id='cf1p5x0'), Comment(id='cf1ls9i'), Comment(id='cf2ajrb'), \
    Comment(id='cf1uqxd'), Comment(id='cf1kn75'), Comment(id='cf5kepp'), \
    Comment(id='cf3ilv3'), Comment(id='cf1tke2'), Comment(id='cf3khdo'), \
    Comment(id='cf4y0h4'), Comment(id='cf1tzht'), Comment(id='cf6fcxx'), \
    Comment(id='cf1w3uj'), Comment(id='cf1vf7l'), Comment(id='cf206n9'), Comment(id='cf1vlo9')]
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/o6wqtr/7_courses_in_one_semester/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_out_comments_replied_to_by_authors(comments, ['pudding-pudding', 'PatrickLu1999', 'Juan_Carl0s', 'arimill', 'codepoetz'])
    [Comment(id='h2wspl3'), Comment(id='h2xek43'), Comment(id='h2wt5lx'), \
    Comment(id='h2yaif5'), Comment(id='h2x1rcb'), Comment(id='h2x26bv'), \
    Comment(id='h2zv8ox'), Comment(id='h2w5op9'), Comment(id='h2w62x6'), \
    Comment(id='h2zvakq'), Comment(id='h2zvbmb'), Comment(id='h2zvclq'), \
    Comment(id='h2zvcdw'), Comment(id='h2zvfqp'), Comment(id='h2xi7h0'), \
    Comment(id='h2yo6hq'), Comment(id='h30ai95'), Comment(id='h3gzt7q'), Comment(id='h30ebrg')] 
    """
    
    filtered_list = []

    for comment in comments:
        
        # First case: the comment has been replied       
        if list(comment.replies) != []:
            
            replies_author = ''
            
            # Record every authors of replies 
            for reply in list(comment.replies):
                
                replies_author+=str(reply.author)
            
            # Two conditions: comment not posted by listed author and this comment was not replied by the listed authors
            if ' '.join(list_of_author_names) not in replies_author and comment.author not in list_of_author_names:
                filtered_list.append(comment)    
                   
        # Second case: the comment has not been replied, so only one condition need to be reached
        elif comment.author not in list_of_author_names:
            filtered_list.append(comment)
                
            
    return filtered_list

def get_authors_from_topic(submission):
    """ (submission) -> dict

    >>> url = 'https://www.reddit.com/r/mcgill/comments/pa6ntd/does_mcgill_have_a_taylor_swift_society/'
    >>> submission = reddit.submission(url=url)
    >>> num_comments_per_author = get_authors_from_topic(submission)
    >>> len(num_comments_per_author)
    23
    >>> num_comments_per_author['basicbitch122']
    12
     
    >>> url = 'https://www.reddit.com/r/mcgill/comments/o6wqtr/7_courses_in_one_semester/'
    >>> submission = reddit.submission(url=url)
    >>> num_comments_per_author = get_authors_from_topic(submission)
    >>> len(num_comments_per_author)
    12
    >>> num_comments_per_author['PatrickLu1999']
    3
    
    >>> url ='https://www.reddit.com/r/mcgill/comments/r0q4bl/advice_before_taking_math240/'
    >>> num_comments_per_author = get_authors_from_topic(submission)
    >>> submission = reddit.submission(url=url)
    >>> len(num_comments_per_author)
    7
    >>> num_comments_per_author['NdersonCouncil']
    1
    """
    final_dict = {}
    all_comments = get_topic_comments(submission)
    
    for comment in all_comments:
        
        # In case some comments were delated
        if comment.author == None:
            continue
        num_of_comment =  len(filter_comments_from_authors(all_comments, comment.author.name.split()))
        final_dict[comment.author.name] = num_of_comment 
    
    return final_dict



def select_random_submission_url(reddit, topic_url, subreddit_name, replace_limit):
    """(reddit, str, str, int or None) -> submission
    Returns the url of submission
    Only if die equals 1 or 2, topic_url is returned. Otherwise, a random url will be selected from top submission of a subreddit named
    subreddit_name
    replace_limit indicates how many following comments we decide to load. 
    """
   
   # Roll a six-sided die
    die = random.randint(1,6)
    top_submission = []
    
    if die == 1 or die ==2:
        submission = reddit.submission(url=topic_url)
        submission.comments.replace_more(limit=replace_limit)
        return submission
    
    else:
        for submission in reddit.subreddit(subreddit_name).top(time_filter="all"):
            top_submission.append(submission)
            random_top_submission = random.choice(top_submission)
            random_top_submission.comments.replace_more(limit=replace_limit)
            return random_top_submission
           


def post_reply(submission, username):
    """ (submission, str) -> NoneType
    Enables to post a reply in a specific submission under account username
    if the user has replied to this submission, then choose a comment that the user has not replied to reply
    if the user has not replied to this submission, creat a new top-level comment
    """
    all_comments = []
    comments = get_topic_comments(submission)
    list_of_author_names = [username]
    dict_of_authors = get_authors_from_topic(submission)
    # Check if the user has added a top-level comment in the submission
    if username not in dict_of_authors :
        submission.reply(madlibs.generate_comment())
    else:
        comment = random.choice(filter_out_comments_replied_to_by_authors(comments, list_of_author_names))
        comment.reply(madlibs.generate_comment())
    
    
def bot_daemon(reddit, starting_topic_url, replace_limit, subreddit_name, new_username):
    """ (reddit, str, int or None, str, str) -> NoneType
    Post replies in the submission chosen by select_random_submission_url function every 60 seconds
    """
    
    while True:
        submission = select_random_submission_url(reddit, starting_topic_url, subreddit_name, replace_limit)
        post_reply(submission,new_username)
        time.sleep(60)
        
if __name__ == "__main__":
    reddit = praw.Reddit('bot', config_interpolation="basic")
    

