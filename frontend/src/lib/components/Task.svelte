<script>
    import {taskStore} from '../../lib/store/taskStore'
    import {request } from '../helpers/request'
    export let task
    
    let editing = false
    $: color = task.done?'bg-green-500':'bg-yellow-400'
    async function remove(){
        const resp = await request(`api/v1/task/${task.id}`, true, 'DELETE')
        if(resp.status !== 202){
            console.log(resp)
            return
        }
        $taskStore = $taskStore.filter((t)=> t.id !== task.id)
    }
    async function updateCheck(){
        task.done = !task.done
        edit()
    }
    
    async function edit(){
        const resp = await request(`api/v1/task/${task.id}`, true, 'PUT', task)
        if (resp.status !== 202){
                return
        }
        $taskStore = $taskStore
    }
    async function save(){
        edit()
        editing = false
    }
  
</script>
<div class="flex space-x-5 bg-shadow-md rounded-3xl p-3 bg-gray-100 m-3 w-full ">
    <div class="grid">  
        <button class="m-2" on:click={remove}>
            <svg
			class="fill-red-400 hover:fill-red-700"
			width="25"
			height="25"
			viewBox="0 0 32 32"
			xmlns="http://www.w3.org/2000/svg">
			<g clip-path="url(#clip0_35_392)">
				<path
					d="M24 6.4H32V9.6H28.8V30.4C28.8 30.8244 28.6314 31.2313 28.3314 31.5314C28.0313 31.8314 27.6243 32 27.2 32H4.8C4.37565 32 3.96869 31.8314 3.66863 31.5314C3.36857 31.2313 3.2 30.8244 3.2 30.4V9.6H0V6.4H8V1.6C8 1.17565 8.16857 0.768688 8.46863 0.468629C8.76869 0.168571 9.17565 0 9.6 0H22.4C22.8243 0 23.2313 0.168571 23.5314 0.468629C23.8314 0.768688 24 1.17565 24 1.6V6.4ZM25.6 9.6H6.4V28.8H25.6V9.6ZM18.2624 19.2L21.0912 22.0288L18.8288 24.2912L16 21.4624L13.1712 24.2912L10.9088 22.0288L13.7376 19.2L10.9088 16.3712L13.1712 14.1088L16 16.9376L18.8288 14.1088L21.0912 16.3712L18.2624 19.2ZM11.2 3.2V6.4H20.8V3.2H11.2Z"
				/>
			</g>
		</svg>
        </button>
        {#if !editing}
            <button class="m-2" on:click={()=>editing=true}>
                <svg class="fill-blue-500"  
                height="20" width="20" id="Layer_1" version="1.1" viewBox="0 0 19 19"  xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <g><path d="M8.44,7.25C8.348,7.342,8.277,7.447,8.215,7.557L8.174,7.516L8.149,7.69   C8.049,7.925,8.014,8.183,8.042,8.442l-0.399,2.796l2.797-0.399c0.259,0.028,0.517-0.007,0.752-0.107l0.174-0.024l-0.041-0.041   c0.109-0.062,0.215-0.133,0.307-0.225l5.053-5.053l-3.191-3.191L8.44,7.25z" /><path d="M18.183,1.568l-0.87-0.87c-0.641-0.641-1.637-0.684-2.225-0.097l-0.797,0.797l3.191,3.191l0.797-0.798   C18.867,3.205,18.824,2.209,18.183,1.568z" /><path d="M15,9.696V17H2V2h8.953l1.523-1.42c0.162-0.161,0.353-0.221,0.555-0.293   c0.043-0.119,0.104-0.18,0.176-0.287H0v19h17V7.928L15,9.696z"/></g></svg>
            </button>
        {:else}
            <button class="m-2" on:click={save}>
                <svg class="fill-gray-700 hover:fill-slate-900" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
                width="25" height="25" 
                viewBox="0 0 407.096 407.096"
                xml:space="preserve">
            <g>
                <g>
                    <path d="M402.115,84.008L323.088,4.981C319.899,1.792,315.574,0,311.063,0H17.005C7.613,0,0,7.614,0,17.005v373.086
                        c0,9.392,7.613,17.005,17.005,17.005h373.086c9.392,0,17.005-7.613,17.005-17.005V96.032
                        C407.096,91.523,405.305,87.197,402.115,84.008z M300.664,163.567H67.129V38.862h233.535V163.567z"/>
                    <path d="M214.051,148.16h43.08c3.131,0,5.668-2.538,5.668-5.669V59.584c0-3.13-2.537-5.668-5.668-5.668h-43.08
                        c-3.131,0-5.668,2.538-5.668,5.668v82.907C208.383,145.622,210.92,148.16,214.051,148.16z"/>
                </g>
            </g>
            </svg>
            </button>
        {/if}
    </div>

    <div class="flex space-x-4 mt-3 font-medium w-full justify-items-center">
        <div class="flex space-x-5">
            <div class="mt-5">
                <input class=" text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500"
                on:click={updateCheck} checked={task.done} type="checkbox" >
            </div>
            <div class="mt-5">
                {#if !editing}
                <p>
                    {task.name}
                </p>
                {:else}
                <input class="w-full p-2 text-sm border-b-2 border-gray-400 outline-none opacity-50 focus:border-blue-500" bind:value={task.name}>
                {/if}
            </div>
        </div>
        <div class="{color} rounded-3xl text-white">
            <div class="px-2 py-4">
                {#if task.done}
                    Completed
                {:else}
                    In progress
                {/if}
            </div>
        </div>
    </div>
</div>