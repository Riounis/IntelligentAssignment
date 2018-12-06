from review_bid_list import ReviewBidList
from review_group import ReviewGroup
from random import shuffle

def gale_shapley(user_preferences):
    # max number of reviewers on a topic
    max_reviewers = user_preferences.review_size
    
    # map of team ids to collection of users reviewing them
    team_reviewer_map = []
    
	# randomize users for fairness
    shuffle(user_preferences.participants)
    
    # for each participant
    for participant in user_preferences.participants:
    
        #for each team in that participant's priority list
        for teamid in participant.teams:
        
            found = 0
            appended = 0
            for review_group in team_reviewer_map:
                # if team id is in the map
                if review_group.teamid == teamid:
                    found = 1
                    # fewer than MAX REVIEWERS, assign user to this review
                    if len(review_group.users) < max_reviewers:
                        review_group.users.append(participant.participant_id)
                        appended = 1
                    # MAX REVIEWERS, fall through to next team id
                    break

            #if team id is not in the map, insert it and assign user to this review
            if found == 0:
                user_list = []
                user_list.append(participant.participant_id)
                team_reviewer_map.append(ReviewGroup(teamid, user_list))
                appended = 1
            if appended == 1:
                break
            
    return team_reviewer_map
