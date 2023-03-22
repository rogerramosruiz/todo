from db.task import select, add, edit
from helpers.serilizer import serilize_list


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
    
def create_task(data):
    name = data.get('name', '')
    id_user = data.get('id_user', 0)
    if name == '':
        return {'message':'name required'}, 400
    if id_user == 0:
        return {'message':'id_user required'}, 400
    if type(name) != str:
         return {'message':'name shoudl be string'}, 400   
    id = add(name, id_user)
    return {'id': id}, 201

def edit_task(id, data):
    try:
        name = data.get('name', '')
        done = data.get('done')
        if name == '':
            return {'message':'name required'}, 400
        
        if done is None:
            return {'message':'done required'}, 400

        if type(name) != str:
            return {'message': f'name should be string'}, 400
        if type(done) != bool:
            return {'message': f'done should be type boolean'}, 400
        
        edit(id, name, done)

    except Exception as e:
        print(e)
        return {'message': 'Internal server error'}, 500
    return {'message': 'Success'}, 202