from db.task import select
from helpers.serilizer import serilize, serilize_list


def get_tasks(id_users, args):
    try:
        # Get qury paraetrs limit and offset
        limit = args.get("limit", default=10, type=int)
        offset = args.get("offset", default=0, type=int)
        limit = min(limit, 30)
        offset = max(offset, 0)
        # get data from database
        data, description = select(id_users, limit, offset)
        # serilize data
        tasks = serilize_list(data, description)
        return tasks
    except Exception as e:
        print(e)
        return {'message': "Internal server error"}, 500