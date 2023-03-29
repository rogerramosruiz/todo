<script>
    import {taskStore} from '../lib/store/taskStore'
    import {onMount} from "svelte"
    import { goto } from '$app/navigation'
    import {request} from '../lib/request/request'
    import Task from "../lib/components/Task.svelte";
    import taskCreate from '../lib/components/taskCreate.svelte'
    import TaskCreate from '../lib/components/taskCreate.svelte';

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

<nav class="flex justify-end">
    <button 
    on:click={()=>goto('login')}
    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 m-5 rounded focus:outline-none focus:shadow-outline" type="submit">
        Logout 
    </button>
</nav>

<main>
    <TaskCreate />
    <h1>Tasks</h1>    
    {#each $taskStore as task}
		<li>
            <Task task={task}/>
		</li>
	{/each}

</main>