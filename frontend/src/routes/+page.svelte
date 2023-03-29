<script>
    import {taskStore} from '../lib/store/taskStore'
    import {onMount} from "svelte"
    import { goto } from '$app/navigation'
    import {request} from '../lib/request/request'
    import Task from "../lib/components/Task.svelte";

    let name = ''

    onMount(async () => {
        if(localStorage.accessToken == null || localStorage.refreshToken == null){
            goto('login')
            return
        }
        const resp = await request('api/v1/task', true)
        if (resp.status === 200)
            $taskStore = await resp.json()
     })

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
        <h1>Please sign in</h1>
        <div>
            <label for="name">Task name</label>
            <input id="name" type="text" bind:value ={name} placeholder="task name">
        </div>
        <button type="submit">Submit</button>
    </form>


    <h1>Tasks</h1>    
    {#each $taskStore as task}
		<li>
            <Task task={task}/>
		</li>
	{/each}

</main>