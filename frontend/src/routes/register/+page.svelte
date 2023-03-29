<script>
    import { goto } from '$app/navigation';
    import {request} from '../../lib/request/request'
    
    let username="", password = "", confirmation=""
    let message = ""

    $: submit = async() =>{
        const response = await request('api/v1/auth/signup', false, 'POST', {
            username:username,
            password:password,
            confirmation_password: confirmation
        })
        const data = await response.json()
        if(response.status == 201){
            message = 'user created, redirecting to login'
            setTimeout(() =>goto('login'), 2000) 
        }
        else{
            message = data.message
        }
    }
</script>

<main>
    
    <form on:submit|preventDefault={submit}>
        <h1>Sign up</h1>
        <div>
            <label for="username">Username</label>
            <input id="username" type="text" bind:value = {username} placeholder="username">
        </div>
        <div>
            <label for="password">Password</label>
            <input id="password" type="password" bind:value={password} placeholder="Password">
        </div>
        <div>
            <label for="confirmation">Passowrd confirmation</label>
            <input id="confirmation" type="password" bind:value={confirmation} placeholder="Password">
        </div>
        <button type="submit">Submit</button>
    </form>

    <div>
        <h1>{message}</h1>
    </div>

</main>