import facebook, sentiment, make2
import numpy as np
import matplotlib.pyplot as plt

template = """therapist: No, please don't think like that, we are here for you
therapist: same, you are not alone
therapist: everything will get better soon enough
therapist: you should be positive my friend
therapist: be strong
therapist: have courage, my  friend
therapist: It doesn’t matter who you are, where you come from. The ability to triumph begins with you. Always.
therapist: Courage, dear heart.
therapist: In the middle of difficulty lies opportunity.
therapist: He who has a why to live can bear almost any how.
therapist: """

page_id = 147666920017094

post_id = '147666920017094_147683740015412'

entry=[]
sentiment_array=[]


page_token = 'EAAMHk5SfQbcBALn07ZAPGo9zJXceNm6RmS9uRnwd52n6XVX0E5CQF3hHZAVZBCbM6jRs2RIZBkZBzYu8a3NCjMjce2HKo33ColrzZBHdbgrGkWRnWqp8VxhZAoF6RvxhX1FmUdTbVfotlFhduq8GiZArP2O1ezcHpNpCp37GVJ5DUtKYWtf9aFOMc7OyatgEGZAJMgS2BFVarI2i5i15VZCYNKyHKrlPEmjrwhhuKrjFkSdgZDZD'
#page_token = '852755365183927|_Zh3java3z46AngTL0EUFtg6xpI'

graph = facebook.GraphAPI(access_token=page_token, 
                          version="3.1")

#get session info
default_info = graph.get_object(id=page_id)



def get_posts(my_post_id):
    global template,sentiment_array,entry
    count=0
    posts_25 = graph.get_object(id=my_post_id,fields='posts')
    liste = list(posts_25.values())[0].get('data')
    #print(liste)
    print('+'*50)
    for i in liste:
        #print(i)
        sender = i.get('from')
        message = str(i.get('message'))
        temp = 'Patien: '+message+'\n'+template
        post_id = str(i.get('id'))
        sentimentt, score = sentiment.print_sentiment_scores(message)
        if score<0:
            y =  make2.interact_model(subject= temp).split('therapist')[0]
            sentimentt1, score1 = sentiment.print_sentiment_scores(y)
        print('MESSAGE:  ',message)
        print('FROM:  ',sender)
        print('POST ID:  ',post_id)
        print(sentimentt)
        sentiment_array.append(score1)
        entry.append(count)
        count+=1
        
        if score<0:
            print('\n Here is Reply  ',y)
            #add_comment(post_id, str(y))
            print('here is the score  ',score1)
        print('\n\n')
    #print(posts_25)



def get_post_comments(my_post_id):
    global template
    # Get the comments from a post.
    comments = graph.get_connections(id=my_post_id, connection_name='comments')
    print('+'*50)
    liste = list(comments.values())[0]
    for i in liste:
        sender = i.get('from').get('name')
        message = i.get('message')
        comment_id = i.get('id')
        sentimentt, score = sentiment.print_sentiment_scores(message)
        print('MESSAGE:  ',message)
        print('FROM:  ',sender)
        print('COMMENT ID:  ',comment_id)
        print(sentimentt)
        print('\n\n')



#LIKE the post
def like_post(my_post_id):
    graph.put_like(object_id='comment_id')

# Write a comment on a post.
def add_comment(my_post_id, reply):
    graph.put_object(parent_object=my_post_id, connection_name='comments',message=reply)

def plot_result():
    global sentiment_array,entry
    data1 = np.squeeze(sentiment_array)
    data2 = np.squeeze(entry)
    plt.plot(data1) 
    plt.plot(data2)
    plt.show()


if __name__ == '__main__':
    get_posts(page_id)
    plot_result()

    
