<script>
    import {onMount} from "svelte"
    import { goto } from '$app/navigation'
    import {request} from '../lib/request/request'
    import Task from "../lib/components/Task.svelte";


    let tasks = []
    
    onMount(async () => {
        if(localStorage.accessToken == null || localStorage.refreshToken == null){
            goto('login')
            return
        }
        const resp = await request('api/v1/task', true)
        if (resp.status === 200)
            tasks = await resp.json()
        })




</script>

<main>
    <h1>Tasks</h1>    
    {#each tasks as task}
		<li>
            <Task task={task}/>
		</li>
	{/each}

</main>