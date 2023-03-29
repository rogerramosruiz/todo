<script>
    import { goto } from '$app/navigation';
    import {request} from '../../lib/request/request'
    
    let username="", password = "", confirmation=""
    let error = false
    let message = ""

    $: submit = async() =>{
        console.log('requesting ')
        const response = await request('api/v1/auth/signup', false, 'POST', {
            username:username,
            password:password,
            confirmation_password: confirmation
        })
        const data = await response.json()
        if(response.status == 201){
            message = 'User created, redirecting to login'
            setTimeout(() =>goto('login'), 1000) 
            error = false
        }
        else{
            error = true
            message = data.message
        }
    }
</script>

<nav class="flex justify-end">
    <button 
    on:click={()=>goto('login')}
    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 m-5 rounded focus:outline-none focus:shadow-outline" type="submit">
        Login
    </button>
</nav>

<div class="grid place-items-center sm:h-4 w-screen">
    <form on:submit|preventDefault={submit} class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 lg:w-1/4 ">
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
          Username
        </label>
        <input bind:value={username} class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="Username">
      </div>
      <div class="mb-6">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
          Password
        </label>
        <input bind:value={password} class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="******************">
      </div>
      <div class="mb-6">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="confirmation">
            Confirmation
        </label>
        <input bind:value = {confirmation} class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="confirmation" type="password" placeholder="******************">
      </div>
      <div class="grid place-items-center">
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
          Sign up
        </button>
        <div>
            {#if !error}
                <h1 class="text-green-600": >{message}</h1>
            {:else}
                <h1 class="text-red-600": >{message}</h1>
            {/if}
          
      </div>
      </div>
    </form>
  </div>
