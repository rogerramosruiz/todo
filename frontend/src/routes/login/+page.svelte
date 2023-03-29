<script>
    import { goto } from '$app/navigation';
    import {request} from '../../lib/request/request'

    let username="", password = ""

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

<main>
    <form on:submit|preventDefault={submit}>
        <h1>Please sign in</h1>
        <div>
            <label for="username">Username</label>
            <input id="username" type="text" bind:value ={username} placeholder="username">
        </div>
        <div>
            <label for="password">Password</label>
            <input id="password" type="password" bind:value = {password} placeholder="Password">
        </div>
        <button type="submit">Submit</button>
    </form>
</main>