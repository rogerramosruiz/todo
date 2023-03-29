<script>
    import {taskStore} from '../../lib/store/taskStore'
    import {request } from '../request/request'
    export let task
    
    let editing = false
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
    async function edit(){
        const resp = await request(`api/v1/task/${task.id}`, true, 'PUT', task)
        if (resp.status !== 202){
            console.log(resp)
            return
        }

        $taskStore = $taskStore
    }
    async function save(){
        edit()
        editing = false
    }
  
</script>

<div>
    {#if !editing}
        {task.name}
        {task.done}
        <button on:click={()=>editing=true}>
            edit
        </button>
        {:else}
        <input bind:value={task.name}>
        <button on:click={save}>
            save
        </button>

    {/if}
        <button on:click={remove}>
            delete
        </button>
</div>