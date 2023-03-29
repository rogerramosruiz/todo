import {PUBLIC_API_URL} from '$env/static/public'


export async function request(url, auth=false, method = 'GET', body){
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

    return resp
}