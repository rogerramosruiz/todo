<script>
    import {taskStore} from '../lib/store/taskStore'
    import {onMount} from "svelte"
    import { goto } from '$app/navigation'
    import {request, logout } from '../lib/helpers/request'
    import Task from "../lib/components/Task.svelte";
    import TaskCreate from '../lib/components/taskCreate.svelte';
    import {isLoggedIn} from '../lib/helpers/helper'
    let name = ''

    onMount(async () => {
        if(!isLoggedIn()){
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
    on:click={logout}
    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 m-5 rounded focus:outline-none focus:shadow-outline" type="submit">
        Logout 
    </button>
</nav>

<div class="grid place-items-center w-screen">
    <TaskCreate />
    <h1>Tasks</h1>    
    <div >
        {#each $taskStore as task}
            <Task task={task}/>
        {/each}
    </div>

</div>