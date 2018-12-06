from user import User
from random import shuffle

def gale_shapley(users):
    # map of team ids to collection of users reviewing them
    assigned_users = []
    
	# randomize users for fairness
    shuffle(users)
    
    # choose the highest ranked team available for each user
    for user in users:
    
        #for each team id in user.topic_rank
        for team in user.topic_rank:
        
            # if team id is in the map
                # fewer than MAX REVIEWERS, assign user to this review
                # MAX REVIEWERS, fall through to next team id
            #if team id is not in the map, insert it and assign user to this review
            
	return assigned_users