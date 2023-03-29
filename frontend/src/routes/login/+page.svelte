<script>
    import { goto } from '$app/navigation';
    import {request} from '../../lib/helpers/request'
    import {onMount} from "svelte"
    import {isLoggedIn} from '../../lib/helpers/helper'
    
    let username="", password = ""
  

    onMount(() => {
      if(isLoggedIn()){
        goto('/')
      }
    })
 
    $: submit = async() =>{
        const response = await request('api/v1/auth/login',false, 'POST',  {
            username, 
            password
        })
        const data = await response.json()
        localStorage.accessToken = data.access_token
        localStorage.refreshToken = data.refresh_token
        goto('/')
    }
</script>
<nav class="flex justify-end">
    <button 
    on:click={()=>goto('signup')}
    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 m-5 rounded focus:outline-none focus:shadow-outline" type="submit">
        Sign up
    </button>
</nav>
<div class="grid place-items-center sm:h-4 w-screen h-screen">
  <form on:submit|preventDefault={submit} class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-96 md:mb-0 md:mt-28 lg:w-1/4 ">
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
      <input bind:value = {password} class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="******************">
      <!-- <p class="text-red-500 text-xs italic">Please choose a password.</p> -->
    </div>
    <div class="grid place-items-center">
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
        Login
      </button>
    </div>
  </form>
</div>