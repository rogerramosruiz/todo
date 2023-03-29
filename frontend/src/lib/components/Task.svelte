<script>
    import {taskStore} from '../../lib/store/taskStore'

    export let task
    
    let edit = false
    function save(){
        edit = false
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
        <input value={task.name} class="">
        <button on:click={save}>
            save
        </button>

    {/if}
        <button>
            delete
        </button>
</div>