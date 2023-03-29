<script>
    import {taskStore} from '../../lib/store/taskStore'
    import {request } from '../helpers/request'
    import Icon from 'svelte-icons-pack/Icon.svelte';
    import AiOutlineNodeExpand from 'svelte-icons-pack/ai/AiOutlineNodeExpand';
    import plus from 'svelte-icons-pack/im/ImPlus';
    

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


<div class="grid place-items-center w-screen m-5">
    <form on:submit|preventDefault={createTask} class="bg-gray-50 shadow-md rounded px-8 pt-6 pb-8 m-10 lg:w-1/4 w-full">  
        <div class="flex align-middle">
            <input id="name" type="text" bind:value ={name} placeholder="task name" class="w-full p-2 text-sm border-b-2 border-gray-400 outline-none opacity-50 focus:border-blue-500">
            <button 
            class="bg-blue-500 hover:bg-blue-700 text-white fill-white font-bold py-2 px-4 rounded-full focus:outline-none focus:shadow-outline mx-5"
            type="submit">
            Add
        </button>
        </div>
    </form>

</div>