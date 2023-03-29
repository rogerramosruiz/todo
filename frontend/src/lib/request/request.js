import {PUBLIC_API_URL} from '$env/static/public'
import { goto } from '$app/navigation';


async function refreshToken(){
    console.log('refreshing token')
    const header = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.refreshToken}`
    }

    const resp = await fetch(`${PUBLIC_API_URL}/api/v1/auth/token`, {
        headers: header,
    })
    if(resp.status === 401 ){
        localStorage.clear()
        goto('login')
        return false
    }
    if(resp.status === 200){
        const data = await resp.json()
        localStorage.accessToken = data.access_token
        localStorage.accessTime = data.expires_in
        return true
    }
}

export async function request(url, auth=false, method = 'GET', body,){
    const header = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    if(auth){
        header.Authorization = `Bearer ${localStorage.accessToken}`
    }
    if(body)
        body = JSON.stringify(body)

    let resp = await fetch(`${PUBLIC_API_URL}/${url}`, {
        method: method,
        headers: header,
        body: body
    })
    
    if(resp.status === 401 && auth){
       const success = await refreshToken()
       header.Authorization = `Bearer ${localStorage.accessToken}`
        if(success){
            resp = await fetch(`${PUBLIC_API_URL}/${url}`, {
                method: method,
                headers: header,
                body: body
            })      
        }
    }
    return resp

}