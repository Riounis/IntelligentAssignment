'''
The way to call this method
    user_ranks = [{
        "pid": 1,
        "ranks": [1,2,3]
    },{
        "pid": 2,
        "ranks": [3,1,2]
    }, {
        "pid": 3,
        "ranks": [2,3,1]
    }, {
        "pid": 4,
        "ranks": [2,1,3]
    }, {
        "pid": 5,
        "ranks": [1,2,3]
    }]
    print gale_shapley(user_ranks, 2, 2)
'''
from random import shuffle

def gale_shapley(users, item_size, assign_size):

    # randomize users for fairness
    shuffle(users)

    # construct a user priority list for every item
    item_ranks = {}
    for user in users:
        for i, item in enumerate(user["ranks"]):
            if not item in item_ranks:
                item_ranks[item] = []
            #every item hold a list of priority of users
            item_ranks[item].append({"pid": user["pid"], "priority": i})

    assigned_item_count = {}
    item_assigned = {}

    # sort the item ranks by user's priority so that the algorithm can select the most interested users
    for item in item_ranks:
        item_ranks[item].sort(key=lambda x: x["priority"])
        assigned_item_count[item] = 0

    # start bidding
    for item in item_ranks:
        # select the most interested users
        for user in item_ranks[item]:
            # if number of user for each item exceeds its limit:
            # the assignment for this item is finished
            if assigned_item_count[item] >= item_size:
                break
            user_id = user["pid"]
            if user_id not in item_assigned:
                item_assigned[user_id] = []
            # if user has enough assignment, choose another user with less interest.
            if len(item_assigned[user_id]) >= assign_size:
                continue
            item_assigned[user_id].append(item) 
            assigned_item_count[item] += 1

    rst = []
    for user in item_assigned:
        rst.append({"pid": user, "items": item_assigned[user]})
    return rst
