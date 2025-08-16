export default defineNuxtRouteMiddleware((to, _from) => {
    const auth = useAuth() //Or any other auth technique

    console.log(auth)
    if (to.path === "/" && !auth.isAuthenticated.value) {
        return navigateTo("/login")
    }
})
