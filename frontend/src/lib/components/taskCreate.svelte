<script>
    import {taskStore} from '../../lib/store/taskStore'
    import {request } from '../request/request'


    let name = ''

     async function createTask(){
        if (name == ''){
            console.log('tasname emtpy')
            return
        }
        let body = {
            name
        }
        const resp = await request('api/v1/task', true, 'POST', body)
        const data = await resp.json()
        if(resp.status === 201){
            $taskStore = [{
                id: data.id,
                done: false,
                name: name
            },
            ...$taskStore
        ]
        }

        name = ''
    }

     
</script>


<main>
    <form on:submit|preventDefault={createTask}>
        <div>
            <label for="name">Task name</label>
            <input id="name" type="text" bind:value ={name} placeholder="task name">
        </div>
        <button type="submit">Submit</button>
    </form>

</main>