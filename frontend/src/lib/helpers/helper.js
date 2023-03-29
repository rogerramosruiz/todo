import { browser } from '$app/environment';
export function isLoggedIn(){
    if (browser) {
        return localStorage.accessToken != undefined || localStorage.refreshToken != undefined
      }
}