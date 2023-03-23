from db.task import select,select_one, add, edit, delete
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

def get_task(id_user, id):
    try:
        data, description = select_one(id_user, id)
        if data is None:
            return {'message': 'Task not found'}, 404
        task = serilize(data, description)    
        return task
    except Exception as e:
        print(e)
        return {'message': "Internal server error"}, 500
    
def create_task(id_user, data):
    name = data.get('name', '')
    if name == '':
        return {'message':'name required'}, 400
    if type(name) != str:
         return {'message':'name shoudl be string'}, 400   
    id = add(name, id_user)
    return {'id': id}, 201

def edit_task(id_user, id, data):
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
        
        task, _ = select_one(id_user, id )
        if task is None:
            return {'message': "task dosen't exist"}, 400
        
        edit(id, name, done, id_user)
    except Exception as e:
        print(e)
        return {'message': 'Internal server error'}, 500
    
    return {'message': 'Success'}, 202

def delete_task(id_user, id):
    try:
        delete(id, id_user)
        return {"message": "Success"}, 202
    except:
        return {'message': 'Internal server error'}, 500