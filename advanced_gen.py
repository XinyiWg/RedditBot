import markovify
import time
import reddit as r
import madlibs
import praw
import random



def advance_gen(num_of_sentences):
    """(int) -> str
    Returns a reply that is going to be posted with num_of_sentences sentences.
    >>> advance_gen(2)
    'Never ever vote for Alex. Imagine the passing grade? '
    
    >>> advance_gen(3)
    'We do need a leader who is able to pose your toughest questions and get a response direct from the candidate! \
    Here are your candidates for the CSSSMU Executive 2022-2023 is about to begin!! According to the point, \
    we tend to think that if we get to the key of the CodePost tests for it to pass. '
    
    >>> advance_gen(1)
    'He deserves a chance to be a truly adult! '
    """
    filename = 'advanced_genfile.txt'
    text = open(filename,'r')

    # Build the model.
    text_model = markovify.Text(text,state_size = 2)
    text.close()

    # sentence will be replied
    whole_reply = ''
    for i in range(num_of_sentences):
        each_sentence = text_model.make_sentence(tries = 100) + ' '
        whole_reply += each_sentence
    
    return whole_reply
            



def post_advance_reply(submission, username, num_of_sentences):
    """ (submission, str, int) -> NoneType
    num_of_sentences indicates exactly how many sentences you want to include in a reply
    """
    all_comments = []
    comments = r.get_topic_comments(submission)
    list_of_author_names = [username]
    dict_of_authors = r.get_authors_from_topic(submission)
    if username not in dict_of_authors :
        submission.reply(advance_gen(num_of_sentences))
    else:
        comment = random.choice(r.filter_out_comments_replied_to_by_authors(comments, list_of_author_names))
        comment.reply(advance_gen(num_of_sentences))


def bot(reddit, starting_topic_url, replace_limit, subreddit_name, new_username, num_of_sentences):
    """(reddit, str, int or None, str, str, int) -> NoneType
    post a reply per 60 seconds by calling the function
    """
    while True:
        submission = r.select_random_submission_url(reddit, starting_topic_url, subreddit_name, replace_limit)
        post_advance_reply(submission,new_username, num_of_sentences)
        time.sleep(60)
    
if __name__ == "__main__":
    reddit = praw.Reddit('bot', config_interpolation="basic")
