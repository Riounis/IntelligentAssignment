from user import User
from random import shuffle

def gale_shapley(users):
    # map of team ids to collection of users reviewing them
    assigned_users = []
    
	# randomize users for fairness
    shuffle(users)
    
    # choose the highest ranked team available for each user
    for user in users:
        
        # if team id is in the map
            # fewer than MAX REVIEWERS, assign user to this review
            # MAX REVIEWERS, fall through to next topic
        #if team id is not in the map, insert it and assign user to this review
            
	return assigned_users