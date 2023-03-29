<script>
    import {taskStore} from '../../lib/store/taskStore'
    import {request } from '../request/request'
    export let task
    
    let edit = false
    function save(){
        edit = false
    }
    async function remove(){
    const resp = await request(`api/v1/task/${task.id}`, true, 'DELETE')
    if (resp.status == 202){
        console.log('deleted')
        $taskStore = $taskStore.filter((t)=> t.id !== task.id)
    }
    else{
        console.log(resp)
    }
    }
    
</script>

<div>
    {#if !edit}
        {task.name}
        {task.done}
        <button on:click={()=>edit=true}>
            edit
        </button>
        {:else}
        <input value={task.name}>
        <button on:click={save}>
            save
        </button>

    {/if}
        <button on:click={remove}>
            delete
        </button>
</div>