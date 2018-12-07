'''
The way to call this method
user_ranks = [{"pid":1,"ranks":[1,2,3]},{"pid":2,"ranks":[3,1,2]},{"pid":3,"ranks":[2,3,1]},{"pid":4,"ranks": [2,1,3]},{"pid":5,"ranks": [1,2,3]}]
print gale_shapley(user_ranks, 2, 2)
'''
from random import shuffle

def gale_shapley(users, user_size, item_size):
    """
    Description
    -----------
    Given the users preference towards items, the available slots of each item and
    maximum number each user can have items, assign items to users according to their preference.
    -----------
    Parameters
    -----------
    users       :   List[dict]
        dict format: {"pid": user_id, "ranks": [item_id]} the most interested items go first.
    user_size   :   int
    item_size   :   int
    -----------
    Return
    List[dict]
    """
    item_ranks = {}
    count_assigned_items = {}
    users_items = {}

    # construct a user priority list for every item
    for user in users:
        for i, item in enumerate(user["ranks"]):
            if not item in item_ranks:
                item_ranks[item] = []
            if not user["pid"] in users_items:
                users_items[user["pid"]] = []
            #every item hold a list of priority of users
            item_ranks[item].append({"pid": user["pid"], "priority": i})

    # sort the item ranks by user's priority so that the algorithm can select the most interested users
    for item in item_ranks:
        #randomize the order of users for fairness
        shuffle(item_ranks[item])
        item_ranks[item].sort(key=lambda x: x["priority"])
        count_assigned_items[item] = 0

    #randomize the order of items for fairness
    items = item_ranks.keys()
    shuffle(items)
    # start bidding
    while True:
        added = 0
        for item in items:
            # select the most interested users
            while item_ranks[item]:
                user = item_ranks[item].pop(0)
                # if item is assigned to a number of users and this number exceeds its limit:
                # the assignment for this item is finished
                if count_assigned_items[item] >= item_size:
                    break
                user_id = user["pid"]
                # if user has enough assignment, choose another user with less interest.
                if len(users_items[user_id]) >= user_size:
                    continue
                users_items[user_id].append(item)
                count_assigned_items[item] += 1
                added = 1
                break
        if not added: break

    rst = []
    for user in users_items:
        rst.append({"pid": user, "items": users_items[user]})
    return rst
